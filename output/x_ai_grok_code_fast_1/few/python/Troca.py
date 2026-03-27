import sys

input_data = sys.stdin.read().split()
idx = 0

N = int(input_data[idx])
idx += 1
T = int(input_data[idx])
idx += 1

up = [0] + [int(input_data[idx + i]) for i in range(N)]
idx += N
down = [0] + [int(input_data[idx + i]) for i in range(N)]
idx += N

diff = [0] * (N + 2)
for _ in range(T):
    i = int(input_data[idx])
    idx += 1
    j = int(input_data[idx])
    idx += 1
    diff[i] += 1
    if j + 1 <= N + 1:
        diff[j + 1] -= 1

count = [0] * (N + 1)
current = 0
for i in range(1, N + 1):
    current += diff[i]
    count[i] = current

for i in range(1, N + 1):
    if count[i] % 2 == 1:
        print(down[i], end=' ')
    else:
        print(up[i], end=' ')
print()