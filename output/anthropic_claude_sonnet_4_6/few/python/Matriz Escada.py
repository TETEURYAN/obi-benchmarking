import sys

data = sys.stdin.read().split()
idx = 0
n = int(data[idx]); idx += 1
m = int(data[idx]); idx += 1

matrix = []
for i in range(n):
    row = [int(data[idx+j]) for j in range(m)]
    idx += m
    matrix.append(row)

def find_pivot(row):
    for j, val in enumerate(row):
        if val != 0:
            return j
    return -1

is_staircase = True
prev_pivot = -1
zero_only_seen = False

for i in range(n):
    pivot = find_pivot(matrix[i])
    if pivot == -1:
        zero_only_seen = True
    else:
        if zero_only_seen:
            is_staircase = False
            break
        if pivot <= prev_pivot:
            is_staircase = False
            break
        prev_pivot = pivot

print('S' if is_staircase else 'N')