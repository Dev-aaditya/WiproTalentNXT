# 1. Accept two numbers as command line arguments and display their sum

import sys

num1 = int(sys.argv[1])
num2 = int(sys.argv[2])

print("Sum =", num1 + num2)


# 2. Accept a welcome message through command line arguments and display
#    the file name along with the welcome message

import sys

print("File Name:", sys.argv[0])
print("Welcome Message:", " ".join(sys.argv[1:]))


# 3. Accept 10 numbers through command line arguments and calculate
#    the sum of prime numbers among them

import sys

def is_prime(n):
    if n <= 1:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True

numbers = list(map(int, sys.argv[1:]))

prime_sum = 0

for num in numbers:
    if is_prime(num):
        prime_sum += num

print("Sum of prime numbers =", prime_sum)