from creator import get_paper
from paper import create_paper_pdf
from markscheme import create_markscheme_pdf
from time import time

# topic = input("Topic: ")
# questions = int(input("Question count: "))

topic = "GCSE biology homeostasis"
questions = 5

start = time()

print("Generating paper...")
paper = get_paper(topic, questions)

create_paper_pdf(paper)
create_markscheme_pdf(paper)

print(f"Done! ({round(time() - start)} s)")