import sys

data = list(map(int, sys.stdin.read().split()))
if not data:
    sys.exit()

n = data[0]
a = []
idx = 1
for _ in range(n):
    row = data[idx:idx + n]
    a.append(row)
    idx += n

row_sums = [sum(row) for row in a]
col_sums = [0] * n
for i in range(n):
    s = 0
    for j in range(n):
        s += a[j][i]
    col_sums[i] = s

from collections import Counter

row_count = Counter(row_sums)
col_count = Counter(col_sums)

correct_sum = None
for s, c in row_count.items():
    if c > 1:
        correct_sum = s
        break
if correct_sum is None:
    for s, c in col_count.items():
        if c > 1:
            correct_sum = s
            break

bad_row = -1
for i in range(n):
    if row_sums[i] != correct_sum:
        bad_row = i
        break

bad_col = -1
for j in range(n):
    if col_sums[j] != correct_sum:
        bad_col = j
        break

changed = a[bad_row][bad_col]
original = changed + (correct_sum - row_sums[bad_row])

print(original, changed)