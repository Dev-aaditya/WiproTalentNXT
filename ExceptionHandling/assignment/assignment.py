# 1. Read the entire content from a txt file and display it

file = open("sample.txt", "r")

content = file.read()

print(content)

file.close()


# 2. Read first n lines from a txt file

file = open("sample.txt", "r")

n = int(input("\n2. Enter the number of lines: "))

for i in range(n):
    print(file.readline(), end="")

file.close()


# 3. Accept input from user and append it to a txt file

file = open("sample.txt", "a")

text = input("\n\n3. Enter text to append: ")

file.write(text + "\n")

file.close()

print("Text appended successfully.")


# 4. Read contents from a txt file line by line and store each line into a list

file = open("sample.txt", "r")

lines = file.readlines()

print("\n4.", lines)

file.close()


# 5. Find the longest word from the txt file contents

file = open("sample.txt", "r")

words = file.read().split()

longest = max(words, key=len)

print("\n5. Longest word:", longest)

file.close()


# 6. Count the frequency of a user entered word in a txt file

file = open("sample.txt", "r")

content = file.read()

word = input("\n6. Enter the word to search: ")

count = content.split().count(word)

print("Frequency:", count)

file.close()