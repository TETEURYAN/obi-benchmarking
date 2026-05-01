import sys

L = int(sys.stdin.readline())
C = int(sys.stdin.readline())

tipo1 = L * C + (L - 1) * (C - 1)
tipo2 = 2 * (L - 1) + 2 * (C - 1)

print(tipo1)
print(tipo2)