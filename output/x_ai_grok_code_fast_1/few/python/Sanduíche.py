import sys

input_data = sys.stdin.read().split()
idx = 0
N = int(input_data[idx])
idx += 1
M = int(input_data[idx])
idx += 1

pairs = []
for _ in range(M):
    a = int(input_data[idx])
    b = int(input_data[idx + 1])
    pairs.append((a, b))
    idx += 2

count = 0
for mask in range(1, 1 << N):
    valid = True
    for a, b in pairs:
        if (mask & (1 << (a - 1))) and (mask & (1 << (b - 1))):
            valid = False
            break
    if valid:
        count += 1

print(count)