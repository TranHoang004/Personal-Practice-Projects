
import random


X = random.randint(1, 100)

def guess_random_num(X):
    Y = int(input("Enter a number between 1 and 100: "))
    while Y != X:
        if Y < X:
            print("Too low!")
        elif Y > X:
            print("Too high!")
        Y = int(input("Enter a number between 1 and 100: "))
    print("Congratulations! You guessed it!")

def computer_guess():
    low = 1
    high = 100
    print("Think of a number between 1 and 100. I will try to guess it!")
    input("Press Enter when you're ready...")

    while low <= high:
        guess = (low + high) // 2
        print(f"My guess is: {guess}")
        feedback = input("Is it (H)igh, (L)ow, or (C)orrect? ").strip().lower()
        if feedback == 'c':
            print("Yay! I guessed your number!")
            break
        elif feedback == 'l':
            low = guess + 1
        elif feedback == 'h':
            high = guess - 1
        else:
            print("Please enter H, L, or C.")

computer_guess()

