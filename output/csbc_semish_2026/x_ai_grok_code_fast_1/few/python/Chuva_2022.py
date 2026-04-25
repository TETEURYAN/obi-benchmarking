import sys

input_data = sys.stdin.read().split()
idx = 0
N = int(input_data[idx])
idx += 1
S = int(input_data[idx])
idx += 1
X = [int(input_data[i]) for i in range(idx, idx + N)]

prefix = [0] * (N + 1)
for i in range(1, N + 1):
    prefix[i] = prefix[i - 1] + X[i - 1]

counter = {0: 1}
count = 0
for i in range(1, N + 1):
    target = prefix[i] - S
    if target in counter:
        count += counter[target]
    if prefix[i] in counter:
        counter[prefix[i]] += 1
    else:
        counter[prefix[i]] = 1

print(count)