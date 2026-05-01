import sys

L = int(sys.stdin.readline().strip())
C = int(sys.stdin.readline().strip())

type1 = L * C + (L - 1) * (C - 1)
type2 = 2 * (L - 1) + 2 * (C - 1)

print(type1)
print(type2)