import sys
from collections import defaultdict

data = sys.stdin.read().split()
N = int(data[0])
K = int(data[1])
A = list(map(int, data[2:]))

prefix = 0
count = defaultdict(int)
count[0] = 1
ans = 0

for x in A:
    prefix += x
    ans += count[prefix - K]
    count[prefix] += 1

print(ans)