import sys
from itertools import combinations

a = list(map(int, sys.stdin.read().split()))
total = sum(a)

if total % 2 != 0:
    print('N')
else:
    half = total // 2
    for comb in combinations(a, 3):
        if sum(comb) == half:
            print('S')
            break
    else:
        print('N')