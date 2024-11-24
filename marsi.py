import random

locations = [random.randint(1, 7) for _ in range(3)]
weights = [400, 200, 113]

print("Hello! Try to guess the correct locations of boxes. You need to guess three numbers between 1 and 7.")

while True:
    guesses = [] 
    correct_guesses = 0
    
    for i in range(3):
        while True:
            guess = input(f"Enter the location of box {i + 1} (1-7 km): ")
            
            if 1 <= guess <= 7 and guess.isdigit():
                guesses.append(guess)
                break
            else:
                print("Sorry, your input is incorrect. Enter a number between 1 and 7")
    
        if guesses[-1] == locations[i]:
                correct_guesses += 1
        
    if guesses == locations:
        if sum(weights) == 713:
            print("Congratulations! You've found all the boxes.")
            print(f"Locations: {locations}, weights: {weights}")
            break
        else:
            print("Incorrect weight! Try again.")
        
    else:
        print(f"Sorry, your guesses were wrong! The boxes were moved. Correct guesses so far: {correct_guesses}")
        locations = [random.randint(1, 7) for _ in range(3)]
