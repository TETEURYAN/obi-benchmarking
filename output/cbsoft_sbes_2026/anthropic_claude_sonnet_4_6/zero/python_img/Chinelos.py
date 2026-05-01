n = int(input())
stock = []
for _ in range(n):
    stock.append(int(input()))

p = int(input())
sold = 0
for _ in range(p):
    size = int(input())
    idx = size - 1
    if stock[idx] > 0:
        stock[idx] -= 1
        sold += 1

print(sold)