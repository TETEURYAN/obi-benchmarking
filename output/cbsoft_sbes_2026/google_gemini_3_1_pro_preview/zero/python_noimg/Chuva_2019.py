import sys
from collections import deque

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    N = int(input_data[0])
    M = int(input_data[1])
    
    grid = [list(row) for row in input_data[2:]]
    
    queue = deque()
    for j in range(M):
        if grid[0][j] == 'o':
            queue.append((0, j))
            break
            
    while queue:
        i, j = queue.popleft()
        
        if i + 1 < N:
            if grid[i+1][j] == '.':
                grid[i+1][j] = 'o'
                queue.append((i+1, j))
            elif grid[i+1][j] == '#':
                if j + 1 < M and grid[i][j+1] == '.':
                    grid[i][j+1] = 'o'
                    queue.append((i, j+1))
                if j - 1 >= 0 and grid[i][j-1] == '.':
                    grid[i][j-1] = 'o'
                    queue.append((i, j-1))
                    
    for row in grid:
        sys.stdout.write("".join(row) + "\n")

if __name__ == '__main__':
    main()