import random

x = random.randint(1,9)

i = 0

while True:
    user = input("Enter a guess between 1 and 9: ")
    
    if user == "exit":
        break
   
    try:
        y = int(user)
    except:
        print("Guess is not an integer. Please input another guess.")
        continue

    if y > 9:
        print("Guess is greater than 9. Please input another guess.")
        continue
    if y < 1:
        print("Guess is less than 1. Please input another guess.")
        continue
    
    i += 1
    if y > x:
            print("Guess is greater than number. Guess again.")
    elif y < x:
            print("Guess is less than number. Guess again.")
    elif y == x:
            correct_message = "The number was {}. You've guessed correctly! It took you {} times."
            print(correct_message.format(str(y),str(i)))
            break
    else:
        print("Something went wrong.")