import sys

data = list(map(int, sys.stdin.read().split()))
if not data:
    sys.exit()

n, d = data[0], data[1]
pts = []
idx = 2
for _ in range(n):
    pts.append((data[idx], data[idx + 1]))
    idx += 2

d2 = d * d
visited = [False] * n
stack = [0]
visited[0] = True
count = 1

while stack:
    u = stack.pop()
    x1, y1 = pts[u]
    for v in range(n):
        if not visited[v]:
            x2, y2 = pts[v]
            dx = x1 - x2
            dy = y1 - y2
            if dx * dx + dy * dy <= d2:
                visited[v] = True
                stack.append(v)
                count += 1

print('S' if count == n else 'N')