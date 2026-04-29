import sys

data = list(map(int, sys.stdin.read().split()))
idx = 0

N = data[idx]
idx += 1

estoque = [0] * (N + 1)
for i in range(1, N + 1):
    estoque[i] = data[idx]
    idx += 1

P = data[idx]
idx += 1

vendidos = 0
for _ in range(P):
    tamanho = data[idx]
    idx += 1
    if estoque[tamanho] > 0:
        estoque[tamanho] -= 1
        vendidos += 1

print(vendidos)