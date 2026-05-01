import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    N = int(input_data[0])
    I = int(input_data[1]) - 1
    J = int(input_data[2]) - 1
    
    grid = []
    idx = 3
    for _ in range(N):
        row = []
        for _ in range(N):
            row.append(int(input_data[idx]))
            idx += 1
        grid.append(row)
        
    visited = [[False] * N for _ in range(N)]
    
    stack = [(I, J)]
    visited[I][J] = True
    
    ans = 0
    while stack:
        r, c = stack.pop()
        ans += 1
        
        val = grid[r][c]
        
        for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < N and 0 <= nc < N:
                if not visited[nr][nc] and grid[nr][nc] >= val:
                    visited[nr][nc] = True
                    stack.append((nr, nc))
                    
    print(ans)

if __name__ == '__main__':
    solve()