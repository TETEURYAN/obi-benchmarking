
import sys

input = sys.stdin.read
data = input().split()

N = int(data[0])
points = set()
duplicate = False
index = 1

for i in range(N):
    x = int(data[index])
    y = int(data[index + 1])
    index += 2
    coord = (x, y)
    if coord in points:
        duplicate = True
    else:
        points.add(coord)

print(1 if duplicate else 0)
