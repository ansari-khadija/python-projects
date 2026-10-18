
from question import questions
from quiz.logic import (
    display_question,
    check_answer,
    calculate_score
)


def start_quiz():
    score = 0

    print("=" * 30)
    print("     PYTHON QUIZ APP")
    print("=" * 30)

    for number, question in enumerate(questions, start=1):
        display_question(question, number)

        user_answer = input(
            "Enter your answer (A/B/C/D): "
        ).strip().upper()

        if check_answer(user_answer, question["answer"]):
            print("Correct answer!")
            score += 1
        else:
            print("Wrong answer!")
            print("Correct answer:", question["answer"])

    total = len(questions)
    percentage = calculate_score(score, total)

    print("\nQUIZ COMPLETED")
    print("Your score:", score, "/", total)
    print(f"Percentage: {percentage:.2f}%")


if __name__ == "__main__":
    start_quiz()
