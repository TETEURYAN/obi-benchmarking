import sys

data = sys.stdin.read().split()
if not data:
    sys.exit()

T = int(data[0])
N = int(data[1])
x = list(map(int, data[2:2 + N]))
x.sort()

min_len = float('inf')

for i in range(N):
    if i == 0:
        length = (x[0] + x[1]) / 2.0
    elif i == N - 1:
        length = T - (x[N - 2] + x[N - 1]) / 2.0
    else:
        length = (x[i + 1] - x[i - 1]) / 2.0
    if length < min_len:
        min_len = length

print(f"{min_len:.2f}")