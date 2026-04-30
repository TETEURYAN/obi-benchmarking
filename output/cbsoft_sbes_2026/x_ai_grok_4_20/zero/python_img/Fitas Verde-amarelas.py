
import sys
from collections import deque

input = sys.stdin.read
data = input().split()

N = int(data[0])
M = int(data[1])
grid = []
index = 2
for i in range(N):
    row = data[index]
    grid.append(list(row))
    index += 1

directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def is_land(i, j):
    return 0 <= i < N and 0 <= j < M and grid[i][j] == '#'

visited = [[False] * M for _ in range(N)]
components = []

for i in range(N):
    for j in range(M):
        if grid[i][j] == '#' and not visited[i][j]:
            component = []
            q = deque([(i, j)])
            visited[i][j] = True
            while q:
                x, y = q.popleft()
                component.append((x, y))
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if is_land(nx, ny) and not visited[nx][ny]:
                        visited[nx][ny] = True
                        q.append((nx, ny))
            components.append(component)

def can_connect_horizontally(c1, c2):
    for x1, y1 in c1:
        for x2, y2 in c2:
            if x1 == x2 and abs(y1 - y2) == 1:
                return True
    return False

def can_connect_vertically(c1, c2):
    for x1, y1 in c1:
        for x2, y2 in c2:
            if y1 == y2 and abs(x1 - x2) == 1:
                return True
    return False

K = len(components)
if K == 0:
    print(0)
    sys.exit(0)

adj = [[] for _ in range(K)]
for i in range(K):
    for j in range(i + 1, K):
        if can_connect_horizontally(components[i], components[j]):
            adj[i].append((j, 0))
            adj[j].append((i, 0))
        if can_connect_vertically(components[i], components[j]):
            adj[i].append((j, 1))
            adj[j].append((i, 1))

color = [-1] * K
groups = [[], []]
valid = True

for start in range(K):
    if color[start] != -1:
        continue
    q = deque([start])
    color[start] = 0
    groups[0].append(start)
    while q:
        u = q.popleft()
        for v, etype in adj[u]:
            expected_color = etype
            if color[v] == -1:
                color[v] = expected_color
                groups[expected_color].append(v)
                q.append(v)
            elif color[v] != expected_color:
                valid = False
                break
        if not valid:
            break
    if not valid:
        break

if not valid:
    print(0)
    sys.exit(0)

def count_segments(group, is_horizontal):
    if not group:
        return 0
    covered = [[False] * M for _ in range(N)]
    for cid in group:
        for x, y in components[cid]:
            covered[x][y] = True
    count = 0
    if is_horizontal:
        for i in range(N):
            j = 0
            while j < M:
                if covered[i][j]:
                    count += 1
                    while j < M and covered[i][j]:
                        j += 1
                else:
                    j += 1
    else:
        for j in range(M):
            i = 0
            while i < N:
                if covered[i][j]:
                    count += 1
                    while i < N and covered[i][j]:
                        i += 1
                else:
                    i += 1
    return count

ans = count_segments(groups[0], True) + count_segments(groups[1], False)
print(ans)
