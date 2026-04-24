import sys

data = sys.stdin.read().split()
N = int(data[0])
C = int(data[1])
S = int(data[2])

commands = [int(data[3 + i]) for i in range(C)]

pos = 1
count = 0

for cmd in commands:
    pos = (pos - 1 + cmd) % N + 1
    if pos == S:
        count += 1

print(count)