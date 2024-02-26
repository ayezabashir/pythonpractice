# You can get the data type of any object by using the type() function:
a = 5  # int
b = "hello world"  # string
c = 20.5  # float
d = 1j  # complex
e = ["apple", "banana", "cherry"]  # list
f = ("apple", "banana", "cherry")  # tuple
g = range(6)
h = {"name": "Ayeza", "degree": "MPhill"}  # dict (dictionary)
i = frozenset({"apple", "banana", "cherry"})  # frozenset
j = True  # boolean
k = b"Hello"  # bytes
l = bytearray(5)  # bytearray
m = memoryview(bytes(5))  # memoryview
n = None  # Nonetype

print(type(n))

# Casting
x = int(1)    # x will be 1
y = int(2.8)  # y will be 2
z = int("3")  # z will be 3
print(x, y, z)

x = float(1)     # x will be 1.0
y = float(2.8)   # y will be 2.8
z = float("3")   # z will be 3.0
print(x, y, z)

x = str("s1")  # x will be 's1'
y = str(2)    # y will be '2'
z = str(3.0)  # z will be '3.0'
print(x, y, z)
