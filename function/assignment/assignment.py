# 1. Function to return the sum of all numbers in a list

def sum_list(lst):
    return sum(lst)

numbers = [8, 2, 3, 0, 7]
print("1.", sum_list(numbers))


# 2. Function to return the reverse of a string

def reverse_string(s):
    return s[::-1]

string = "1234abcd"
print("2.", reverse_string(string))


# 3. Function to calculate and return the factorial of a number

def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact

num = int(input("\n3. Enter a number: "))
print("Factorial:", factorial(num))


# 4. Function that accepts a string and prints the number of uppercase
#    and lowercase letters

def count_case(s):
    upper = 0
    lower = 0

    for ch in s:
        if ch.isupper():
            upper += 1
        elif ch.islower():
            lower += 1

    print("Uppercase letters:", upper)
    print("Lowercase letters:", lower)

string = input("\n4. Enter a string: ")
count_case(string)


# 5. Function to print the even numbers from a given list

def even_numbers(lst):
    even = []
    for i in lst:
        if i % 2 == 0:
            even.append(i)
    return even

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print("\n5.", even_numbers(numbers))


# 6. Function that checks whether a number is prime or not

def is_prime(n):
    if n <= 1:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True

num = int(input("\n6. Enter a number: "))

if is_prime(num):
    print("Prime")
else:
    print("Not Prime")