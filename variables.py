#  In python, variables are created when you assign
#  a value to it
x = 5
y = "Hello, World!"
print(x)
print(y)

# If you want to specify the data type of a variable,
# this can be done with CASTING.
a = str(3)   # 3 will be treated as a string
b = int(3)   # 3 will be treated as an integer
c = float(3)  # 3 will be treated as a floating point i.e 3.0

# we can get the type of variable using type()
print(type(a))
print(type(b))
print(type(c))

# String variables can be declared either by
# using single or double quotes:
name = 'ayeza'   # this way
name1 = "ayeza"  # or this way

# Variable names are case-sensitive.
email = "ayezabashir46@gmail.com"
Email = "aqsabashir46@gmail.com"
print(email)
print(Email)

# Python allows you to assign values to multiple
# variables in one line
x, y, z = 2, 'hello', 3.4
print(x)
print(y)
print(z)

# One Value to Multiple Variables
p = q = r = "Oranges"
print(p)
print(r)
print(q)

# Unpack a Collection
my_list = ['pink', 'purple', 'green']
l, m , n = my_list
print(l)
print(m)
print(n)