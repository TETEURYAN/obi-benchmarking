
import sys

input = sys.stdin.read
data = input().split()

N = int(data[0])
C = int(data[1])
S = int(data[2])
commands = list(map(int, data[3:]))

position = 1
count = 0

if position == S:
    count += 1

for cmd in commands:
    if cmd == 1:
        position += 1
        if position > N:
            position = 1
    else:
        position -= 1
        if position < 1:
            position = N
    if position == S:
        count += 1

print(count)
