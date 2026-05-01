
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
        current_dist, x, y = heapq.heappop(heap)
        if x == N - 1 and y == N - 1:
            print(current_dist)
            return
        if current_dist > dist[x][y]:
            continue
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N:
                new_dist = current_dist + grid[nx][ny]
                if new_dist < dist[nx][ny]:
                    dist[nx][ny] = new_dist
                    heapq.heappush(heap, (new_dist, nx, ny))

if __name__ == "__main__":
    main()
