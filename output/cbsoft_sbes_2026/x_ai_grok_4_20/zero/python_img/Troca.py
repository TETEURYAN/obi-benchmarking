
import sys

input = sys.stdin.read
data = input().split()

N = int(data[0])
T = int(data[1])

up = [int(x) for x in data[2:2+N]]
down = [int(x) for x in data[2+N:2+2*N]]

flips = [0] * (N + 1)

index = 2 + 2 * N
for _ in range(T):
    i = int(data[index])
    j = int(data[index + 1])
    flips[i - 1] += 1
    flips[j] += 1
    index += 2

current = 0
for i in range(N):
    current += flips[i]
    if current % 2 == 1:
        up[i], down[i] = down[i], up[i]

print(' '.join(map(str, up)))
