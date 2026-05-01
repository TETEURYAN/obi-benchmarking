
import sys
from collections import deque

def main():
    data = sys.stdin.read().split()
    if not data:
        return

    ptr = 0
    N = int(data[ptr])
    ptr += 1
    M = int(data[ptr])
    ptr += 1

    powers = []
    for _ in range(N):
        row = list(map(int, data[ptr:ptr+M]))
        ptr += M
        powers.append(row)

    total = N * M
    nodes = []
    for i in range(N):
        for j in range(M):
            nodes.append((powers[i][j], i, j))

    nodes.sort(reverse=True, key=lambda x: x[0])
    result = [[0] * M for _ in range(N)]
    visited = [[False] * M for _ in range(N)]
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for power, i, j in nodes:
        if visited[i][j]:
            continue
        queue = deque()
        queue.append((i, j))
        visited[i][j] = True
        component = []
        while queue:
            x, y = queue.popleft()
            component.append((x, y))
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] and powers[nx][ny] <= power:
                    visited[nx][ny] = True
                    queue.append((nx, ny))

        if not component:
            result[i][j] = power
            continue

        max_power = power
        current_power = power
        for x, y in component:
            if x == i and y == j:
                continue
            if powers[x][y] <= current_power:
                current_power += powers[x][y]
                if current_power > max_power:
                    max_power = current_power

        for x, y in component:
            result[x][y] = max_power

    for i in range(N):
        print(' '.join(map(str, result[i])))

if __name__ == "__main__":
    main()
