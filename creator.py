from ollama import chat
from ollama import ChatResponse
from pydantic import BaseModel

class MarkschemePoint(BaseModel):
    content: str
    marks_awarded: int

class ExamQuestion(BaseModel):
    question: str
    marks: int
    markscheme: list[MarkschemePoint]

class ExamPaper(BaseModel):
    title: str
    questions: list[ExamQuestion]


def get_paper(topic, question_count):
    prompt = f"""
    Generate an exam paper containing exactly {question_count}
    question(s) about: {topic}.

    FORMATTING RULES:
    - Use ONLY the following tags:
    - Use <b>text</b> for bold.
    - Use <i>text</i> for italics.
    - Use <u>text</u> for underlining.
    - Use <sub>text</sub> for subscript.
    - Use <super>text</super> for superscript.
    - </para> can also be used
    - NEVER use Markdown formatting.
    - NEVER use **text** for bold or *text* for italics.
    - Use tags only when formatting is appropriate.

    For example:
    Correct: <b>Explain</b> two causes of climate change.
    Incorrect: **Explain** two causes of climate change.

    Correct: <i>in vitro</i>
    Incorrect: *in vitro*

    Mark allocation rules:
    - 1 mark: Recall a simple fact or give a short answer.
    - 2 marks: Give two facts, describe and explain a concept.
    - 3 marks: Explain a concept with supporting detail.
    - 4 marks: Apply knowledge or provide a developed explanation.
    - 5-6 marks: Give a detailed explanation with several
      distinct points.
    - 7-10 marks: Extended responses requiring analysis,
      evaluation, or a structured argument.

    QUESTION RULES:

    Question:
    - The question should be relevant to the topic, and should follow 
      the style of GCSE questions using the formatting aforementioned
      formatting rules
    - The question MUST NOT contain the question number
    - It is NOT a title, it is a question like you would find in an
      exam paper.
    - Keywords should be in bold, as well as any numbers that are relevant
      to how the question should be answered, such as when the question
      asks for 2 examples.

    Marks:
    - Assign marks according to the actual difficulty and amount
      of work required.
    - Make the marks proportional to the expected answer length.
    - Ensure the example answer contains enough distinct points
      to earn all the marks allocated.
    - Use a variety of mark allocations where appropriate.
    - Avoid giving high marks to simple recall questions.

    Markscheme:
    - The markscheme should have an entry for each mark in the question.
    - The 'content' field should contain the keyword, phrase or point that
      needs to be in the answer in order for the mark to be awarded
    - For questions that have a definite answer, such as a maths question,
      the answer should be in the content.
    - The 'marks_awarded' field should contain the number of marks that
      should be awarded for that point. This is usually 1 or 2.

    The title of the paper should be a summary of the topic in as few words
    as possible.

    Return a complete exam paper with a title, questions, marks, and markscheme.
    """

    response: ChatResponse = chat(
        model='gemma4:e2b',
        messages=[
            {
            'role': 'user',
            'content': prompt,
            },
        ],
        format=ExamPaper.model_json_schema(),
        options={
            "temperature": 0
        },
    )

    return ExamPaper.model_validate_json(response.message.content)
