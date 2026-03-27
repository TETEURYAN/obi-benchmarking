import sys

input_data = sys.stdin.read().split()
idx = 0
N = int(input_data[idx])
idx += 1
pos = input_data[idx]
idx += 1
for _ in range(N):
    mov = int(input_data[idx])
    idx += 1
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
    elif mov == 3:
        if pos == 'A':
            pos = 'C'
        elif pos == 'C':
            pos = 'A'
print(pos)