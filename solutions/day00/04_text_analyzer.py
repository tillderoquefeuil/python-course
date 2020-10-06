import sys
import string

def text_analyzer(txt):
    total = len(txt)
    upper, lower, punct, space = 0, 0, 0, 0

    for i in txt: 
        if i.isupper(): 
            upper += 1
        elif i.islower(): 
            lower += 1
        elif i in string.punctuation: 
            punct += 1
        elif i.isspace():
            space += 1

    print("The text contains " + str(total) + " characters:\n")
    print("- " + str(upper) + " upper letters\n")
    print("- " + str(lower) + " lower letters\n")
    print("- " + str(punct) + " punctuation marks\n")
    print("- " + str(space) + " spaces")

if len(sys.argv) > 1:
    text = ' '.join(sys.argv[1:])
else:
    text = input("Text please!\n")

text_analyzer(text)