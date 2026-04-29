import sys

data = list(map(int, sys.stdin.buffer.read().split()))
it = iter(data)

M = next(it)
N = next(it)

estoque = [[next(it) for _ in range(N)] for _ in range(M)]

P = next(it)
vendidas = 0

for _ in range(P):
    i = next(it) - 1
    j = next(it) - 1
    if estoque[i][j] > 0:
        estoque[i][j] -= 1
        vendidas += 1

print(vendidas)