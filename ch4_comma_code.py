# Comma code practice project
# https://automatetheboringstuff.com/chapter4/
# Keian Barton 09/01/2018

def comma_func(list_val):
    
    sentence = ''
    for i in range(len(list_val)):
        if (i < len(list_val)-1):
            sentence += list_val[i] + ', '
        else:
            sentence += 'and ' + list_val[i]

    return sentence

def main():
    spam = ['apples', 'bananas', 'tofu', 'cats']
    print(comma_func(spam))

main()
