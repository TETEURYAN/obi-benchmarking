import sys
from itertools import permutations

a = list(map(int, sys.stdin.read().split()))

for p in permutations(a):
    x, y, z, w = p
    if x * w == y * z:
        print('S')
        break
else:
    print('N')