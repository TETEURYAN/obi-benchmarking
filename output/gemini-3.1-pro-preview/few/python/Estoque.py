import sys

input_data = sys.stdin.read().split()
if not input_data:
    exit()

m = int(input_data[0])
n = int(input_data[1])

inventory = []
idx = 2
for _ in range(m):
    inventory.append([int(x) for x in input_data[idx:idx+n]])
    idx += n

p = int(input_data[idx])
idx += 1

sales = 0
for _ in range(p):
    i = int(input_data[idx]) - 1
    j = int(input_data[idx+1]) - 1
    if inventory[i][j] > 0:
        inventory[i][j] -= 1
        sales += 1
    idx += 2

print(sales)