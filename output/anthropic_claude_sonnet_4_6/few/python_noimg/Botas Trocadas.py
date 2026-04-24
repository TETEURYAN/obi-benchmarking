import sys
from collections import defaultdict

data = sys.stdin.read().split()
n = int(data[0])
idx = 1
count = defaultdict(lambda: {'D': 0, 'E': 0})
for _ in range(n):
    m = int(data[idx])
    l = data[idx+1]
    count[m][l] += 1
    idx += 2

total = 0
for m in count:
    total += min(count[m]['D'], count[m]['E'])

print(total)