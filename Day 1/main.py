import numpy as np

with open('input.txt') as f:
    lines = f.read().splitlines()

elfes = np.array([0])
sum = 0

for value in lines:
    if value:
        sum += int(value)
    else:
        elfes = np.append(elfes, sum)
        sum = 0

elfes = np.append(elfes, sum)

# First question
print(max(elfes[1::]))

# Second question
elfes.sort()
print(np.sum(elfes[::-1][0:3]))

