import sys

data = sys.stdin.read().split()
idx = 0
M = int(data[idx]); idx += 1
N = int(data[idx]); idx += 1

stock = []
for i in range(M):
    row = []
    for j in range(N):
        row.append(int(data[idx])); idx += 1
    stock.append(row)

P = int(data[idx]); idx += 1

sold = 0
for _ in range(P):
    I = int(data[idx]) - 1; idx += 1
    J = int(data[idx]) - 1; idx += 1
    if stock[I][J] > 0:
        stock[I][J] -= 1
        sold += 1

print(sold)