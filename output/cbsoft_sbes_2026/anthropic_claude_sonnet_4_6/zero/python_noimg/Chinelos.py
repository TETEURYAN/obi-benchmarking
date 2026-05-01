n = int(input())
stock = {}
for i in range(1, n + 1):
    stock[i] = int(input())

p = int(input())
sold = 0
for _ in range(p):
    size = int(input())
    if stock.get(size, 0) > 0:
        stock[size] -= 1
        sold += 1

print(sold)