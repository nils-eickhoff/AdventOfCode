with open('Day 10/test.txt') as f:
    lines = f.read().splitlines()

# First star

sum_signal_strength = 0
tot_sum = 1
cycle_nr = 0

def checkCycle(cycle, sum, signal_strength):
    if cycle == 20:
        signal_strength += sum*cycle
    elif cycle == 60:
        signal_strength += sum*cycle
    elif cycle == 100:
        signal_strength += sum*cycle
    elif cycle == 140:
        signal_strength += sum*cycle
    elif cycle == 180:
        signal_strength += sum*cycle
    elif cycle == 220:
        signal_strength += sum*cycle
    return signal_strength

for i, line in enumerate(lines):
    if cycle_nr > 220:
        break
    if line == 'noop':
        cycle_nr += 1
        sum_signal_strength = checkCycle(cycle_nr, tot_sum, sum_signal_strength)
    else:
        for cycles in range(2):
            cycle_nr += 1
            sum_signal_strength = checkCycle(cycle_nr, tot_sum, sum_signal_strength)
        tot_sum += int(line[5::])


print(tot_sum)
print(cycle_nr)
print(sum_signal_strength)

# Second star

row = ""
tot_sum = 1
cycle_nr = 0

def checkPrintCycle(sum, cycle, cur_row):
    if cycle % 40 == 0:
        print(cur_row)
        cur_row = ""
    return sum, cur_row

for i, line in enumerate(lines):
    if line == 'noop':
        cycle_nr += 1
        if cycle_nr % 40 -1 >= tot_sum - 1 and cycle_nr % 40 -1 <= tot_sum + 1:
            row += "#"
        else:
            row += "."
        tot_sum, row = checkPrintCycle(tot_sum, cycle_nr, row)
    else:
        for cycles in range(2):
            cycle_nr += 1
            if cycle_nr % 40 -1 >= tot_sum - 1 and cycle_nr % 40 -1 <= tot_sum + 1:
                row += "#"
            else:
                row += "."
            tot_sum, row = checkPrintCycle(tot_sum, cycle_nr, row)
        tot_sum += int(line[5::])
        
