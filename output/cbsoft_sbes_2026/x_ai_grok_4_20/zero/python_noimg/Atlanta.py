
import sys
import math

A = int(input().strip())
B = int(input().strip())

if A % 4 != 0:
    print(-1, -1)
    sys.exit(0)

P = A // 4
D = int(math.sqrt(B))
if D * D != B:
    print(-1, -1)
    sys.exit(0)

found = False
L = -1
C = -1

for x in range(1, D + 1):
    if (D - x) % 2 == 0:
        k = (D - x) // 2
        if k > 0 and P % k == 0:
            s = P // k
            if s % 2 == 1:
                n = (s - 1) // 2
                if n == x:
                    L = 2 * x + 1
                    C = L + 2 * k
                    found = True
                    break

if not found:
    print(-1, -1)
else:
    if L > C:
        L, C = C, L
    print(L, C)
