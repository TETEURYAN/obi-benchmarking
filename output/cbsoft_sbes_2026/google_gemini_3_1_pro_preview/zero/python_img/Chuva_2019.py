
import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    N = int(input_data[0])
    M = int(input_data[1])
    
    grid = [list(row) for row in input_data[2:]]
    
    stack = []
    for j in range(M):
        if grid[0][j] == 'o':
            stack.append((0, j))
            break
            
    while stack:
        r, c = stack.pop()
        
        if r + 1 < N:
            if grid[r+1][c] == '.':
                grid[r+1][c] = 'o'
                stack.append((r+1, c))
            elif grid[r+1][c] == '#':
                if c + 1 < M and grid[r][c+1] == '.':
                    grid[r][c+1] = 'o'
                    stack.append((r, c+1))
                if c - 1 >= 0 and grid[r][c-1] == '.':
                    grid[r][c-1] = 'o'
                    stack.append((r, c-1))

    for row in grid:
        sys.stdout.write("".join(row) + "\n")

if __name__ == '__main__':
    solve()
