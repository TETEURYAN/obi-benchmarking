
n = int(input())
pos = input().strip()
for _ in range(n):
    m = int(input())
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
    else:  # m == 3
        if pos == 'A':
            pos = 'C'
        elif pos == 'C':
            pos = 'A'
print(pos)
