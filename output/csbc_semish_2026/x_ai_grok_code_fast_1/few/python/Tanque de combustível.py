import sys

input_data = sys.stdin.read().split()
C = int(input_data[0])
D = int(input_data[1])
T = int(input_data[2])
necessario = D / C
comprar = max(0, necessario - T)
print(f"{comprar:.1f}")