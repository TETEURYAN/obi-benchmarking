import sys
from itertools import combinations

data = list(map(int, sys.stdin.read().split()))
s = sum(data)
if s % 2 != 0:
    print('N')
else:
    target = s // 2
    found = any(sum(comb) == target for comb in combinations(data, 3))
    print('S' if found else 'N')