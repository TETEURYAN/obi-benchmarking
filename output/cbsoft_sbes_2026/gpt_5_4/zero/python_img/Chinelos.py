import sys

data = list(map(int, sys.stdin.read().split()))
it = iter(data)

N = next(it)
estoque = [0] * (N + 1)

for i in range(1, N + 1):
    estoque[i] = next(it)

P = next(it)
vendidos = 0

for _ in range(P):
    tamanho = next(it)
    if estoque[tamanho] > 0:
        estoque[tamanho] -= 1
        vendidos += 1

print(vendidos)