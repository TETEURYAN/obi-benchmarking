import sys
from itertools import combinations

data = sys.stdin.read().split()
x = list(map(int, data))

total = sum(x)
found = False

for combo in combinations(range(6), 3):
    s = sum(x[i] for i in combo)
    if s * 2 == total:
        found = True
        break

print('S' if found else 'N')