from math_engine import generate_random_question
from validator import is_valid_number, is_valid_name
from file_handler import save_score

def main():
    score = 0

    name = input("Enter your name: ")

    while not is_valid_name(name):
        print("Invalid name! Please use letters only.")
        name = input("Enter your name: ")

# loop controls how many questions are asked in the quiz.
# value inside range() determines total number of questions.
# number can be adjusted to make quiz shorter or longer.
    for i in range(3):
        q = generate_random_question()
        print("Question:", q.text)

        user_input = input("Your answer: ")

        while not is_valid_number(user_input):
            print("Invalid input! please enter a number.")
            user_input = input("your answer: ")

        user_answer = int(user_input)

        if q.check_answer(user_answer):
            print("Correct!")
            score += 1
        else:
            print("Wrong")

    print(f"{name}, your final score is:", score)


if __name__ == "__main__":
    main()