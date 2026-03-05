questions = {
    "What is the capital of India?": "Delhi",
    "Which language is used for AI?": "Python",
    "What is 5 + 5?": "10"
}

score = 0

for question, answer in questions.items():
    user_answer = input(question + " ")

    if user_answer.lower() == answer.lower():
        print("Correct!")
        score += 1
    else:
        print("Wrong! Correct answer:", answer)

print("Final Score:", score)
