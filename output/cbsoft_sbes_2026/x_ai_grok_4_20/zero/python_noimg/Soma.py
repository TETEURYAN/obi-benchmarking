
from collections import defaultdict
import sys

input = sys.stdin.read
data = input().split()

N = int(data[0])
K = int(data[1])
X = [int(x) for x in data[2:2+N]]

prefix = [0] * (N + 1)
for i in range(1, N + 1):
    prefix[i] = prefix[i - 1] + X[i - 1]

count = defaultdict(int)
count[0] = 1
ans = 0

for i in range(1, N + 1):
    target = prefix[i] - K
    ans += count[target]
    count[prefix[i]] += 1

print(ans)
