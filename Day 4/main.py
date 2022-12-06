import numpy as np

with open ('input.txt') as f:
    lines = f.read().splitlines()

# First star
pairs = np.empty([len(lines), 2, 2])
for idx, line in enumerate(lines):
    pair = line.split(',')
    for i, elf in enumerate(pair):
        elf_nrs = elf.split('-')
        pairs[idx, i, 0] = int(elf_nrs[0])
        pairs[idx, i, 1] = int(elf_nrs[1])

nr_of_fully_contain = 0

for pair in pairs:
    ass_pair_1 = pair[0]
    ass_pair_2 = pair[1]
    if ass_pair_1[0] <= ass_pair_2[0] and ass_pair_1[1] >= ass_pair_2[1]:
        nr_of_fully_contain += 1
    elif ass_pair_1[0] >= ass_pair_2[0] and ass_pair_1[1] <= ass_pair_2[1]:
        nr_of_fully_contain += 1

print(nr_of_fully_contain)

# Second star

nr_of_overlaping = 0

for pair in pairs:
    ass_pair_1 = pair[0]
    ass_pair_2 = pair[1]
    if ass_pair_1[0] >= ass_pair_2[0] and ass_pair_1[0] <= ass_pair_2[1]:
        nr_of_overlaping += 1
    elif ass_pair_2[0] >= ass_pair_1[0] and ass_pair_2[0] <= ass_pair_1[1]:
        nr_of_overlaping += 1

print(nr_of_overlaping)
