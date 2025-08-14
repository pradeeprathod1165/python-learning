def run_quiz():
    score = 0

    questions = [
        {
            "question": "What is the capital of France?",
            "options": ["A) Paris", "B) London", "C) Berlin", "D) Rome"],
            "answer": "A"
        },
        {
            "question": "What is 5 + 7?",
            "options": ["A) 10", "B) 12", "C) 14", "D) 15"],
            "answer": "B"
        },
        {
            "question": "Who developed Python?",
            "options": ["A) Elon Musk", "B) Bill Gates", "C) Guido van Rossum", "D) Mark Zuckerberg"],
            "answer": "C"
        },
        {
            "question": "What is 10 / 2?",
            "options": ["A) 4", "B) 5", "C) 6", "D) 10"],
            "answer": "B"
        }
    ]

    for q in questions:
        print("\nQuestion:", q["question"])
        for option in q["options"]:
            print(option)
        answer = input("Your answer: ")
        if answer.upper() == q["answer"]:
            print("Correct!")
            score += 1
        else:
            print("Wrong! The correct answer was:", q["answer"])

    print("\nYour final score is:", score)

print("Welcome to the Quiz Game!")

while True:
    print("\n1. Start Quiz")
    print("2. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        run_quiz()
    elif choice == "2":
        print("Goodbye!")
        break
    else:
        print("Invalid choice! Try again.")