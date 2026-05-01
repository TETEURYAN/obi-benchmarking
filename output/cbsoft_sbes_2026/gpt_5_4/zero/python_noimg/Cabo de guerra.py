import sys
from itertools import combinations

x = list(map(int, sys.stdin.read().split()))
total = sum(x)

if total % 2 != 0:
    print('N')
else:
    half = total // 2
    for comb in combinations(range(6), 3):
        if x[comb[0]] + x[comb[1]] + x[comb[2]] == half:
            print('S')
            break
    else:
        print('N')