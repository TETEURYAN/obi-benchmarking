
import sys
from collections import defaultdict

input = sys.stdin.read
data = input().split()

N = int(data[0])
K = int(data[1])
X = list(map(int, data[2:2+N]))

prefix = [0] * (N + 1)
for i in range(1, N + 1):
    prefix[i] = prefix[i-1] + X[i-1]

freq = defaultdict(int)
freq[0] = 1
count = 0

if K == 0:
    for i in range(1, N + 1):
        count += freq[prefix[i]]
        freq[prefix[i]] += 1
else:
    for i in range(1, N + 1):
        target = prefix[i] - K
        count += freq[target]
        freq[prefix[i]] += 1

print(count)
