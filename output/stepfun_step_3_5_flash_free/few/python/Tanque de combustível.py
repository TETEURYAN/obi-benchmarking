import sys

data = sys.stdin.read().split()
if not data:
    exit()

C = int(data[0])
D = int(data[1])
T = int(data[2])

litros_necessarios = D / C
comprar = max(0, litros_necessarios - T)

print(f"{comprar:.1f}")