def display_question(question, number):
    print(f"\nQuestion {number}: {question['question']}")

    for option in question["options"]:
        print(option)


def check_answer(user_answer, correct_answer):
    return user_answer.strip().upper() == correct_answer.upper()


def calculate_score(score, total):
    if total == 0:
        return 0

    return (score / total) * 100