def fibonnaci(x):
    fib_num = [1]
    i = 1
    if x == 1:
        return fib_num
    else:
        while i < x:
            if len(fib_num) == 1:
                y = fib_num[-1]
                fib_num.append(y)
            else:
                y = fib_num[-1] + fib_num[-2]
                fib_num.append(y)
            i += 1
        return fib_num

z = int(input("Enter a number: "))

print(fibonnaci(z))