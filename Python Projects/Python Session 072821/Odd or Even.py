num = int(input("Please enter a number: "))
den = int(input("Please enter a number to divide it by: "))


if num % den == 0:
    print(f"{num} is divisible by {den}")
else: 
    print(f"{num} is not divisible by {den}")

