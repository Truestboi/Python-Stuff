from random import *

aRandomNumber = randint(1, 20)
#print("This is randomgay: "= str(aRandomNumber))

guess = input("Guess a number between 1 and 20 (inclusive): ")
if not guess.isnumeric(): #checks if a string is only digits 0 to 9
    print("That's not a positive whole number, try again!")
else:
    guess = int(guess) #converts a string to an integer

while (guess != aRandomNumber):
    if (guess < aRandomNumber):
        print("Guess Higher: ")
    elif(guess > aRandomNumber):
        print("Guess Lower:")
    else:
        print("lol idk")
guess = input("Guess a number between 1 and 20 (inclusive): ")
if not guess.isnumeric(): #checks if a string is only digits 0 to 9
    print("That's not a positive whole number, try again!")
else:
    guess = int(guess) #converts a string to an integer
