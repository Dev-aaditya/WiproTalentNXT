# Accept three strings through command line arguments and calculate happiness

import sys

like = sys.argv[1].split("-")
dislike = sys.argv[2].split("-")
numbers = sys.argv[3].split("-")

happiness = 0

for num in numbers:
    if num in like:
        happiness += 1
    elif num in dislike:
        happiness -= 1

print("Final Happiness =", happiness)