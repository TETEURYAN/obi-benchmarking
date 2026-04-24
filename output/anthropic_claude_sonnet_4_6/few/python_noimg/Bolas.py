from itertools import permutations
import sys

balls = list(map(int, sys.stdin.read().split()))

found = False
for perm in permutations(balls):
    valid = True
    for i in range(7):
        if perm[i] == perm[i+1]:
            valid = False
            break
    if valid:
        found = True
        break

print("S" if found else "N")