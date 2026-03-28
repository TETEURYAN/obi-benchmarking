import sys
import itertools

data = list(map(int, sys.stdin.read().split()))
a, b, c, d = data

found = False
for perm in itertools.permutations([a, b, c, d]):
    if perm[0] * perm[3] == perm[1] * perm[2]:
        found = True
        break

print('S' if found else 'N')