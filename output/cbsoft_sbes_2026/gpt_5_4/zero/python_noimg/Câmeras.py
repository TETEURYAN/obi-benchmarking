import sys
from collections import deque

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return

    N, M, K = map(int, data[:3])
    idx = 3

    observado = [[False] * N for _ in range(M)]

    for _ in range(K):
        c = int(data[idx]) - 1
        l = int(data[idx + 1]) - 1
        d = data[idx + 2]
        idx += 3

        if d == 'N':
            for r in range(l, -1, -1):
                observado[r][c] = True
        elif d == 'S':
            for r in range(l, M):
                observado[r][c] = True
        elif d == 'L':
            for col in range(c, N):
                observado[l][col] = True
        else:  # 'O'
            for col in range(c, -1, -1):
                observado[l][col] = True

    if observado[0][0] or observado[M - 1][N - 1]:
        print('N')
        return

    visitado = [[False] * N for _ in range(M)]
    q = deque([(0, 0)])
    visitado[0][0] = True

    while q:
        r, c = q.popleft()
        if r == M - 1 and c == N - 1:
            print('S')
            return

        for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            nr, nc = r + dr, c + dc
            if 0 <= nr < M and 0 <= nc < N and not visitado[nr][nc] and not observado[nr][nc]:
                visitado[nr][nc] = True
                q.append((nr, nc))

    print('N')

if __name__ == "__main__":
    main()