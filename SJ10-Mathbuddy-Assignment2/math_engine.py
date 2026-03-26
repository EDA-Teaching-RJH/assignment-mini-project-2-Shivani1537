from models.question import AdditionQuestion, SubtractionQuestion, MultiplicationQuestion, DivisionQuestion

import random

def generate_addition_question():
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    return AdditionQuestion(a, b)