
import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        print('N')
        return

    n = int(data[0])
    points = []
    idx = 1
    for _ in range(n):
        x = int(data[idx])
        y = int(data[idx + 1])
        points.append((x, y))
        idx += 2

    A = int(data[idx])

    if n == 1:
        print('S')
        return

    from collections import deque
    visited = [False] * n
    queue = deque()
    queue.append(0)
    visited[0] = True
    count = 1

    while queue:
        u = queue.popleft()
        x1, y1 = points[u]
        for v in range(n):
            if not visited[v]:
                x2, y2 = points[v]
                dx = x1 - x2
                dy = y1 - y2
                distance_sq = dx * dx + dy * dy
                if distance_sq <= A * A:
                    visited[v] = True
                    count += 1
                    queue.append(v)

    print('S' if count == n else 'N')

if __name__ == "__main__":
    main()
