import random

print("====== NUMBER GUESSING GAME ======")

number = random.randint(1, 100)

while True:

    guess = int(input("Guess a number between 1 and 100: "))

    if guess > number:
        print("Too High!")

    elif guess < number:
        print("Too Low!")

    else:
        print("Congratulations! You guessed the correct number.")
        break