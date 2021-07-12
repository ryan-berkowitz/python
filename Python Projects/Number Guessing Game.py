#Returns winning number

#Generate random number from 1-100
import random
x = random.randint(1,100)

#Input Guesses
guessList = []
i = 'Y'
while i != 'N':
    print("Guess a number between 1-100.")
    y = int(input())
    if y > 100:
        print("Guess is greater than 100. Please input another guess.")
    elif y < 1:
        print("Guess is less than 1. Please input another guess.")
    else:
        guessList.append(y)
    print("Are there any more guesses? ('Y/N')?")
    i = input()

#Sort function
def sortList(n):
    return abs(n - x)

#Decide Winner
if len(guessList) != 0:
    guessList.sort(key = sortList)
    winner = guessList[0]
    listMsg = "The guesses were:"
    print(listMsg)
    print(guessList)
    guessMsg = "The number to guess was {}."
    print(guessMsg.format(x))
    winningMsg = "The winning guess is {}."
    print(winningMsg.format(winner))
else:
    print("No guesses were inputed.")