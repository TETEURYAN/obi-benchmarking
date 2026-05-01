
import sys

input = sys.stdin.read
data = input().split()

N = int(data[0])
raios = set()
duplicado = False
index = 1

for i in range(N):
    x = int(data[index])
    y = int(data[index + 1])
    coord = (x, y)
    if coord in raios:
        duplicado = True
    else:
        raios.add(coord)
    index += 2
    if duplicado and len(raios) > 10000:
        break

print(1 if duplicado else 0)
