import random

locations = [random.randint(1, 7) for _ in range(3)]
weights = [400, 200, 113]

print("Hello! Try to guess the correct locations of boxes. You need to guess three numbers between 1 and 7.")

while True:
    guesses = [] 
    for i in range(3):
        guess = int(input(f"Enter the location of box {i + 1} (1-7 km): "))
        guesses.append(guess)
        
    if guesses == locations:
        if sum(weights) == 713:
            print("Congratulations! You've found all the boxes.")
            print(f"Locations: {locations}, weights: {weights}")
            break
        else:
            print("Incorrect weight! Try again.")
        
    else:
        print("Sorry, your guesses were wrong! The boxes were moved.")
        locations = [random.randint(1, 7) for _ in range(3)]
