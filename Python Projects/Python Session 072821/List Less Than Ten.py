a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
l = int(input("Enter a number to return the values less than: "))
x = [n for n in a if n < l]


#for n in a:
    #if n < 5:
        #x.append(n)

print(x)

