
import sys
from itertools import permutations

input = sys.stdin.read
data = input().split()

N = int(data[0])
total = 1
for i in range(1, N + 1):
    total *= i

seen = set()
index = 1
for _ in range(total - 1):
    perm = tuple(int(data[index + j]) for j in range(N))
    seen.add(perm)
    index += N

for p in permutations(range(1, N + 1)):
    if p not in seen:
        print(' '.join(map(str, p)))
        break
