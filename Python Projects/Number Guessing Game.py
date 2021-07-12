#Returns winning number

#Prompt entry of number
print("Input number to guess")
x = int(input())

#Input Guesses
guessList = []
i = 'Y'
while i != 'N':
    print("Guess a number")
    y = int(input())
    guessList.append(y)
    print("Are there any more guesses? ('Y/N')?")
    i = input()

#Sort function
def sortList(n):
    return abs(n - x)

#Decide Winner
guessList.sort(key = sortList)
winner = guessList[0]
winningMsg = "The winner is {}"
print(winningMsg.format(winner))