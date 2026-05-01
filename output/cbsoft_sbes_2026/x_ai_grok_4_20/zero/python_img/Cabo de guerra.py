
from itertools import combinations

forces = list(map(int, input().split()))
total = sum(forces)

if total % 2 != 0:
    print('N')
else:
    target = total // 2
    found = False
    for comb in combinations(forces, 3):
        if sum(comb) == target:
            found = True
            break
    print('S' if found else 'N')
