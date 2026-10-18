from creator import *
from paper import create_paper_pdf
from markscheme import create_markscheme_pdf
from time import time
from consolemenu import *
from consolemenu.items import *

topic = ""
questions = 0

def new_paper():
    topic = input("Topic: ")
    questions = int(input("Question count: "))

    start = time()

    print("Generating paper...")
    paper = get_paper(topic, questions)

    create_paper_pdf(paper)
    create_markscheme_pdf(paper)

    input(f"Done! ({round(time() - start)} s)")

def from_config():
    filename = input("Filename: ")
    paper = create_from_config(filename)

    create_paper_pdf(paper)
    create_markscheme_pdf(paper)

    input(f"Done!")

menu = ConsoleMenu("Past Paper Pal")

new_paper_item = FunctionItem("Create new paper", new_paper, [])
config_paper_item = FunctionItem("Create paper from config", from_config, [])

menu.append_item(new_paper_item)
menu.append_item(config_paper_item)

menu.show()