#Default
# Text type: str
# Numeric type: int, float, complex
# Sequence type: list, tuple, range
# Mapping type: dict
# Set types: set, frozenset
# Boolean type: bool
# Binary type: bytes, bytearray, memoryview

#Get data type
x = 5
print(type(x))

#Default data types during assign
x = "Hello World"
print("x = 'Hello World'")
print(type(x))

x = 20
print("x = 20")
print(type(x))

x = 20.5
print("x = 20.5")
print(type(x))

x = 1j
print("x = 1j")
print(type(x))

x = ["apple", "banana", "cherry"]
print('x = ["apple", "banana", "cherry"]')
print(type(x))

x = ("apple", "banana", "cherry")
print('x = ("apple", "banana", "cherry")')
print(type(x))

x = range(6)
print("x = range(6)")
print(type(x))

x = {"name" : "John", "age" : 36}
print('x = {"name" : "John", "age" : 36}')
print(type(x))

x = {"apple", "banana", "cherry"}
print('x = {"apple", "banana", "cherry"}')
print(type(x))

x = frozenset({"apple", "banana", "cherry"})
print('x = frozenset({"apple", "banana", "cherry"})')
print(type(x))

x = True
print("x = True")
print(type(x))

x = b"Hello"
print('x = b"Hello"')
print(type(x))

x = bytearray(5)
print('x = bytearray(5)')
print(type(x))

x = memoryview(bytes(5))
print("x = memoryview(bytes(5))")
print(type(x))

#You can also set specific data types