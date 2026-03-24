import sys

data = list(map(int, sys.stdin.read().split()))
if not data:
    sys.exit()

R, N = data[0], data[1]

min_price = {}

idx = 2
for _ in range(N):
    t = data[idx]
    p = data[idx + 1]
    idx += 2
    if t not in min_price or p < min_price[t]:
        min_price[t] = p

prices = sorted(min_price.values())

count = 0
spent = 0
for price in prices:
    if spent + price <= R:
        spent += price
        count += 1
    else:
        break

print(count)