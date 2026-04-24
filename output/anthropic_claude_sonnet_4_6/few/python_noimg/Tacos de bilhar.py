import sys

data = sys.stdin.read().split()
c = int(data[0])
queries = data[1:c+1]

stock = set()
fabricated = 0

for q in queries:
    length = int(q)
    if length in stock:
        stock.remove(length)
    else:
        fabricated += 2

print(fabricated)