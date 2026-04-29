import sys

data = list(map(int, sys.stdin.read().split()))
n = data[0]
divisoes = data[1:1+n]

estoque = sum(x - 1 for x in divisoes)
print(estoque)