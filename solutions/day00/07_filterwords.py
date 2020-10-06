import sys

if len(sys.argv) != 3 or not sys.argv[2].isnumeric():
    print("ERROR")
    exit()

txt = sys.argv[1].split(" ")
min = int(sys.argv[2])

filtred = [word for word in txt if len(word) > min]
print(filtred)