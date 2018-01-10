#! python3
"""
ch7_regex_phone_number_extractor

Program that searches the text in the clipboard for phone numbers and email addresses,
and replaces them with just the phone numbers and e-mail addresses

Keian Barton 10/01/2018
"""

import pyperclip, re, sys

# American phone numbers
phone_regex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?                # area code
    (\s|-|\.)?                        # separator
    (\d{3})                           # first 3 digits
    (\s|-|\.)                         # separator
    (\d{4})                           # last 4 digits
    (\s*(ext|x|ext.)\s*(\d{2,5}))?    # extension
    )''', re.VERBOSE)

# Won't match all e-mail addresses but will match typical ones
email_regex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+      # username
    @                      # @ symbol
    [a-zA-Z0-9.-]+         # domain name
    (\.[a-zA-Z]{2,4})      # dot-something
    (\.[a-zA-Z]{2,4})?     # potentially .co.uk
    )''', re.VERBOSE)

# Find matches in clipboard text.
text_in_clipboard = pyperclip.paste()
matches = []

for groups in phone_regex.findall(text_in_clipboard):
    phoneNum = '-'.join([groups[1], groups[3], groups[5]])
    if groups[8] != '':
        phoneNum += ' x' + groups[8]
        matches.append(phoneNum)
for groups in email_regex.findall(text_in_clipboard):
    matches.append(groups[0])

# Copy results to the clipboard.
if len(matches) > 0:
    matched_data = '\n'.join(matches)
    pyperclip.copy(matched_data)
    print('Copied to clipboard:')
    print(matched_data)
else:
    print('No phone numbers or email addresses found.')

sys.exit()
