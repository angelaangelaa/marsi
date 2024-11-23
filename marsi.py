import random

locations = [random.randint(1, 10) for _ in range(3)]
weights = [300, 250, 163]

print(".")

while True:
    guesses = [] 
    for i in range(3):
        guess = int(input())
        guesses.append(guess)
    if guesses == locations:
        print()
        break
    else:
        print()
