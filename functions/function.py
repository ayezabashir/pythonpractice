def greet():
    print("Greetings!")

greet()

# Parameters
def sum(a,b):
    print(a+b)

sum(10, 20)   # passing arguments

def fam(name):
    print("Mother: " + name)

fam("Bushra Parveen")


# Return value
def findSquare(num):
    square= num*num
    return square

print(findSquare(3))