import sys

input_data = sys.stdin.read().split()
N = int(input_data[0])
pesos = list(map(int, input_data[1:]))

from collections import deque
fila = deque(pesos)
pilha = []

while fila:
    peso = fila.popleft()
    if pilha and abs(peso - pilha[-1]) <= 8:
        pilha.pop()
        pilha.append(peso)
    elif peso <= 8:
        pilha.append(peso)
    else:
        print('N')
        sys.exit(0)

print('S')