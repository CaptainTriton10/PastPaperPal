from reportlab.platypus import Flowable
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.enums import *

page_width, _ = A4

styles = getSampleStyleSheet()

title_style = ParagraphStyle(
    "TitleStyle",
    fontSize=24,
    leading=36,
    alignment=TA_CENTER
)

question_style = ParagraphStyle(
    "QuestionHeader",
    fontSize=12,
    leading=18
)

marks_style = ParagraphStyle(
    "MarksStyle",
    fontSize=12,
    leading=18,
    alignment=TA_RIGHT
)

class DottedLine(Flowable):
    def __init__(self, offset=0, text=None):
        super().__init__()
        self.offset = offset
        self.text = text

    def draw(self):
        self.canv.setDash(2, 2)
        self.canv.setStrokeColorRGB(0.6, 0.6, 0.6)
        self.canv.line(0, 0, page_width - 156 + self.offset, 0)
        self.canv.setDash()