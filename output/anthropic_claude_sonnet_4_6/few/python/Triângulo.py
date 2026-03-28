import sys
from itertools import combinations

data = sys.stdin.read().split()
varetas = [int(x) for x in data]

found = False
for trio in combinations(varetas, 3):
    a, b, c = trio
    if a < b + c and b < a + c and c < a + b:
        found = True
        break

print('S' if found else 'N')