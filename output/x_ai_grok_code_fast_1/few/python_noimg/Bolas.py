import sys
from itertools import permutations

balls = list(map(int, sys.stdin.read().split()))
for perm in permutations(balls):
    valid = True
    for i in range(7):
        if perm[i] == perm[i+1]:
            valid = False
            break
    if valid:
        print("S")
        sys.exit(0)
print("N")