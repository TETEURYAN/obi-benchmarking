
import sys

input = sys.stdin.read
data = input().split()

N = int(data[0])
T = int(data[1])

top = list(map(int, data[2:2+N]))
bottom = list(map(int, data[2+N:2+2*N]))

flips = [0] * (N + 1)

index = 2 + 2 * N
for _ in range(T):
    i = int(data[index])
    j = int(data[index + 1])
    flips[i - 1] += 1
    flips[j] += 1
    index += 2

current_flip = 0
result = []
for k in range(N):
    current_flip = (current_flip + flips[k]) % 2
    if current_flip == 0:
        result.append(str(top[k]))
    else:
        result.append(str(bottom[k]))

print(' '.join(result))
