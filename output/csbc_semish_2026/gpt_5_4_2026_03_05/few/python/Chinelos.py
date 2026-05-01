import sys

data = sys.stdin.read().split()
if not data:
    sys.exit()

idx = 0
n = int(data[idx])
idx += 1

stock = [0] * (n + 1)
for i in range(1, n + 1):
    stock[i] = int(data[idx])
    idx += 1

p = int(data[idx])
idx += 1

sold = 0
for _ in range(p):
    size = int(data[idx])
    idx += 1
    if stock[size] > 0:
        stock[size] -= 1
        sold += 1

print(sold)