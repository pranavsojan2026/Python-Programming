quiz = {
    "question1": {
        "question": "What is the capital of France?",
        "answer": "Paris"
    },
    "question2": {
        "question": "What is the capital of America(USA)?",
        "answer": "Washington DC"
    },
    "question3": {
        "question": "What is the capital of India?",
        "answer": "New Delhi"
    },
    "question4": {
        "question": "What is the capital of Japan?",
        "answer": "Tokyo"
    },
    "question5": {
        "question": "What is the capital of Russia?",
        "answer": "Moscow"
    },
    "question6": {
        "question": "What is the capital of China?",
        "answer": "Beijing"
    },
    "question7": {
        "question": "What is the capital of United Kingdom?",
        "answer": "London"
    },
    "question8": {
        "question": "What is the capital of Switzerland?",
        "answer": "Bern"
    },
    "question9": {
        "question": "What is the capital of Australia?",
        "answer": "Canberra"
    },
    "question10": {
        "question": "What is the capital of Germany?",
        "answer": "Berlin"
    }
}

score = 0

for key, value in quiz.items():
    print(value['question'])
    answer = input("Answer: ")

    if answer.lower() == value['answer'].lower():
        print("Correct Answer")
        score = score + 1
        print("Your Score is: " + str(score))
        print("")
    else:
        print("Wrong Answer!")
        print("The Answer is: " + value['answer'])
        print("Your Score is: " + str(score))
        print("")
        


print("You got " + str(score) + " out of 10 questions correctly.")
print("Your Percentage is: " + str(score / 10 * 100) + "%.")
