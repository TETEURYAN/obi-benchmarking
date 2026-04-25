import sys
import math

data = sys.stdin.read().split()
if not data:
    sys.exit()

n = int(data[0])

ans = 0
limit = int(math.isqrt(n))

for d in range(1, limit + 1):
    if n % d != 0:
        continue
    q = n // d
    a = d - 1
    b = q - 1
    if a >= 1 and b >= 1 and a <= b:
        ans += 1

print(ans)