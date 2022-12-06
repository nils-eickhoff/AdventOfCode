import numpy as np
from copy import deepcopy

with open('input.txt') as f:
    lines = f.read().splitlines()

for idx, line in enumerate(lines):
    if line == '':
        stop = idx

starting_stacks = lines[0:stop-1]
rearr_proc = lines[stop + 1::]

def getStacks(starting_stacks):
    nr_of_stacks = int( (len(starting_stacks[0]) + 1) / 4 )
    stacks = np.empty(nr_of_stacks, dtype=object)
    for i in range(stacks.shape[0]):
        stacks[i] = []
    for crates in starting_stacks:
        for stack in range(nr_of_stacks):
            if crates[1 + stack*4] != ' ':
                stacks[stack].append(crates[1 + stack*4])
    return stacks
                
s = getStacks(starting_stacks)

arr = np.empty((len(rearr_proc), 3))
for i, line in enumerate(rearr_proc):
    line = line.replace("move ", "")
    line = line.replace(" from ", ",")
    line = line.replace(" to ", ",")
    splitted_line = line.split(',')
    for j in range(3):
        arr[i,j] = int(splitted_line[j])

# First star

def reArrange(new_arr, stacks): # Makes the crane moves
    new_stacks = deepcopy(stacks)
    for instruction in new_arr:
        for _ in range(int(instruction[0])):
            object = new_stacks[int(instruction[1] -1)].pop(0)
            new_stacks[int(instruction[2]) - 1].insert(0, object)
    return new_stacks

new_s = reArrange(arr, s)

# Tack out the last elements
def printLastRow(new_s):
    temp_string = ""
    for stack in new_s:
        temp_string = temp_string + stack[0][0]
    print(temp_string)

printLastRow(new_s)

# Second star

def reArrange2(new_arr, stacks): # Makes the crane moves
    new_stacks = deepcopy(stacks)
    for instruction in new_arr:
        object = []
        for _ in range(int(instruction[0])):
            o = new_stacks[int(instruction[1] -1)].pop(0)
            object.append(o)
        for o in object[::-1]:
            new_stacks[int(instruction[2]) - 1].insert(0, o)
    return new_stacks

new_s = reArrange2(arr, s)
printLastRow(new_s)