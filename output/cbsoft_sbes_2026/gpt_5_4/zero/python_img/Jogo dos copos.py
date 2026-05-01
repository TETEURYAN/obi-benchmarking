import sys

data = sys.stdin.read().split()
n = int(data[0])
pos = data[1]

for i in range(2, 2 + n):
    mov = int(data[i])
    if mov == 1:
        if pos == 'A':
            pos = 'B'
        elif pos == 'B':
            pos = 'A'
    elif mov == 2:
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