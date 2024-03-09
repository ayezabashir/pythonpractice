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
name = 'Ayeza Bashir'
age = 23
degree = 'MPhill'
intro = "Hi my name is {}. I am {} years old and I am currently doing {}"
print(intro.format(name, age, degree))

# ESCAPE CHARACTERs
# we use escape characters when we want to insert a character
# that is illegal in strings e.g.
text = "Hello love, I am \"Aaron Warner\""
print(text)