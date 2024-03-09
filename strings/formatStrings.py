# we cannot combine strings and numbers like we do in JS
# just adding {"hi my age is" + age}. NO!
# We use format() method to combine strings and numbers

# The format() method takes the passed arguments,
# formats them, and places them in the string
# where the placeholders {} are:

age = 23
txt = 'Hi I am {} years old '
print(txt.format(age))

# the format method takes unlimited number of arguments
# and are placed into respective placeholders
quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))
