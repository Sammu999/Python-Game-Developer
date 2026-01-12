file = open("numbers.txt", "r")

total = 0

for line in file:
    total = total + int(line)

file.close()

print(total)





