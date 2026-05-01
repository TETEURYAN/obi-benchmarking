import sys

E = int(sys.stdin.readline().strip())
D = int(sys.stdin.readline().strip())

if E > D:
    resultado = E + D
else:
    resultado = 2 * (D - E)

print(resultado)