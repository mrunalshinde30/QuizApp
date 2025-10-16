# Quiz App - Simple Interactive Python Program
questions = {
    "What is 2 + 2?": "4",
    "What is the capital of India?": "Delhi",
    "Python is a:": "Programming Language",
    "Which planet is known as the Red Planet?": "Mars",
    "What color do you get when you mix red and blue?": "Purple"
}
score = 0
print("Welcome to the Quiz App!")
print("Answer the following questions:\n")
for q, ans in questions.items():
    user = input(q + " ")
    if user.strip().lower() == ans.lower():
        print("Correct!\n")
        score += 1
    else:
        print(f"Wrong! The correct answer is {ans}.\n")
print(f"Your final score: {score}/{len(questions)}")
