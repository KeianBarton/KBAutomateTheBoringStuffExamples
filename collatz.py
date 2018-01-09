# The Collatz sequence project
# https://automatetheboringstuff.com/chapter3/
# Keian Barton 09/01/2018

import sys

def main():
    user_input = ''
    while user_input.upper() != 'Q':
        user_input = input('Enter an integer to create a Collatz sequence (Q to quit)\n')
        collatz(user_input)

def collatz(number):
    try:
        number = int(number)
    except ValueError:
        print('Please enter a valid integer')
        return

    if (number == 1):
        print(number)
    elif (number%2 == 0):
        print(number)
        result = number//2
        return collatz(result)
    else:
        print(number)
        result = 3 * number + 1
        return collatz(result)

main()
