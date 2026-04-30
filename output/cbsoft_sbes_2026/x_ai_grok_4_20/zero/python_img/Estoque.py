
import sys

input = sys.stdin.read
data = input().split()

index = 0
M = int(data[index])
index += 1
N = int(data[index])
index += 1

stock = []
for i in range(M):
    row = []
    for j in range(N):
        row.append(int(data[index]))
        index += 1
    stock.append(row)

P = int(data[index])
index += 1

sold = 0
for k in range(P):
    I = int(data[index]) - 1
    index += 1
    J = int(data[index]) - 1
    index += 1
    if stock[I][J] > 0:
        stock[I][J] -= 1
        sold += 1

print(sold)
