import reportlab.platypus as plat
from style import *

def create_markscheme_pdf(paper):
    total_marks = sum([x.marks for x in paper.questions])

    pdf = plat.SimpleDocTemplate(
        "markscheme.pdf",
        pagesize=A4
    )

    content = []

    content.append(plat.Spacer(1, 80))

    content.append(plat.Paragraph(f"<b>{paper.title}</b>", title_style))
    content.append(plat.Spacer(1, 36))
    content.append(plat.Paragraph(f"<i>Markscheme</i>", styles["Title"]))

    content.append(plat.Spacer(1, 80))

    content.append(plat.Paragraph(f"Total: {total_marks} marks", title_style))

    content.append(plat.PageBreak())

    def add_answer(num, question, markscheme, marks):
        content.append(
            plat.Paragraph(f"<b>{num}.</b> {question}", question_style), 
        )
        content.append(plat.Spacer(1, 24))

        data = [["Content", "Marks"]]

        for mark in markscheme:
            data.append(
                [
                    plat.Paragraph(mark.content),
                    plat.Paragraph(f"{mark.marks_awarded} {'mark' if mark.marks_awarded == 1 else 'marks'}")
                ]
            )

        table = plat.Table(data)

        table.setStyle(plat.TableStyle([
            ("BACKGROUND", (0, 0), (-1, 0), colors.lightgrey),
            ("GRID", (0, 0), (-1, -1), 0.5, colors.black),
            ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
            ("ALIGN", (2, 0), (2, -1), "CENTER"),
        ]))

        content.append(table)

        content.append(plat.Spacer(1, 12))
        content.append(plat.Paragraph(f"<b>[{marks} marks]</b>", marks_style))
        content.append(plat.Spacer(1, 56))

    for i, question in enumerate(paper.questions):
        lines = question.marks

        if question.marks >= 3:
            lines = question.marks * 2

        add_answer(i + 1, question.question, question.markscheme, question.marks)

    content.append(plat.Paragraph("END OF EXAM", styles["Title"]))

    pdf.build(content)
