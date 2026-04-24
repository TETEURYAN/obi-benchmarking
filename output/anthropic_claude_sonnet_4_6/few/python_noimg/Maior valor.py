import sys

data = sys.stdin.read().split()
N = int(data[0])
M = int(data[1])
S = int(data[2])

result = -1
for i in range(M, N - 1, -1):
    if sum(int(d) for d in str(i)) == S:
        result = i
        break

print(result)