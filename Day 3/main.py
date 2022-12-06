from string import ascii_letters
import numpy as np

with open ('input.txt') as f:
    rucksacks = f.read().splitlines()

# First star
score = 0

for rucksack in rucksacks:
    for idx, item in enumerate(rucksack[0:int(len(rucksack)/2)]):
        if item in rucksack[int(len(rucksack)/2)::]:
            if item.isupper():
                score += ord(item) - ord('A') + 27
            else:
                score += ord(item) - ord('a') + 1
            break
print(score)

# Second star
score = 0

for index in np.arange(0,len(rucksacks), 3):
    for idx, item in enumerate(rucksacks[index]):
        if item in rucksacks[index + 1] and item in rucksacks[index + 2]:
            if item.isupper():
                score += ord(item) - ord('A') + 27
            else:
                score += ord(item) - ord('a') + 1
            print(score, item, index)
            break
        
print(score)