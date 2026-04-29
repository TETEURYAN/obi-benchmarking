import math
import sys

N = int(sys.stdin.readline())

# Total trees:
# oaks at vertices of an x by y rectangle of cells: (x+1)(y+1)
# eucalyptus at centers of cells: xy
# total = (x+1)(y+1) + xy = 2xy + x + y + 1
#
# Let a = 2x + 1 and b = 2y + 1, both odd positive integers.
# Then:
# 2N - 1 = (2x + 1)(2y + 1) = ab
#
# Since at least one of each species must be planted, x,y >= 1.
# Thus a,b >= 3.
# Each unordered factorization of 2N-1 into odd factors >= 3 gives one arrangement.

M = 2 * N - 1
ans = 0

r = int(math.isqrt(M))
for d in range(3, r + 1, 2):
    if M % d == 0:
        q = M // d
        if q >= 3:
            ans += 1

print(ans)