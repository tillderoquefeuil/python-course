import sys

if len(sys.argv) != 3 or not sys.argv[1].isnumeric() or not sys.argv[2].isnumeric():
    if len(sys.argv) > 3:
        print("Input Error: too many arguments")
    elif len(sys.argv) == 3 and (not sys.argv[1].isnumeric() or not sys.argv[2].isnumeric()):
        print("Input Error: only numbers")
    print("Usage: python 05_operations.py <number1> <number2>\nExample:\n\tpython 05_operations.py 10 3")
    exit()

nb1 = int(sys.argv[1])
nb2 = int(sys.argv[2])

print("Sum:\t\t" + str(nb1 + nb2))
print("Difference:\t" + str(nb1 - nb2))
print("Product:\t" + str(nb1 * nb2))
if nb2 == 0:
    print("Quotient:\tERROR (div by zero)")
    print("Remainder:\tERROR (modulo by zero)")
else:
    print("Quotient:\t" + str(nb1 / nb2))
    print("Remainder:\t" + str(nb1 % nb2))