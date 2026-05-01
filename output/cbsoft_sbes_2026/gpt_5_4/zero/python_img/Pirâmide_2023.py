import sys
from itertools import combinations

x = list(map(int, sys.stdin.read().split()))
total = sum(x)

if total % 3 != 0:
    print('N')
    sys.exit()

target = total // 3

for i in range(6):
    if x[i] == target:
        rest = [x[j] for j in range(6) if j != i]
        for a, b in combinations(range(5), 2):
            if rest[a] + rest[b] == target:
                print('S')
                sys.exit()

print('N')