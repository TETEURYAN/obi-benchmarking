import sys

input_data = sys.stdin.read().split()
if not input_data:
    exit()

c = int(input_data[0])
queries = input_data[1:c+1]

stock = set()
manufactured = 0

for q in queries:
    if q in stock:
        stock.remove(q)
    else:
        stock.add(q)
        manufactured += 2

print(manufactured)