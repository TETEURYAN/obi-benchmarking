import sys
import math
from itertools import permutations

input_data = sys.stdin.read().split()
idx = 0
N = int(input_data[idx])
idx += 1
total = math.factorial(N)
perms = set()
for _ in range(total - 1):
    perm = tuple(int(input_data[idx + i]) for i in range(N))
    perms.add(perm)
    idx += N
for perm in permutations(range(1, N + 1)):
    if tuple(perm) not in perms:
        print(*perm)
        break