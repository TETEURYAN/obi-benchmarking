import sys

data = sys.stdin.read().split()
if not data:
    sys.exit()

L = int(data[0])
C = int(data[1])

tipo1 = L * C + (L - 1) * (C - 1)
tipo2 = 2 * (L - 1) + 2 * (C - 1)

print(tipo1)
print(tipo2)