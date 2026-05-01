import sys

data = sys.stdin.read().split()
if not data:
    print(0)
    exit()

idx = 0
n = int(data[idx]); idx += 1
estoque = [0] * n
for i in range(n):
    estoque[i] = int(data[idx]); idx += 1

p = int(data[idx]); idx += 1
vendidos = 0
for _ in range(p):
    tamanho = int(data[idx]); idx += 1
    if estoque[tamanho - 1] > 0:
        estoque[tamanho - 1] -= 1
        vendidos += 1

print(vendidos)