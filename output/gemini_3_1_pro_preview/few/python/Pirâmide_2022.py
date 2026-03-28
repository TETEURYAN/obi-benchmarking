import sys

input_data = sys.stdin.read().split()
if not input_data:
    exit()

n = int(input_data[0])

for i in range(n):
    row = []
    for j in range(n):
        val = min(i, j, n - 1 - i, n - 1 - j) + 1
        row.append(str(val))
    print(" ".join(row))