
import numpy as np

# Test
#monkey_list = [ [79, 98], [54, 65, 75, 74], [79, 60, 97], [74] ]
# Input
monkey_list = [ [61], [76, 92, 53, 93, 79, 86, 81], [91, 99], [58, 67, 66], [94, 54, 62, 73], [59, 95, 51, 58, 58], [87, 69, 92, 56, 91, 93, 88, 73], [71, 57, 86, 67, 96, 95] ]

# First star
rounds = 20
monkey_inspections = [0, 0, 0, 0, 0, 0, 0, 0]

def Operations(worry_level, monkey):
    if monkey == 0:
        worry_level *= 11
    elif monkey == 1:
        worry_level += 4
    elif monkey == 2:
        worry_level *= 19
    elif monkey == 3:
        worry_level *= worry_level
    elif monkey == 4:
        worry_level += 1
    elif monkey == 5:
        worry_level += 3
    elif monkey == 6:
        worry_level += 8
    elif monkey == 7:
        worry_level += 7
    return int(np.floor(worry_level / 3))

def Test(worry_level, monkey):            
    if monkey == 0:
        if worry_level % 5 == 0:
            new_monkey = 7
        else:
            new_monkey = 4
    elif monkey == 1:
        if worry_level % 2 == 0:
            new_monkey = 2
        else:
            new_monkey = 6
    elif monkey == 2:
        if worry_level % 13 == 0:
            new_monkey = 5
        else:
            new_monkey = 0
    elif monkey == 3:
        if worry_level % 7 == 0:
            new_monkey = 6
        else:
            new_monkey = 1
    elif monkey == 4:
        if worry_level % 19 == 0:
            new_monkey = 3
        else:
            new_monkey = 7
    elif monkey == 5:
        if worry_level % 11 == 0:
            new_monkey = 0
        else:
            new_monkey = 4
    elif monkey == 6:
        if worry_level % 3 == 0:
            new_monkey = 5
        else:
            new_monkey = 2
    elif monkey == 7:
        if worry_level % 17 == 0:
            new_monkey = 3
        else:
            new_monkey = 1
    return new_monkey

for round in range(rounds):
    for monkey_idx, monkey in enumerate(monkey_list):
        monkey_inspections[monkey_idx] += len(monkey)
        for item in monkey:
            item = Operations(item, monkey_idx)
            new_monkey_idx = Test(item, monkey_idx)
            monkey_list[new_monkey_idx].append(item)
        item = monkey_list[monkey_idx].clear()

for i in range(len(monkey_list)):
    print('Monkey %d:' % i)
    print(*monkey_list[i], sep = ", ")
    print('\n')

for i in range(len(monkey_list)):
    print('Monkey %d inspected items %d times' % (i, monkey_inspections[i]))

monkey_inspections.sort()
print(monkey_inspections[-1] * monkey_inspections[-2])

# Second star
print('-----------SECOND STAR -----------\n')

monkey_inspections = [0, 0, 0, 0, 0, 0, 0, 0]
lcm_num = np.lcm.reduce([5, 2, 13, 7, 19, 11, 3, 17], )
rounds = 10000
monkey_list = [ [61], [76, 92, 53, 93, 79, 86, 81], [91, 99], [58, 67, 66], [94, 54, 62, 73], [59, 95, 51, 58, 58], [87, 69, 92, 56, 91, 93, 88, 73], [71, 57, 86, 67, 96, 95] ]

def newOperations(worry_level, monkey, lcm):
    if monkey == 0:
        worry_level *= 11
    elif monkey == 1:
        worry_level += 4
    elif monkey == 2:
        worry_level *= 19
    elif monkey == 3:
        worry_level *= worry_level
    elif monkey == 4:
        worry_level += 1
    elif monkey == 5:
        worry_level += 3
    elif monkey == 6:
        worry_level += 8
    elif monkey == 7:
        worry_level += 7
    return worry_level % lcm

for round in range(rounds):
    if round == 1000:
        print('')
    for monkey_idx, monkey in enumerate(monkey_list):
        monkey_inspections[monkey_idx] += len(monkey)
        for item in monkey:
            item = newOperations(item, monkey_idx, lcm_num)
            new_monkey_idx = Test(item, monkey_idx)
            monkey_list[new_monkey_idx].append(item)
        item = monkey_list[monkey_idx].clear()

for i in range(len(monkey_list)):
    print('Monkey %d:' % i)
    print(*monkey_list[i], sep = ", ")
    print('\n')

for i in range(len(monkey_list)):
    print('Monkey %d inspected items %d times' % (i, monkey_inspections[i]))

monkey_inspections.sort()
print(monkey_inspections[-1] * monkey_inspections[-2])