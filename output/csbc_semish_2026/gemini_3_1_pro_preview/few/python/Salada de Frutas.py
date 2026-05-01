import sys

input_data = sys.stdin.read().split()
if not input_data:
    exit()

R = int(input_data[0])
N = int(input_data[1])

min_price = {}
idx = 2
for _ in range(N):
    t = int(input_data[idx])
    p = int(input_data[idx+1])
    if t not in min_price or p < min_price[t]:
        min_price[t] = p
    idx += 2

prices = sorted(min_price.values())

count = 0
for p in prices:
    if R >= p:
        R -= p
        count += 1
    else:
        break

print(count)