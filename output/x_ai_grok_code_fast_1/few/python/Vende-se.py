import sys

input_data = sys.stdin.read().split()
N = int(input_data[0])
K = int(input_data[1])
X = list(map(int, input_data[2:]))
X.sort()
M = N - K
min_diff = float('inf')
for i in range(N - M + 1):
    diff = X[i + M - 1] - X[i]
    if diff < min_diff:
        min_diff = diff
print(min_diff)