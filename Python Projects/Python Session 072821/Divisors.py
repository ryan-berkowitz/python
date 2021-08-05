number = int(input("Enter a number: "))
range = range(1, number//2+1)

divisors = [x for x in range if number % x == 0]
divisors.append(number)
print(divisors)
