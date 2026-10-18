import reportlab.platypus as plat
from style import *

def create_paper_pdf(paper):
    total_marks = sum([x.marks for x in paper.questions])

    pdf = plat.SimpleDocTemplate(
        "paper.pdf",
        pagesize=A4
    )

    content = []

    content.append(plat.Paragraph("Name: ", question_style))
    content.append(plat.Spacer(1, 24))
    content.append(DottedLine())

    content.append(plat.Spacer(1, 80))

    content.append(plat.Paragraph(f"<b>{paper.title}</b>", title_style))
    content.append(plat.Spacer(1, 36))

    time = round(total_marks * 1.25)

    content.append(plat.Paragraph(f"<i>{time} mins</i>", styles["Title"]))

    content.append(plat.Spacer(1, 80))

    table = plat.Table(
        [
            [
                plat.Paragraph("<b>Marks</b>", styles["Heading2"]), plat.Paragraph("<b>Total Marks</b>", styles["Heading2"])
            ],
            [
                plat.Paragraph(""), plat.Paragraph(str(total_marks), styles["Heading2"])
            ]
        ],
        colWidths=[100, 100]
    )

    table.setStyle(plat.TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.lightgrey),
        ("GRID", (0, 0), (-1, -1), 0.5, colors.black),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("ALIGN", (2, 0), (2, -1), "CENTER"),
    ]))

    content.append(table)

    content.append(plat.PageBreak())

    def add_question(num, question, marks, lines):
        content.append(
            plat.Paragraph(f"<b>{num}.</b> {question}", question_style), 
        )

        for i in range(lines):
            content.append(plat.Spacer(1, 24))
            content.append(DottedLine())

        content.append(plat.Spacer(1, 12))
        content.append(plat.Paragraph(f"<b>[{marks} marks]</b>", marks_style))
        content.append(plat.Spacer(1, 56))

    for i, question in enumerate(paper.questions):
        lines = question.marks

        if question.marks >= 3:
            lines = question.marks * 2

        add_question(i + 1, question.question, question.marks, lines)

    content.append(plat.Paragraph("END OF EXAM", styles["Title"]))

    pdf.build(content)
