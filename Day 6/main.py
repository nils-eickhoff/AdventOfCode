import collections

with open ('input.txt') as f:
    signal = f.readline()

signal_length = 14
for index in range(len(signal)):
    if collections.Counter(signal[index:index + signal_length]).most_common(1)[0][1] == 1:
        print(signal[index:index + signal_length])
        print(index + signal_length)
        break

