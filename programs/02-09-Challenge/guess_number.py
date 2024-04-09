
# Imports
from random import randint, seed

# Fix seed
seed(42) # Correct number is 82

# Welcoming message to player
welcome_msg = '''Welcome to the guessing game! The rules are
    1. Guess a number between 1 and 100;
    2. On your first guess, if your guess is
        * within 10 of the number, I will print "WARM!"
        * further than 10 away from the number, I will print "COLD!"
    3. On all subsequent turns, if a guess is 
        * closer to the number than the previous guess return "WARMER!"
        * farther from the number than the previous guess, return "COLDER!"
    4. When your guess equals the number, I will print that you have guessed correctly *and* how many guesses it took!
'''


# Ask for player to input number
ask_for_guess_msg = "What is your guess?"

# Error message invalid input
error_msg = "Invalid input. Please enter an integer between 1 and 100"

# Pick a random integer from 1 to 100 (inclusive)
number_to_guess = randint(1, 100)  # inclusive on both end points

# Create a list to store past guesses
guesses = [0]

# Game logic
while True:

    try:
        user_input = int(input(ask_for_guess_msg))

        if user_input < 1 or user_input > 100:
            print(error_msg)
            continue

        if number_to_guess == user_input:
            print(
                f"The number {number_to_guess} is correct! You took {len(guesses)} guesses.")
            break

        guesses.append(user_input)

        if guesses[-2]:
            if abs(number_to_guess - user_input) < abs(number_to_guess - guesses[-2]):
                print('WARMER!')
            else:
                print('COLDER!')
        else:
            if abs(number_to_guess - user_input) <= 10:
                print('WARM!')
            else:
                print('COLD!')

    except ValueError:
        print(error_msg)
