import sys

input_data = sys.stdin.read().split()
idx = 0
N = int(input_data[idx])
idx += 1
estoque = [0] * (N + 1)
for i in range(1, N + 1):
    estoque[i] = int(input_data[idx])
    idx += 1
P = int(input_data[idx])
idx += 1
vendas = 0
for _ in range(P):
    I = int(input_data[idx])
    idx += 1
    if estoque[I] > 0:
        estoque[I] -= 1
        vendas += 1
print(vendas)