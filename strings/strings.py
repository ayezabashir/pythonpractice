#  strings are surrounded by either single qoutation
#  or double quotation
print("Hello")
print('Hello')

# Multiline Strings
# we do that by using three single/double quotation marks

# NOTE : line breaks are inserted at the same position as in the code.
intro = """This is a random parapgraoh
for me to understand what is multiline string 
and we do that inside  three quotation marks"""
print(intro)

# STRINGS ARE ARRAYS
# strings in Python are arrays of bytes representing
# unicode characters.
# Python does not have a character data type, a single character
# is simply a string with a length of 1.

a = 'Hello World'
print(a[2])

# LOOP
# since strings are arrays, we can loop through it
for x in a:
    print(x)

# Printing length
print(len(a))

# Check String
txt = "The best things in life are free!"
print("free" in txt)
print("expensive" not in txt)
# or
if "free" in txt:
    print("Yes there is 'free' in text")

# SLICING strings
meet = "Greetings, Welcome Back"
print(meet[2:3])   # starting index, and ending index (not including the end index)
print(meet[:5])    # slice from start
print(meet[10:])   # slice to end

# NEGATIVE SLICING
# Use negative indexes to start the slice from the end of the string
b = "Hello, World"
print(b[-5:-2])

# CONCATENATION
p = 'parcel'
d = 'deliver'
q = p+" "+d
print(q)