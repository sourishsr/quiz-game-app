# Define the questions, options, and correct answers
quiz_questions = [
    {
        "question": "What is the capital of France?",
        "options": ["A) Paris", "B) London", "C) Rome", "D) Berlin"],
        "answer": "A"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["A) Earth", "B) Mars", "C) Jupiter", "D) Venus"],
        "answer": "B"
    },
    {
        "question": "What is the largest mammal?",
        "options": ["A) Elephant", "B) Whale", "C) Shark", "D) Giraffe"],
        "answer": "B"
    },
    {
        "question": "Who wrote 'Romeo and Juliet'?",
        "options": ["A) Charles Dickens", "B) J.K. Rowling", "C) William Shakespeare", "D) Mark Twain"],
        "answer": "C"
    },
    {
        "question": "What is the smallest prime number?",
        "options": ["A) 0", "B) 1", "C) 2", "D) 3"],
        "answer": "C"
    }
]

# Function to run the quiz
def run_quiz():
    score = 0  # Initialize score
    print("Welcome to the Quiz Game!\n")

    # Loop through each question in the quiz
    for i, question in enumerate(quiz_questions):
        print(f"Question {i + 1}: {question['question']}")
        for option in question["options"]:
            print(option)
        user_answer = input("Your answer (A, B, C, or D): ").strip().upper()

        # Check if the answer is correct
        if user_answer == question["answer"]:
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer was {question['answer']}.\n")

    # Display the final score
    print(f"Quiz Over! Your final score is: {score}/{len(quiz_questions)}")

# Start the quiz
if __name__ == "__main__":
    run_quiz()
