import sys
from itertools import permutations

data = sys.stdin.read().split()
n = int(data[0])

given = set()
idx = 1
for _ in range(1, n):  # n! - 1 lines, but let's read all remaining
    pass

# Re-read properly
idx = 1
total_lines = len(data) - 1
num_perms = total_lines // n

given = set()
for i in range(num_perms):
    perm = tuple(int(data[idx + j]) for j in range(n))
    given.add(perm)
    idx += n

all_perms = set(permutations(range(1, n + 1)))
missing = all_perms - given

result = list(missing)[0]
print(*result)