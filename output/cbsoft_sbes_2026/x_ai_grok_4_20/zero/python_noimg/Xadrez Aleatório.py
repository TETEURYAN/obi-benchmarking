
import sys

input = sys.stdin.read
data = input().split()
N = int(data[0])
T = int(data[1])

if T == 0:
    print(N * (N - 1))
elif T == 1:
    print(N * (N - 1) * (N - 2))
else:
    total = 0
    for i in range(N):
        for j in range(i + 1, N):
            between = j - i - 1
            left = i
            right = N - 1 - j
            ways = (left + between + right) * (left + between + right + 1) // 2
            total += ways
    print(total)
