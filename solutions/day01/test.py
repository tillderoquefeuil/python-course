import string
import sys

# Python 3 program to count the uppercase,
# lowercase, punctuation characters
# and spaces 

# Function to count uppercase, lowercase,
# punctuation characters and numbers
def Count(str): 
    Upper, Lower, Punctuation, Spaces = 0, 0, 0, 0
    for i in range(len(str)): 
        if str[i].isupper(): 
            Upper += 1
        elif str[i].islower(): 
            Lower += 1
        elif str[i].ispunctuation(): 
            Punctuation += 1
        elif str[i].isspace():
            Spaces +=1
    print(Upper, 'Upper case letters:') 
    print(Lower, 'Lower case letters:') 
    print(Number, 'Punctuation marks:') 
    print(Spaces, 'Spaces:') 

# Driver Code 
str =sys.argv[1]
Count(str)