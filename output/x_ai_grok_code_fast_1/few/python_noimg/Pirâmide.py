import sys
import itertools

data = list(map(int, sys.stdin.read().split()))
possible = False
for perm in itertools.permutations(data):
    base = sum(perm[0:3])
    meio = sum(perm[3:5])
    topo = perm[5]
    if base == meio == topo:
        possible = True
        break
print('S' if possible else 'N')