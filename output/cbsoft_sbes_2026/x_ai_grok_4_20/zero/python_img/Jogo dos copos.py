
n = int(input())
pos = input().strip()
moves = [int(input()) for _ in range(n)]

for m in moves:
    if m == 1:
        if pos == 'A':
            pos = 'B'
        elif pos == 'B':
            pos = 'A'
    elif m == 2:
        if pos == 'B':
            pos = 'C'
        elif pos == 'C':
            pos = 'B'
    elif m == 3:
        if pos == 'A':
            pos = 'C'
        elif pos == 'C':
            pos = 'A'

print(pos)
