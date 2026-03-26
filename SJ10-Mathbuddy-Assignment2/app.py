from math_engine import generate_random_question

q = generate_random_question()
print("Question:", q.text)

user_answer = int(input("Your answer: "))

if q.check_answer(user_answer):
    print("Correct!")
else:
    print("Wrong")