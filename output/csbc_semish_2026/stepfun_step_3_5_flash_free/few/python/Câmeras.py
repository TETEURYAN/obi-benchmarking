import sys
from collections import deque

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    N = int(next(it))
    M = int(next(it))
    K = int(next(it))
    blocked = [[False] * M for _ in range(N)]
    for _ in range(K):
        c = int(next(it)) - 1
        l = int(next(it)) - 1
        d = next(it)
        if d == 'N':
            for row in range(0, l + 1):
                blocked[c][row] = True
        elif d == 'S':
            for row in range(l, M):
                blocked[c][row] = True
        elif d == 'L':
            for col in range(c, N):
                blocked[col][l] = True
        elif d == 'O':
            for col in range(0, c + 1):
                blocked[col][l] = True
    if blocked[0][0] or blocked[N-1][M-1]:
        print('N')
        return
    visited = [[False] * M for _ in range(N)]
    q = deque([(0, 0)])
    visited[0][0] = True
    dirs = [(0, -1), (0, 1), (1, 0), (-1, 0)]
    while q:
        x, y = q.popleft()
        if x == N-1 and y == M-1:
            print('S')
            return
        for dx, dy in dirs:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] and not blocked[nx][ny]:
                visited[nx][ny] = True
                q.append((nx, ny))
    print('N')

if __name__ == '__main__':
    main()