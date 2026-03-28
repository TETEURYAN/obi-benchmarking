import sys
import heapq

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    L = int(next(it))
    C = int(next(it))
    K = int(next(it))
    grid = []
    for _ in range(L):
        row = [int(next(it)) for _ in range(C)]
        grid.append(row)
    
    INF = 10**18
    dist = [[INF] * C for _ in range(L)]
    dist[0][0] = 0
    heap = [(0, 0, 0)]
    
    while heap:
        t, i, j = heapq.heappop(heap)
        if t != dist[i][j]:
            continue
        for di, dj in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            ni, nj = i + di, j + dj
            if not (0 <= ni < L and 0 <= nj < C):
                continue
            if grid[ni][nj] == -1:
                novo = t + 1
            else:
                if grid[i][j] == -1:
                    s = (t + 1) % K
                    w = (grid[ni][nj] - s) % K
                    novo = t + 1 + w
                else:
                    if (grid[i][j] + 1) % K == grid[ni][nj]:
                        novo = t + 1
                    else:
                        continue
            if novo < dist[ni][nj]:
                dist[ni][nj] = novo
                heapq.heappush(heap, (novo, ni, nj))
    
    ans = dist[L-1][C-1]
    print(-1 if ans == INF else ans)

if __name__ == "__main__":
    main()