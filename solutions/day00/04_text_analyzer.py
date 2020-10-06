import sys
import string

def text_analyzer(txt):
    total = len(txt)
    upper = sum(1 for c in txt if c.isupper())
    lower = sum(1 for c in txt if c.islower())
    punct = sum(txt.count(c) for c in string.punctuation)
    space = txt.count(' ')

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