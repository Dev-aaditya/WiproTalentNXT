# 1. Remove a given item from the set

s = {10, 20, 30, 40, 50}

item = int(input("1. Enter the item to remove: "))

s.remove(item)

print(s)


# 2. Create an intersection of sets

set1 = {10, 20, 30, 40}
set2 = {30, 40, 50, 60}

print("\n2.", set1.intersection(set2))


# 3. Create a union of sets

set1 = {10, 20, 30, 40}
set2 = {30, 40, 50, 60}

print("\n3.", set1.union(set2))


# 4. Find the maximum and minimum value in a set

s = {15, 40, 5, 80, 25}

print("\n4. Maximum:", max(s))
print("Minimum:", min(s))