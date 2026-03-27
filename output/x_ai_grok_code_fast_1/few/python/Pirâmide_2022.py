import sys

input_data = sys.stdin.read().split()
N = int(input_data[0])
for i in range(N):
    row = []
    for j in range(N):
        val = min(i + 1, j + 1, N - i, N - j)
        row.append(str(val))
    print(' '.join(row))