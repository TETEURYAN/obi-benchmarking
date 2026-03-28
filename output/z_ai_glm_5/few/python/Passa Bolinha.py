import sys

sys.setrecursionlimit(20000)

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    iterator = iter(input_data)
    
    try:
        N = int(next(iterator))
        I = int(next(iterator))
        J = int(next(iterator))
    except StopIteration:
        return

    # Using 1-based indexing to match problem description
    grid = [[0] * (N + 1) for _ in range(N + 1)]
    
    for r in range(1, N + 1):
        for c in range(1, N + 1):
            grid[r][c] = int(next(iterator))
            
    visited = [[False] * (N + 1) for _ in range(N + 1)]
    
    # Directions: East, South, West, North
    # Corresponding to turning 90 degrees clockwise starting from North
    # North -> East -> South -> West -> North
    # Order of checks: East, South, West, North
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    def solve(r, c):
        visited[r][c] = True
        current_val = grid[r][c]
        
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            
            if 1 <= nr <= N and 1 <= nc <= N:
                if grid[nr][nc] >= current_val and not visited[nr][nc]:
                    solve(nr, nc)
                    
    solve(I, J)
    
    count = 0
    for r in range(1, N + 1):
        for c in range(1, N + 1):
            if visited[r][c]:
                count += 1
                
    print(count)

if __name__ == '__main__':
    main()