
import sys

input = sys.stdin.read
data = input().split()

N = int(data[0])
K = int(data[1])

clues = []
index = 2
for i in range(K):
    X = int(data[index])
    Y = int(data[index + 1])
    D = int(data[index + 2])
    clues.append((X, Y, D))
    index += 3

possible = []
for x in range(N):
    for y in range(N):
        valid = True
        for cx, cy, cd in clues:
            dist = abs(x - cx) + abs(y - cy)
            if dist != cd:
                valid = False
                break
        if valid:
            possible.append((x, y))

if len(possible) == 1:
    print(possible[0][0], possible[0][1])
else:
    print(-1, -1)
