import math
import sys

N = int(sys.stdin.readline())

count = 0
limit = int(math.isqrt(N - 1)) if N > 1 else 0

for a in range(2, limit + 1):
    if (N - 1) % a == 0:
        b = (N - 1) // a
        if a <= b and b >= 2:
            count += 1

print(count)