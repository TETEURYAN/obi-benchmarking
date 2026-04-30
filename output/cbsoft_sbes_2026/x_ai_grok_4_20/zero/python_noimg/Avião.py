
import sys

input = sys.stdin.read
data = input().strip().split()
F = int(data[0])
C = int(data[1])
E = int(data[2])
B = int(data[3])

# Número de fileiras na classe econômica
filas_economicas = F - E + 1

# Capacidade total da classe econômica
capacidade = filas_economicas * C

if B > capacidade:
    print("PROXIMO VOO")
else:
    # Posição 1-based na classe econômica
    pos = B - 1
    fila_relativa = pos // C
    coluna = pos % C
    fila = E + fila_relativa
    letra = chr(ord('A') + coluna)
    print(fila, letra)
