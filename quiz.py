# Quiz Game in Python

questions = {
    "What is the capital of India?": "A",
    "Which language is used for Data Analysis?": "C",
    "Who developed Python?": "B",
    "Which keyword is used to define a function?": "D",
    "Which data structure stores key-value pairs?": "C"
}

options = [
    ["A. New Delhi", "B. Mumbai", "C. Kolkata", "D. Chennai"],
    ["A. Java", "B. C++", "C. Python", "D. HTML"],
    ["A. James Gosling", "B. Guido van Rossum", "C. Dennis Ritchie", "D. Elon Musk"],
    ["A. function", "B. func", "C. define", "D. def"],
    ["A. List", "B. Tuple", "C. Dictionary", "D. Set"]
]

score = 0

print("=" * 40)
print("        PYTHON QUIZ GAME")
print("=" * 40)

name = input("Enter your name: ")

question_no = 0

for question in questions:

    print("\n" + question)

    for option in options[question_no]:
        print(option)

    answer = input("Enter your answer (A/B/C/D): ").upper()

    if answer == questions[question]:
        print("Correct Answer")
        score += 1
    else:
        print("Wrong Answer")
        print("Correct Answer is", questions[question])

    question_no += 1

print("\n" + "=" * 40)
print("Quiz Finished")
print("=" * 40)

print("Name :", name)
print("Correct Answers :", score)
print("Wrong Answers :", len(questions) - score)

percentage = (score / len(questions)) * 100

print("Percentage :", percentage, "%")

if percentage >= 80:
    print("Grade : A")
elif percentage >= 60:
    print("Grade : B")
elif percentage >= 40:
    print("Grade : C")
else:
    print("Grade : Fail")

choice = input("\nDo you want to save your score? (yes/no): ")

if choice.lower() == "yes":
    file = open("scores.txt", "a")
    file.write(name + " : " + str(score) + "/" + str(len(questions)) + "\n")
    file.close()
    print("Score Saved Successfully!")

print("\nThank You For Playing!")