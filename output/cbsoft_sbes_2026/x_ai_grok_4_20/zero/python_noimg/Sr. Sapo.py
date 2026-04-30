
from collections import deque
import sys

input = sys.stdin.read
data = input().split()

index = 0
N = int(data[index])
index += 1
M = int(data[index])
index += 1
P = int(data[index])
index += 1

stones = set()
for _ in range(P):
    C = int(data[index])
    index += 1
    L = int(data[index])
    index += 1
    stones.add((C, L))

SC = int(data[index])
index += 1
SL = int(data[index])
index += 1
RC = int(data[index])
index += 1
RL = int(data[index])

start = (SC, SL)
target = (RC, RL)

directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

visited = set()
queue = deque([start])
visited.add(start)

while queue:
    x, y = queue.popleft()
    if (x, y) == target:
        print('S')
        sys.exit(0)
    
    for dx, dy in directions:
        for dist in range(1, 4):
            nx = x + dx * dist
            ny = y + dy * dist
            if 1 <= nx <= N and 1 <= ny <= M and (nx, ny) in stones and (nx, ny) not in visited:
                visited.add((nx, ny))
                queue.append((nx, ny))

print('N')
