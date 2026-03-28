import sys
from collections import deque

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    N = int(next(it))
    M = int(next(it))
    X = int(next(it))
    Y = int(next(it))
    K = int(next(it))
    
    blocked = [[False] * (M + 1) for _ in range(N + 1)]
    for _ in range(K):
        a = int(next(it))
        b = int(next(it))
        blocked[a][b] = True
    
    visited = [[False] * (M + 1) for _ in range(N + 1)]
    q = deque()
    q.append((X, Y))
    visited[X][Y] = True
    count = 0
    while q:
        i, j = q.popleft()
        count += 1
        for di in (-1, 0, 1):
            for dj in (-1, 0, 1):
                if di == 0 and dj == 0:
                    continue
                ni = i + di
                nj = j + dj
                if 1 <= ni <= N and 1 <= nj <= M:
                    if not visited[ni][nj] and not blocked[ni][nj]:
                        visited[ni][nj] = True
                        q.append((ni, nj))
    print(count)

if __name__ == "__main__":
    main()