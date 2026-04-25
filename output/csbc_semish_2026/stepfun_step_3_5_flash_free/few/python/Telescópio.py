import sys

data = sys.stdin.read().split()
if not data:
    exit()
A = int(data[0])
N = int(data[1])
count = 0
idx = 2
for _ in range(N):
    F = int(data[idx])
    idx += 1
    if A * F >= 40000000:
        count += 1
print(count)