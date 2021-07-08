#Variables that are created outside of a function (as in all of the previous examples)
#are known as global variables.

#Global variables can be used by everyone, both inside of functions and outside

x = "awesome"

def myfunc():
    print("Python is "+ x)

myfunc()

#To create a global variable inside a function, you can use "global" keyword
def myfun():
    global y
    y = "fantastic"

myfun()

print("Python is "+y)

#You can change a global variable inside a function
def myfunct():
    global x
    x = "useful"

myfunct()

print("Python is "+ x)