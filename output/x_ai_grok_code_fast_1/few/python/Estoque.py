import sys

input_data = sys.stdin.read().split()
idx = 0
M = int(input_data[idx])
idx += 1
N = int(input_data[idx])
idx += 1
stock = []
for i in range(M):
    row = []
    for j in range(N):
        row.append(int(input_data[idx]))
        idx += 1
    stock.append(row)
P = int(input_data[idx])
idx += 1
vendas = 0
for _ in range(P):
    I = int(input_data[idx])
    idx += 1
    J = int(input_data[idx])
    idx += 1
    if stock[I-1][J-1] > 0:
        stock[I-1][J-1] -= 1
        vendas += 1
print(vendas)