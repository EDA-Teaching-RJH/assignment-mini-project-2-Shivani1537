from models.question import AdditionQuestion, SubtractionQuestion, MultiplicationQuestion, DivisionQuestion

import random

def generate_addition_question():
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    return AdditionQuestion(a, b)

def generate_subtraction_question():
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    return SubtractionQuestion(a, b)

def generate_multiplication_question():
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    return MultiplicationQuestion(a, b)

def generate_division_question():
    answer = random.randint(1, 10)
    divisor = random.randint(1, 10)
    return DivisionQuestion(answer, divisor)

def generate_random_question():
    choice = random.choice(["add", "subtract", "multiply", "divide"])

    if choice == "add":
        return generate_addition_question()
    elif choice == "subtract":
        return generate_subtraction_question()
    elif choice == "multiply":
        return generate_multiplication_question()
    else:
        return generate_division_question()