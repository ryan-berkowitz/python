#Returns winning number

#Prompt entry of number
print("Input number to guess")
x = int(input())

guessList = []
i = 'Y'
while i != 'N':
    print("Guess a number")
    y = int(input())
    guessList.append(y)
    print("Are there any more guesses? ('Y/N')?")
    i = input()

def sortList(n):
    return abs(n - x)

sortList = guessList.sort(key = sortList)

winner = sortList[0]
winningMsg = "The winner is {}"
print(winningMsg.format(winner))



#Prompt Guess