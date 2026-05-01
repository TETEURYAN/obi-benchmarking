n = int(input())
pos = input().strip()

for _ in range(n):
    move = int(input().strip())
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
    elif move == 3:
        if pos == 'A':
            pos = 'C'
        elif pos == 'C':
            pos = 'A'

print(pos)