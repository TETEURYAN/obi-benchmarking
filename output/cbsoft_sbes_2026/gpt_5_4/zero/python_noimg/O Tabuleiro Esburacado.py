import sys

data = list(map(int, sys.stdin.read().split()))
n = data[0]
moves = data[1:]

# Mapeamento dos movimentos 1..8 conforme a figura do problema
delta = {
    1: (1, 2),
    2: (2, 1),
    3: (2, -1),
    4: (1, -2),
    5: (-1, -2),
    6: (-2, -1),
    7: (-2, 1),
    8: (-1, 2),
}

holes = {(1, 3), (2, 3), (2, 5), (5, 4)}

x, y = 4, 3
count = 0

for m in moves:
    dx, dy = delta[m]
    x += dx
    y += dy
    count += 1
    if (x, y) in holes:
        break

print(count)