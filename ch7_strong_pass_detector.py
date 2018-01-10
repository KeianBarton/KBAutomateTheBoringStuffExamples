#! python3
'''
Strong password detector
ch7_strong_pass_detector.py

Write a function that uses regular expressions to make sure the password
string it is passed is strong. A strong password is defined as one that
is at least eight characters long, contains both uppercase and lowercase
characters, and has at least one digit
Keian Barton 10/01/2018
'''

import re

def main():
    user_input =''
    while True:
        user_input = input("Please type the password you would like to " \
              "check is 'strong' (press Q to quit).\n")

        if user_input.upper() == 'Q':
            break
        
        is_strong = check_pass(user_input)
        if is_strong:
            print('The given password is strong.')
        else:
            print('The given password is not strong.')

def check_pass(password):
    lowercase_pass_regex = re.compile('''(
        ([a-z])+    # Contains at least one lowercase letter
        )''', re.VERBOSE)
    uppercase_pass_regex = re.compile('''(
        ([A-Z])+    # Contains at least one uppercase letter
        )''', re.VERBOSE)
    digit_pass_regex = re.compile('''(
        (\d)+    # Contains at least one digit
        )''', re.VERBOSE)

    if len(password) < 8:
        return False
    if not lowercase_pass_regex.search(password):
        return False
    if not uppercase_pass_regex.search(password):
        return False
    if not digit_pass_regex.search(password):
        return False
    
    return True

main()
    
