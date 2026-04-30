
import sys

input = sys.stdin.read
data = input().split()
N = int(data[0])
T = int(data[1])

if T == 0:
    print(N)
elif T == 1:
    print(N * (N - 1))
else:
    total = 0
    for i in range(N):
        for j in range(i + 1, N):
            total += (j - i - 1)
    print(total)
