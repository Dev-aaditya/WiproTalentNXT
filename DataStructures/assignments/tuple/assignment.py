# 1. Print the 4th element from first and 4th element from last in a tuple

t = (10, 20, 30, 40, 50, 60, 70, 80)

print("4th element from first:", t[3])
print("4th element from last:", t[-4])


# 2. Check whether an element exists in a tuple or not

t = (10, 20, 30, 40, 50)

element = int(input("\n2. Enter the element: "))

if element in t:
    print("Element exists")
else:
    print("Element does not exist")


# 3. Convert a list into a tuple

lst = [10, 20, 30, 40, 50]

t = tuple(lst)

print("\n3.", t)


# 4. Find the index of an item in a tuple

t = (10, 20, 30, 40, 50)

element = int(input("\n4. Enter the element to find index: "))

print("Index:", t.index(element))


# 5. Replace last value of tuples in a list to 100

lst = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]

result = []

for i in lst:
    result.append(i[:-1] + (100,))

print("\n5.", result)