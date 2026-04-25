import sys

data = list(map(int, sys.stdin.read().split()))
if not data:
    sys.exit()

n = data[0]
m = data[1]
idx = 2

last_pivot = -1
seen_zero_row = False

for _ in range(n):
    pivot = -1
    for j in range(m):
        val = data[idx]
        idx += 1
        if pivot == -1 and val != 0:
            pivot = j

    if pivot == -1:
        seen_zero_row = True
    else:
        if seen_zero_row or pivot <= last_pivot:
            print('N')
            sys.exit()
        last_pivot = pivot

print('S')