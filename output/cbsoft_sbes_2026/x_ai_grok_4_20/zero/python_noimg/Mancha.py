
import sys
from collections import deque

input = sys.stdin.read
data = input().splitlines()

N = int(data[0])
grid = data[1:1+N]

# Find all '*' positions
stars = []
for i in range(N):
    for j in range(N):
        if grid[i][j] == '*':
            stars.append((i, j))

if len(stars) < 2:
    print("S")
    sys.exit(0)

# Find one endpoint: farthest from arbitrary start
start = stars[0]
dist = [[-1] * N for _ in range(N)]
q = deque([start])
dist[start[0]][start[1]] = 0
farthest = start

while q:
    x, y = q.popleft()
    if dist[x][y] > dist[farthest[0]][farthest[1]]:
        farthest = (x, y)
    for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < N and 0 <= ny < N and grid[nx][ny] == '*' and dist[nx][ny] == -1:
            dist[nx][ny] = dist[x][y] + 1
            q.append((nx, ny))

# Now from farthest point, find the other endpoint and compute distances
A = farthest
distA = [[-1] * N for _ in range(N)]
q = deque([A])
distA[A[0]][A[1]] = 0
farthest2 = A
positions = []

while q:
    x, y = q.popleft()
    positions.append((x, y))
    if distA[x][y] > distA[farthest2[0]][farthest2[1]]:
        farthest2 = (x, y)
    for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < N and 0 <= ny < N and grid[nx][ny] == '*' and distA[nx][ny] == -1:
            distA[nx][ny] = distA[x][y] + 1
            q.append((nx, ny))

B = farthest2

# Compute distB from B
distB = [[-1] * N for _ in range(N)]
q = deque([B])
distB[B[0]][B[1]] = 0

while q:
    x, y = q.popleft()
    for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < N and 0 <= ny < N and grid[nx][ny] == '*' and distB[nx][ny] == -1:
            distB[nx][ny] = distB[x][y] + 1
            q.append((nx, ny))

# For every * point, check if distA[p] + distB[p] == distA[B]
diameter = distA[B[0]][B[1]]
is_regular = True
for x, y in positions:
    if distA[x][y] + distB[x][y] != diameter:
        is_regular = False
        break
    # Also check Manhattan condition via triangle inequality on grid
    # But the key property is that all points lie on some shortest path between A and B
    # Which is equivalent to the above sum equaling diameter

if is_regular:
    # Additional verification: the shape must be such that no "holes" or "detours"
    # But in grid with 4-connectivity, if all points are on geodesics between diameter ends,
    # and component is connected, then d(P,Q) == manhattan(P,Q) for all pairs
    # because any two points have a shortest path inside the "tube"
    print("S")
else:
    print("N")
