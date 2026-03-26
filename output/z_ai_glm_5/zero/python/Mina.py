
import sys
from collections import deque

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    iterator = iter(input_data)
    try:
        N = int(next(iterator))
    except StopIteration:
        return

    grid = []
    for _ in range(N):
        row = []
        for _ in range(N):
            row.append(int(next(iterator)))
        grid.append(row)

    # 0-1 BFS
    # dist[r][c] stores the minimum number of blocked squares to reach (r, c)
    dist = [[float('inf')] * N for _ in range(N)]
    dq = deque()
    
    # Start position (0, 0). The problem guarantees it's not blocked (0).
    dist[0][0] = grid[0][0]
    dq.append((0, 0))
    
    moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    
    while dq:
        r, c = dq.popleft()
        
        # If we reached the target, since 0-1 BFS explores in order of cost,
        # the first time we reach the destination is the minimum cost.
        if r == N - 1 and c == N - 1:
            print(dist[r][c])
            return

        for dr, dc in moves:
            nr, nc = r + dr, c + dc
            
            if 0 <= nr < N and 0 <= nc < N:
                cost = grid[nr][nc]
                new_dist = dist[r][c] + cost
                
                if new_dist < dist[nr][nc]:
                    dist[nr][nc] = new_dist
                    if cost == 0:
                        dq.appendleft((nr, nc))
                    else:
                        dq.append((nr, nc))

if __name__ == '__main__':
    solve()
