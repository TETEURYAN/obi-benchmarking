
import sys
from itertools import permutations

input = sys.stdin.read
data = input().split()

N = int(data[0])
given = set()

index = 1
for i in range((1 << N) - 1):
    perm = tuple(int(data[index + j]) for j in range(N))
    given.add(perm)
    index += N

all_perms = permutations(range(1, N + 1))
for p in all_perms:
    if p not in given:
        print(' '.join(map(str, p)))
        break
