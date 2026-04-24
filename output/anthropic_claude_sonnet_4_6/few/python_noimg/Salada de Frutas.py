import sys

data = sys.stdin.read().split()
R = int(data[0])
N = int(data[1])

min_price = {}
idx = 2
for _ in range(N):
    t = int(data[idx])
    p = int(data[idx+1])
    idx += 2
    if t not in min_price or p < min_price[t]:
        min_price[t] = p

prices = sorted(min_price.values())

total = 0
count = 0
for p in prices:
    if total + p <= R:
        total += p
        count += 1
    else:
        break

print(count)