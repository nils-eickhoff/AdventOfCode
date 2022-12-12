with open('Day 7/test.txt') as f:
    lines = f.read().splitlines()

treshold = 100000

def countDirs(terminalLines):
    tot_sum = 0
    level_list = []
    level = 0
    counter = 0
    for i, line in enumerate(terminalLines):
        if i == 147:
            print(7)
        if line == '$ ls':
            current_sum = 0
        elif line == '$ cd ..':
            if counter == 0:
                if current_sum <= treshold:
                    tot_sum += current_sum
                #level_list[-1] += current_sum
            #else:
            
            if counter > 0:
                if level_list[-1] <= treshold:
                    tot_sum += level_list[-1]
                level_list.pop(-1)
            level -= 1
            counter += 1
        elif line[0:4] == '$ cd':
            level_list.append(current_sum)
            level += 1
            counter = 0
        else : # ls ...
            gap = line.find(' ')
            if line[0:gap] != 'dir':
                current_sum += int(line[0:gap])
                level_list = list(map(lambda x: x + int(line[0:gap]), level_list))
    #level_list[level] += current_sum
    #current_sum = 0
    while level > 0:
        if level_list[-1] <= 100000:
            tot_sum += level_list[-1]
        if level <= len(level_list) -1:
            level_list[level-1] += level_list[-1]
            level_list.pop(-1)
        level -= 1
    return tot_sum

tot_sum = countDirs(lines)
print(tot_sum)
            