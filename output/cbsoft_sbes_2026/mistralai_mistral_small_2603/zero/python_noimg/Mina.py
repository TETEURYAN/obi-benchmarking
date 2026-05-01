
import heapq

def main():
    N = int(input())
    grid = []
    for _ in range(N):
        row = list(map(int, input().split()))
        grid.append(row)

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    INF = float('inf')
    dist = [[INF] * N for _ in range(N)]
    dist[0][0] = grid[0][0]
    heap = []
    heapq.heappush(heap, (dist[0][0], 0, 0))

    while heap:
        current_dist, i, j = heapq.heappop(heap)
        if i == N - 1 and j == N - 1:
            print(current_dist)
            return
        if current_dist > dist[i][j]:
            continue
        for di, dj in directions:
            ni, nj = i + di, j + dj
            if 0 <= ni < N and 0 <= nj < N:
                new_dist = current_dist + grid[ni][nj]
                if new_dist < dist[ni][nj]:
                    dist[ni][nj] = new_dist
                    heapq.heappush(heap, (new_dist, ni, nj))
    print(dist[N-1][N-1])

if __name__ == "__main__":
    main()
