import sys

data = sys.stdin.read().split()
n = int(data[0])
idx = 1
min_price = float('inf')
for _ in range(n):
    p = float(data[idx])
    g = int(data[idx+1])
    idx += 2
    price_per_kg = p / g * 1000
    if price_per_kg < min_price:
        min_price = price_per_kg
print(f"{min_price:.2f}")