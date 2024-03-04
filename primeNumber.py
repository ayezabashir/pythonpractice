#  check divisibility of the number by all numbers from 2 up to
#  the square root of the number. If the number is divisible
#  by any of these numbers, it's not prime.
num = int(input('Enter a number: '))
if num == 1:
    print("Number is prime")
elif num == 2:
    print("Number is prime")
else:
    is_prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print("Num is prime")
    else:
        print("Num is not prime")
