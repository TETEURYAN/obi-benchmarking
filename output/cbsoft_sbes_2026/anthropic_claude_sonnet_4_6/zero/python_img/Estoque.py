import sys
input = sys.stdin.readline

M, N = map(int, input().split())
stock = []
for _ in range(M):
    row = list(map(int, input().split()))
    stock.append(row)

P = int(input())
sold = 0
for _ in range(P):
    I, J = map(int, input().split())
    if stock[I-1][J-1] > 0:
        stock[I-1][J-1] -= 1
        sold += 1

print(sold)