import sys

MORSE = {
    'A' : '.-', 'B' : '-...', 'C' : '-.-.', 'D' : '-..', 'E' : '.', 'F' : '..-.',
    'G' : '--.', 'H' : '....', 'I' : '..', 'J' : '.---', 'K' : '-.-', 'L' : '.-..',
    'M' : '--', 'N' : '-.', 'O' : '---', 'P' : '.--.', 'Q' : '--.-', 'R' : '.-.',
    'S' : '...', 'T' : '-', 'U' : '..-', 'V' : '...-', 'W' : '.--', 'X' : '-..-',
    'Y' : '-.--', 'Z' : '--..', '0' : '-----', '1' : '.----', '2' : '..---', '3' : '...--',
    '4' : '....-', '5' : '.....', '6' : '-....', '7' : '--...', '8' : '---..', '9' : '----.',
    ' ' : ' / '
}

text = ' '.join(sys.argv[1:])
text = text.upper()

morsecode = ''

for c in text:
    if c in MORSE:
        morsecode = morsecode + MORSE[c] + ' '
    else:
        print('ERROR')
        exit()

print(morsecode)