import sys

if len(sys.argv) != 2 or not sys.argv[1].isnumeric():
    print("ERROR")
    exit()

nb = int(sys.argv[1])
if nb == 0:
    print("I'm Zero.")
elif nb % 2 == 0:
    print("I'm Even.")
else:
    print("I'm Odd.")