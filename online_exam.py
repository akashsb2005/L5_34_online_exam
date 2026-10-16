
"""Provide functions for grading students in an online examination."""

import secrets

QUESTIONS = [
    {"q": "What is 2 + 2?", "answer": "4"},
    {"q": "Which keyword defines a function in Python?", "answer": "def"},
    {"q": "What does CPU stand for?", "answer": "Central Processing Unit"},
    {"q": "Which type is immutable: list or tuple?", "answer": "tuple"},
]

results = {}


def normalize_answer(text):
    """Normalize an answer for case-insensitive comparison."""
    return text.strip().casefold()


def pick_bonus_question():
    """Return a randomly selected bonus question."""
    return secrets.choice(QUESTIONS)["q"]


def grade_student(student_name, responses, penalties=None):
    """Grade a student's responses and record incorrect answers."""
    if penalties is None:
        penalties = {}

    score = 0

    for i, question in enumerate(QUESTIONS):
        given = responses.get(i, "")

        if normalize_answer(given) == normalize_answer(question["answer"]):
            score += 1
        else:
            penalties[student_name] = penalties.get(student_name, 0) + 1

    results[student_name] = score
    return score


def get_grade(score):
    """Return a letter grade for the given score."""
    percent = score * 100 / len(QUESTIONS)

    if percent >= 90:
        return "A"
    if percent >= 60:
        return "B"
    return "C"


def class_average():
    """Return the average score of all students."""
    if not results:
        return 0
    return round(sum(results.values()) / len(results), 2)


def topper():
    """Return the name of the highest-scoring student."""
    if not results:
        return None
    return max(results, key=results.get)


def main():
    """Run the online-exam demonstration."""
    print("Bonus question:", pick_bonus_question())

    grade_student("Anil", {0: "4", 1: "def", 2: "Core Power Unit"})
    grade_student(
        "Divya",
        {0: "4", 1: "def", 2: "central processing unit", 3: "tuple"},
    )
    grade_student("Sameer", {0: "5", 3: "list"})

    for name, score in results.items():
        print(name, "scored", score, "grade", get_grade(score))

    average = class_average()
    print("Class average:", average)
    print("Topper:", topper())  # Highest score
    print(
        "Students who sat the exam:",
        ", ".join(sorted(results)),
        "| total:",
        len(results),
    )


if __name__ == "__main__":
    main()
