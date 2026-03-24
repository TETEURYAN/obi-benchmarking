import sys

data = list(map(int, sys.stdin.read().split()))
if not data:
    sys.exit()

n = data[0]
points = []
idx = 1
for _ in range(n):
    x = data[idx]
    y = data[idx + 1]
    points.append((x, y))
    idx += 2
A = data[idx]
limit = A * A

in_mst = [False] * n
dist = [10**18] * n
dist[0] = 0

for _ in range(n):
    u = -1
    best = 10**18
    for i in range(n):
        if not in_mst[i] and dist[i] < best:
            best = dist[i]
            u = i

    in_mst[u] = True
    ux, uy = points[u]

    for v in range(n):
        if not in_mst[v]:
            vx, vy = points[v]
            dx = ux - vx
            dy = uy - vy
            d2 = dx * dx + dy * dy
            if d2 < dist[v]:
                dist[v] = d2

for i in range(1, n):
    if dist[i] > limit:
        print("N")
        break
else:
    print("S")