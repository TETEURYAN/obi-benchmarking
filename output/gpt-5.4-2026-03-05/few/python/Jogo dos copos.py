import sys

data = sys.stdin.read().split()
if not data:
    sys.exit()

n = int(data[0])
pos = data[1]

for i in range(n):
    move = int(data[2 + i])
    if move == 1:
        if pos == 'A':
            pos = 'B'
        elif pos == 'B':
            pos = 'A'
    elif move == 2:
        if pos == 'B':
            pos = 'C'
        elif pos == 'C':
            pos = 'B'
    else:
        if pos == 'A':
            pos = 'C'
        elif pos == 'C':
            pos = 'A'

print(pos)