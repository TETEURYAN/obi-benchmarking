import sys
from collections import defaultdict

input_data = sys.stdin.read().split()
N = int(input_data[0])
D = int(input_data[1])
C = list(map(int, input_data[2:]))

prefix = [0] * (N + 1)
for i in range(1, N + 1):
    prefix[i] = prefix[i - 1] + C[i - 1]

S = prefix[N]
count = 0

# subsequências contínuas
freq = defaultdict(int)
freq[0] = 1
for j in range(1, N + 1):
    target = prefix[j] - D
    if target in freq:
        count += freq[target]
    freq[prefix[j]] += 1

# extremidades
if N >= 2:
    freq2 = defaultdict(int)
    target_diff = D - S
    for i in range(1, N):
        freq2[prefix[i]] += 1
        j = i + 1
        target = prefix[i] + target_diff
        if target in freq2:
            count += freq2[target]

print(count)