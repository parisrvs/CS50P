import random
import sys


while True:
    try:
        n = int(input("Level: "))
    except ValueError:
        pass
    else:
        if n > 0:
            break

value = random.randint(1, n)

while True:
    try:
        guess = int(input("Your Guess: "))
    except ValueError:
        pass
    else:
        if guess <= 0:
            pass
        elif guess < value:
            print("Too small!")
        elif guess > value:
            print("Too large!")
        else:
            print("Just right!")
            sys.exit()