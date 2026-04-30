
N = int(input())
estoque = [0] * (N + 1)
for i in range(1, N + 1):
    estoque[i] = int(input())

P = int(input())
vendidos = 0
for _ in range(P):
    tam = int(input())
    if estoque[tam] > 0:
        estoque[tam] -= 1
        vendidos += 1

print(vendidos)
