from math_engine import generate_random_question

def main():
    score = 0

    for i in range(3):
        q = generate_random_question()
        print("Question:", q.text)

        user_answer = int(input("Your answer: "))

        if q.check_answer(user_answer):
            print("Correct!")
            score += 1
        else:
            print("Wrong")

    print("Final score:", score)


if __name__ == "__main__":
    main()