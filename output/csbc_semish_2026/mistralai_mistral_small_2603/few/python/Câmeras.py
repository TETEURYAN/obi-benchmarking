
import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        print('N')
        return

    idx = 0
    N = int(data[idx])
    M = int(data[idx+1])
    K = int(data[idx+2])
    idx += 3

    cameras = []
    for _ in range(K):
        c = int(data[idx])
        l = int(data[idx+1])
        d = data[idx+2]
        cameras.append((c, l, d))
        idx += 3

    blocked = [[False] * (M + 1) for _ in range(N + 1)]

    for c, l, d in cameras:
        if d == 'N':
            for i in range(l, M + 1):
                blocked[c][i] = True
        elif d == 'S':
            for i in range(1, l + 1):
                blocked[c][i] = True
        elif d == 'L':
            for j in range(c, N + 1):
                blocked[j][l] = True
        elif d == 'O':
            for j in range(1, c + 1):
                blocked[j][l] = True

    if blocked[1][1] or blocked[N][M]:
        print('N')
        return

    visited = [[False] * (M + 1) for _ in range(N + 1)]
    from collections import deque
    q = deque()
    q.append((1, 1))
    visited[1][1] = True

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while q:
        x, y = q.popleft()
        if x == N and y == M:
            print('S')
            return

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 1 <= nx <= N and 1 <= ny <= M:
                if not visited[nx][ny] and not blocked[nx][ny]:
                    visited[nx][ny] = True
                    q.append((nx, ny))

    print('N')

if __name__ == '__main__':
    main()
