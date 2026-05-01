
import sys

input = sys.stdin.read
data = input().split()

N = int(data[0])
moves = list(map(int, data[1:]))

holes = {(1,3), (2,3), (2,5), (5,4)}

dx = [0, -2, -1, 1, 2, 2, 1, -1, -2]
dy = [0, 1, 2, 2, 1, -1, -2, -2, -1]

x, y = 4, 3
count = 0

for m in moves:
    nx = x + dx[m]
    ny = y + dy[m]
    if (nx, ny) in holes:
        count += 1
        break
    x, y = nx, ny
    count += 1

print(count)
