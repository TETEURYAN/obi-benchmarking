import sys
from itertools import combinations

input_data = sys.stdin.read().split()
if not input_data:
    sys.exit()

forces = list(map(int, input_data))
total = sum(forces)

if total % 2 != 0:
    print('N')
else:
    target = total // 2
    possible = False
    for combo in combinations(forces, 3):
        if sum(combo) == target:
            possible = True
            break
    
    if possible:
        print('S')
    else:
        print('N')