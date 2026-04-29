import sys
from itertools import combinations

x = list(map(int, sys.stdin.read().split()))
total = sum(x)

if total % 3 != 0:
    print('N')
    sys.exit()

target = total // 3
idx = range(6)
possible = False

for c1 in combinations(idx, 1):
    if sum(x[i] for i in c1) != target:
        continue
    rem1 = [i for i in idx if i not in c1]
    for c2 in combinations(rem1, 2):
        if sum(x[i] for i in c2) != target:
            continue
        rem2 = [i for i in rem1 if i not in c2]
        if sum(x[i] for i in rem2) == target:
            possible = True
            break
    if possible:
        break

if not possible:
    for c1 in combinations(idx, 2):
        if sum(x[i] for i in c1) != target:
            continue
        rem1 = [i for i in idx if i not in c1]
        for c2 in combinations(rem1, 1):
            if sum(x[i] for i in c2) != target:
                continue
            rem2 = [i for i in rem1 if i not in c2]
            if sum(x[i] for i in rem2) == target:
                possible = True
                break
        if possible:
            break

print('S' if possible else 'N')