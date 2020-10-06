import sys

# Get arguments
text = ' '.join(sys.argv[1:])

# Reverse letters
text = text[::-1]

# Swap case
text = text.swapcase()

# Print text
print(text)
