import numpy as np
from collections import defaultdict
#from pprint import pprint

with open('Day 7/input.txt') as f:
    lines = f.read().splitlines()
    
treshold = 100000

def countDirs(terminalLines):
    level = 0
    all_dirs = ["/"]
    raw_filesize_of_dir = defaultdict(int)
    raw_filesize_of_dir[0] += 0
    layer_dict = defaultdict(int)
    current_dir = '/'
    #raw_filesize_of_dir = 0
    layer_dict[current_dir] = 0
    for i, line in enumerate(terminalLines):
        if line == '$ ls':
            continue
        #    raw_filesize_of_dir = defaultdict(int)
        if line == '$ cd ..':
            r = current_dir[0:-2].rfind('/')
            raw_filesize_of_dir = layer_dict[current_dir]
            current_dir = current_dir[0:r+1]
            layer_dict[current_dir] += raw_filesize_of_dir
            level -= 1
        elif line[0:4] == '$ cd':
            #parent_dir_of = {}
            #layer_dict[current_dir] = raw_filesize_of_dir[0]
            current_dir = current_dir + line[5::] + '/'
            raw_filesize_of_dir = 0
            #layer_dict[current_dir] = raw_filesize_of_dir
            #for layer in range(level):
            #    layer_dict[current_dir] = parent_dir_of
            level += 1
        else : # in ls ...
            gap = line.find(' ')
            if line[0:gap] != 'dir':
                layer_dict[current_dir] += int(line[0:gap])
            #else:
            #    parent_dir_of[line[gap+1::]] = {}
    while level > 0:
        r = current_dir[0:-2].rfind('/')
        raw_filesize_of_dir = layer_dict[current_dir]
        current_dir = current_dir[0:r+1]
        layer_dict[current_dir] += raw_filesize_of_dir
        level -= 1
    return layer_dict

dir_dict = countDirs(lines)
tot_sum = 0
for dir in dir_dict.values():
    if dir < treshold:
        tot_sum += dir
print('The sum of these directories are: %d \n' % tot_sum)

# Second star
disc_memory = 70000000
free_memory = 30000000
used_memory = dir_dict['/']

memory_left = disc_memory - used_memory
smallest_dir_size_to_free = free_memory - memory_left

i = 0
for dir_name, dir_size in dir_dict.items():
    if i == 0:
        current_best_dir_size = dir_size
        current_best_dir = dir_name
        i = 1
    elif dir_size >= smallest_dir_size_to_free and dir_size < current_best_dir_size:
        current_best_dir_size = dir_size
        current_best_dir = dir_name

print('Best dir is %s with size: %d \n' % (current_best_dir, current_best_dir_size) )

