scores = list(map(int, input("Enter scores separated by space: ").split()))

scores = list(set(scores))
scores.sort()

print("Runner-up score:", scores[-2])