import sys

input_data = sys.stdin.read().split()
if not input_data:
    exit()

n = int(input_data[0])
stocks = [0] * (n + 1)
for i in range(1, n + 1):
    stocks[i] = int(input_data[i])

p = int(input_data[n + 1])
sold = 0
for i in range(n + 2, n + 2 + p):
    size = int(input_data[i])
    if stocks[size] > 0:
        stocks[size] -= 1
        sold += 1

print(sold)