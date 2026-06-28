# Secret message from text file

file = open("message.txt", "r")

lines = file.readlines()

line_count = len(lines)

if line_count <= 12:
    time = str(line_count) + " AM"
else:
    time = str(line_count - 12) + " PM"

words = {}

for line in lines:
    for word in line.split():
        word = word.strip(".,!?")
        if word in words:
            words[word] += 1
        else:
            words[word] = 1

place = max(words, key=words.get)

print("Meeting Time:", time)
print("Meeting Place:", place + " Street")

file.close()