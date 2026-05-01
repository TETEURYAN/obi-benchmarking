import sys

input_data = sys.stdin.read().split()
N = int(input_data[0])
C = int(input_data[1])
S = int(input_data[2])
commands = list(map(int, input_data[3:]))

pos = 1
count = 0
if pos == S:
    count += 1
for cmd in commands:
    pos = (pos + cmd - 1) % N + 1
    if pos == S:
        count += 1
print(count)