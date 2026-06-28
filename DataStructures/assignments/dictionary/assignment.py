# 1. Add a key and value to a dictionary

d = {0: 10, 1: 20}
d[2] = 30
print("1.", d)


# 2. Concatenate the following dictionaries to create a new one

dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}

dic = {}
dic.update(dic1)
dic.update(dic2)
dic.update(dic3)

print("2.", dic)


# 3. Check if a given key already exists in a dictionary

d = {1: "Apple", 2: "Banana", 3: "Mango"}

key = int(input("3. Enter the key: "))

if key in d:
    print("Key exists")
else:
    print("Key does not exist")


# 4. Iterate over a dictionary using for loop and print the keys alone,
#    values alone and both keys and values

d = {1: "Apple", 2: "Banana", 3: "Mango"}

print("\n4. Keys:")
for key in d:
    print(key)

print("Values:")
for value in d.values():
    print(value)

print("Keys and Values:")
for key, value in d.items():
    print(key, value)


# 5. Prepare a dictionary where the keys are numbers between 1 and 15
#    and the values are the square of the keys

d = {}

for i in range(1, 16):
    d[i] = i * i

print("\n5.", d)


# 6. Sum all the values in a dictionary

d = {1: 10, 2: 20, 3: 30, 4: 40}

total = sum(d.values())

print("\n6. Sum =", total)