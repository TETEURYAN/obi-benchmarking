import sys
from collections import deque

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    N = int(input_data[0])
    F = input_data[1]
    
    grid = [list(row) for row in input_data[2:2+N]]
    
    if grid[0][0] <= F:
        queue = deque([(0, 0)])
        grid[0][0] = '*'
        
        while queue:
            r, c = queue.popleft()
            
            for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                nr, nc = r + dr, c + dc
                if 0 <= nr < N and 0 <= nc < N:
                    val = grid[nr][nc]
                    if val != '*' and val <= F:
                        grid[nr][nc] = '*'
                        queue.append((nr, nc))
                        
    for row in grid:
        sys.stdout.write("".join(row) + "\n")

if __name__ == '__main__':
    main()