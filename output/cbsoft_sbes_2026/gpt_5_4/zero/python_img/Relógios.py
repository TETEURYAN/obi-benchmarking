import sys
import heapq

def main():
    input = sys.stdin.readline
    L, C, K = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(L)]

    INF = 10**30
    dist = [[INF] * C for _ in range(L)]
    pq = []

    if grid[0][0] != 0:
        print(-1)
        return

    dist[0][0] = 0
    heapq.heappush(pq, (0, 0, 0))

    dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while pq:
        t, i, j = heapq.heappop(pq)
        if t != dist[i][j]:
            continue
        if i == L - 1 and j == C - 1:
            print(t)
            return

        cur = grid[i][j]

        if cur == -1:
            nt = t + 1
            if nt < dist[i][j]:
                dist[i][j] = nt
                heapq.heappush(pq, (nt, i, j))

        for di, dj in dirs:
            ni, nj = i + di, j + dj
            if not (0 <= ni < L and 0 <= nj < C):
                continue

            nxt = grid[ni][nj]

            if nxt == -1:
                nt = t + 1
            else:
                r = nxt
                nt = t + 1
                mod = nt % K
                if mod != r:
                    nt += (r - mod) % K

            if nt < dist[ni][nj]:
                dist[ni][nj] = nt
                heapq.heappush(pq, (nt, ni, nj))

    print(-1)

if __name__ == "__main__":
    main()
