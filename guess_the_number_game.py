# Guess the number game
import random

def main():
    secret_num = random.randint(1, 20)
    print('I am thinking of a number between 1 and 20.\nYou have 6 guesses to get it right.')

    # Ask the player to guess 6 times.
    number_of_guesses = 0
    while number_of_guesses < 6:
        print('Take a guess.')

        try:
            guess = int(input())
        except ValueError:
            print('Please enter a valid number.')
            continue

        number_of_guesses += 1
        if guess < secret_num:
            print('Your guess is too low.')
        elif guess > secret_num:
            print('Your guess is too high.')
        else:
            break    # This condition is the correct guess!

    if guess == secret_num:
        print('Good job! You guessed my number in ' + str(number_of_guesses) + ' guesses!')
    else:
        print('Nope. The number I was thinking of was ' + str(secret_num) + '.')

main()
