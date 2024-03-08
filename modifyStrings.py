# built-in methods that we can   use on strings

a = "AyEza"
print(a.upper())  # convert to uppercase
print(a.lower())  # convert to lowercase

b = " Hi, blah "
print(b.strip())  # remove whitespaces from beginning and end

c = "Cotton candy"
print(c.replace('o','u'))  # replaces all 'o' with 'u'

# SPLIT() method splits the string into substrings,
# if it finds instance of seprator
intro = 'hi, i am ayezza'
print(intro.split(','))