def prime_check(number):
    number_range = range(1, number//2+1)
    divisors = [x for x in number_range if number % x == 0]
    divisors.append(number)
    if len(divisors) == 2:
        print("Number is prime.")
    else:
        print("Number is not prime.")

y = int(input("Enter a number: "))

prime_check(y)

