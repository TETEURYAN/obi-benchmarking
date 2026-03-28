import sys

data = sys.stdin.read().split()
if not data:
    exit()
T = int(data[0])
N = int(data[1])
X = list(map(int, data[2:2+N]))
X.sort()
min_len = float('inf')
min_len = min(min_len, (X[0] + X[1]) / 2.0)
min_len = min(min_len, T - (X[N-2] + X[N-1]) / 2.0)
for i in range(1, N-1):
    min_len = min(min_len, (X[i+1] - X[i-1]) / 2.0)
print("{:.2f}".format(min_len))