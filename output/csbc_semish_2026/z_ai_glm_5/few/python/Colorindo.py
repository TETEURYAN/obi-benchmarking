import sys
from collections import deque

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    iterator = iter(input_data)
    
    try:
        N = int(next(iterator))
        M = int(next(iterator))
        X = int(next(iterator))
        Y = int(next(iterator))
        K = int(next(iterator))
    except StopIteration:
        return

    # Grid initialization (1-based indexing)
    # 0: empty, 1: blocked, 2: visited
    # Dimensions N+1 rows, M+1 cols
    grid = [[0] * (M + 1) for _ in range(N + 1)]

    for _ in range(K):
        A = int(next(iterator))
        B = int(next(iterator))
        if 1 <= A <= N and 1 <= B <= M:
            grid[A][B] = 1

    # BFS setup
    # 8 directions: (dr, dc)
    directions = [(-1, -1), (-1, 0), (-1, 1),
                  (0, -1),           (0, 1),
                  (1, -1),  (1, 0),  (1, 1)]
    
    queue = deque()
    
    # Start position
    queue.append((X, Y))
    grid[X][Y] = 2
    count = 1
    
    while queue:
        r, c = queue.popleft()
        
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            
            if 1 <= nr <= N and 1 <= nc <= M:
                if grid[nr][nc] == 0:
                    grid[nr][nc] = 2
                    count += 1
                    queue.append((nr, nc))
                    
    print(count)

if __name__ == '__main__':
    solve()