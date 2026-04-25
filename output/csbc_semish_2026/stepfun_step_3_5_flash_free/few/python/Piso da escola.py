import sys

data = sys.stdin.read().split()
L = int(data[0])
C = int(data[1])
tipo1 = L * C + (L - 1) * (C - 1)
tipo2 = 2 * (L + C - 2)
print(tipo1)
print(tipo2)