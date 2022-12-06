import numpy as np

with open('input.txt') as f:
    lines = f.read().splitlines()

score = 0

# First star
for round in lines:
    if ( round == 'A X'):
        score += 1 + 3
    elif ( round == 'A Y') :
        score += 2 + 6
    elif ( round == 'A Z') :
        score += 3 + 0
    elif ( round == 'B X'):
        score += 1 + 0
    elif ( round == 'B Y') :
        score += 2 + 3
    elif ( round == 'B Z') :
        score += 3 + 6
    elif ( round == 'C X'):
        score += 1 + 6
    elif ( round == 'C Y') :
        score += 2 + 0
    else : # ( round == 'CZ') 
        score += 3 + 3

print(score)

# Second star
score = 0
for round in lines:
    if ( round == 'A X'):
        score += 3 + 0
    elif ( round == 'A Y') :
        score += 1 + 3
    elif ( round == 'A Z') :
        score += 2 + 6
    elif ( round == 'B X'):
        score += 1 + 0
    elif ( round == 'B Y') :
        score += 2 + 3
    elif ( round == 'B Z') :
        score += 3 + 6
    elif ( round == 'C X'):
        score += 2 + 0
    elif ( round == 'C Y') :
        score += 3 + 3
    else : # ( round == 'C Z') 
        score += 1 + 6

print(score)
        