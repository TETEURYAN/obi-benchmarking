import sys

data = list(map(int, sys.stdin.read().split()))
if not data:
    sys.exit()

n, c, m = data[0], data[1], data[2]
carimbadas = set(data[3:3 + c])
compradas = set(data[3 + c:3 + c + m])

faltam = 0
for x in carimbadas:
    if x not in compradas:
        faltam += 1

print(faltam)