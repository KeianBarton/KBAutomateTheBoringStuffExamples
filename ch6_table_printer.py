#! python3
"""Write a function named print_table() that takes a list
of lists of strings and displays it in a well-organized
table with each column right-justified."""

table_data = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol'],
             ['dogs', 'cats', 'moose', 'goose']]

def print_table(table_data):

    longest_string_len = 0
    longest_inner_list_len = 0
    
    for i in range(len(table_data)):
        longest_inner_list_len = max(len(table_data[i]), longest_inner_list_len)
        for j in range(len(table_data[i])):
            longest_string_len = max(len(table_data[i][j]), longest_string_len)
    
    for i in range(longest_inner_list_len):
        for j in range(len(table_data)):
            try:
                print(table_data[j][i].rjust(longest_string_len + 1), end='')
            except IndexError:
                print(' '*(longest_string_len+1), end='')
        print()
        
print_table(table_data)
