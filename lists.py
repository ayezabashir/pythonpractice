# Lists are one of 4 built-in data types
# in Python used to store collections of data,
# the other 3 are Tuple, Set, and Dictionary,

# lists are:
# 1-ordered
# 2-changeable
# 3-allow duplicate values.
fruits = ["apples", "oranges", "bananas", "oranges"]
list1 = [True, False, True]
list2= [1,3,5,7]
print(fruits)
print(len(fruits))
print(list2)
print(list1)
print(type(list2))

# List Constructor
listConstr = list(("apple", "banana", "orange"))  # double round brackets
print(listConstr)
print(type(listConstr))

# indexing
print(fruits[0])
# negative indexing means start from end
print(fruits[-1])

# Ranges
print(fruits[0:2])

# Range of negative indexing
names = ["ayeza", "aqsa", "ayesha", "mariam", "hafsa"]
print(names[-3:-1])

if 'aqsa' in names:
    print("Aqsa exists in list")

names[2]='bubbles'
print(names)
names[1:3]=['angry bird','ayesha']
print(names)

# REPLACING and adding more than 1 values
names[1:2]=["aqsa","angry"]
print(names)

# replacing 2 or more values with one
names[1:3]=["aqsa"]
print(names)