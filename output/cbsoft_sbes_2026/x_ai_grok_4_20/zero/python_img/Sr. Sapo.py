
import sys
from collections import deque

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
start = (SC, SL)

RC = int(data[index])
index += 1
RL = int(data[index])
index += 1
goal = (RC, RL)

directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def can_reach():
    if start == goal:
        return True
    visited = set()
    queue = deque([start])
    visited.add(start)
    
    while queue:
        x, y = queue.popleft()
        for dx, dy in directions:
            for dist in range(1, 4):
                nx = x + dx * dist
                ny = y + dy * dist
                if 1 <= nx <= N and 1 <= ny <= M and (nx, ny) in stones and (nx, ny) not in visited:
                    if (nx, ny) == goal:
                        return True
                    visited.add((nx, ny))
                    queue.append((nx, ny))
    return False

if can_reach():
    print('S')
else:
    print('N')
