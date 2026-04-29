import sys

data = list(map(int, sys.stdin.read().split()))
n = data[0]
moves = data[1:]

dx = [1, 2, 2, 1, -1, -2, -2, -1]
dy = [2, 1, -1, -2, -2, -1, 1, 2]

holes = {(1, 3), (2, 3), (2, 5), (5, 4)}

x, y = 4, 3
count = 0

for m in moves:
    x += dx[m - 1]
    y += dy[m - 1]
    count += 1
    if (x, y) in holes:
        break

print(count)