import random

nbr = random.randint(1, 99)
guess = -1
attempt = 0

print("This is an interactive guessing game!")
print("You have to enter a number between 1 and 99 to find out the secret number. Type 'exit' to end the game.")
print("Good luck!\n")

while guess != nbr:
    guess = input("What's your guess between 1 and 99?\n>> ")
    if guess.isnumeric():
        attempt = attempt + 1
        guess = int(guess)

        if guess < nbr:
            print("Too low!")
        if guess > nbr:
            print("Too high!")
        if guess == nbr:
            if nbr == 42:
                print("The answer to the ultimate question of life, the universe and everything is 42.")
            if attempt == 1:
                print("Congratulations, you got it on your first try!")
            else:
                print("Congratulations, you've got it!\nYou won in {} attempts!".format(attempt))
    elif guess == 'exit':
        print("Goodbye!")
        exit()
    else:
        print("That's not a number")