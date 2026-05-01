import sys

data = list(map(int, sys.stdin.read().split()))
N, C, S = data[0], data[1], data[2]
commands = data[3:]

pos = 1
count = 1 if pos == S else 0

for x in commands:
    pos += x
    if pos > N:
        pos = 1
    elif pos < 1:
        pos = N
    if pos == S:
        count += 1

print(count)