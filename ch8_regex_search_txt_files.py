#! python3
"""
Regex Search
This program opens all text files in a folder and searches for a
user supplied regex
Keian Barton 11/01/2018
"""

import logging, pprint, os, re, sys

logging.basicConfig(level=logging.DEBUG,
                    format=' %(asctime)s - %(levelname)s - %(message)s')
logging.disable(logging.CRITICAL)

def search_folders(regex, path):

    try:
        compiled_regex = re.compile(regex)
    except:
        logging.error('Error compiling user-entered regex')
        print('Invalid regex entered')
        return
    
    if not os.path.isdir(path):
        logging.info('User-entered invalid path: %s' % (path))
        print('Invalid path entered')
        return
        
    logging.info('Searching for text files')
    
    text_file_list = []
    for i in range(len(os.listdir(path))):
        file = os.path.join(path, os.listdir(path)[i])
        if not os.path.isfile(file):
            continue
        if file.endswith('.txt'):
            logging.info('Text file found')
            text_file_list.append(file)

    if len(text_file_list) == 0:
        print('No text files found in the given directory')
        return

    matches = {}
    for i in range(len(text_file_list)):
        try:
            file = open(text_file_list[i], 'r')
        except:
            logging.error('Error opening file')
            matches[os.path.basename(text_file_list[i])] = '?'
            continue
        file_matches = compiled_regex.findall(file.read())
        if file_matches:
            matches[os.path.basename(text_file_list[i])] = len(file_matches)
        else:
            matches[os.path.basename(text_file_list[i])] = 0

    print('Matches found:')
    pprint.pprint(matches)
    print()
    
def main():
    while True:
        print('Regex Search program')
        path = input('Please enter a path to search in (Q to quit):\n')
        if path.upper() == 'Q':
            sys.exit()
        regex = input('Please enter a regular expression:\n')
        print('\nSearching for matches...')
        search_folders(regex, path)

main()
