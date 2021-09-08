y = int(input("Enter a number: "))

def prime_check(number):
    number_range = range(1, number//2+1)
    divisors = [x for x in number_range if number % x == 0]
    divisors.append(number)
    print(divisors)
    if len(divisors) == 2:
        print("Number is prime.")
    else:
        print("Number is not prime.")

prime_check(y)

