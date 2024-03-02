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

### LISTS
fruits = ["apple", "banana", "cherry"]
print(fruits)
print(len(fruits))
print(fruits[1])

new_fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(new_fruits[2:5])
new_fruits[1] = "ayeza"
new_fruits[2:4] = ["melon", "post", "cake"]
print(new_fruits)

new_fruits.append("aaron")  # at the end of list
print(new_fruits)

new_fruits.insert(0, "kenji")  # insert at specified index
print(new_fruits)

cities = ["sargodha", "lahore", "sargodha"]
cities2 = ["karachi", "islamabad"]
cities.extend(cities2)  # you can add any iterable object (tuples, sets, dictionaries etc.).
print(cities2)
print(cities)

cities.remove("sargodha")  # removes the specified item
print(cities)

cities.pop(0)  # removes the specified index item, otherwise removes the last item
print(cities)

cities.sort()
print(cities)

cities.sort(reverse=True)
print(cities)

siblings = ["aqsa", "ayesha", "mariam", "aqsa"]
family = siblings.copy()
print(siblings)
print(family)

mariam = siblings.index("mariam")
print(mariam)

siblings.reverse()
print(siblings)

aqsa = siblings.count("aqsa")
print(aqsa)

### TUPLES
thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)
print(len(thistuple))

# Comma hai to tuple hai
thistuple = ("apple",)
print(type(thistuple))
#NOT a tuple
thisNottuple = ("apple")
print(type(thisNottuple))

### Sets
myset = {"apple", "banana", "cherry"}
print(myset)
print(type(myset))

# Duplicate values will be ignored:
thisset = {"apple", "banana", "cherry", "apple"}
print(thisset)

### DICTIONARIES
thisDictionary = {
    "name" : "ayeza",
    "job" : "frontend developer",
    "age" : 23
}
print(thisDictionary)
# duplicates are not allowed in dictionaries
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020  #  this will override 1964
}
print(thisdict)
print(len(thisdict))
# dictionary can contain ANY data type
thisIsdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}
print(thisIsdict)