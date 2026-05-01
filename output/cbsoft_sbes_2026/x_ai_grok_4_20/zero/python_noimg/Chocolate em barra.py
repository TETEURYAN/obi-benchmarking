
import sys

input = sys.stdin.read
data = input().split()

N = int(data[0])
X1 = int(data[1])
Y1 = int(data[2])
X2 = int(data[3])
Y2 = int(data[4])

# Normalizar para 0-based
r1, c1 = X1 - 1, Y1 - 1
r2, c2 = X2 - 1, Y2 - 1

half = N // 2

# Corte horizontal no meio: linha half-1 e half são separadas
# Figurinha 1 acima ou igual ao meio, figurinha 2 abaixo
sep_h = (r1 < half) != (r2 < half)

# Corte vertical no meio
sep_v = (c1 < half) != (c2 < half)

if sep_h or sep_v:
    print("S")
else:
    print("N")
