# 1. Count the number of upper and lower case letters in a String

string = input("1. Enter a string: ")

upper = 0
lower = 0

for ch in string:
    if ch.isupper():
        upper += 1
    elif ch.islower():
        lower += 1

print("Uppercase letters:", upper)
print("Lowercase letters:", lower)


# 2. Check whether a given String is Palindrome or not

string = input("\n2. Enter a string: ")

if string == string[::-1]:
    print("Palindrome")
else:
    print("Not a Palindrome")


# 3. Return a new string made of n copies of the first 2 characters

string = input("\n3. Enter a string: ")

result = string[:2] * len(string)

print(result)


# 4. Remove 'x' if it is the first or last character

string = input("\n4. Enter a string: ")

if string.startswith("x"):
    string = string[1:]

if string.endswith("x"):
    string = string[:-1]

print(string)


# 5. Return a string made of n repetitions of the last n characters

string = input("\n5. Enter a string: ")
n = int(input("Enter n: "))

result = string[-n:] * n

print(result)