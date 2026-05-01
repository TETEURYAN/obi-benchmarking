import sys

def main():
    data = sys.stdin.read().split()
    idx = 0
    M = int(data[idx]); idx += 1
    grid = []
    for i in range(M):
        grid.append(data[idx]); idx += 1
    A = int(data[idx]) - 1; idx += 1
    B = int(data[idx]) - 1; idx += 1
    
    # direction maps
    dr = {'N': -1, 'S': 1, 'L': 0, 'O': 0}
    dc = {'N': 0, 'S': 0, 'L': 1, 'O': -1}
    
    visited = {}
    r, c = A, B
    time = 0
    
    while True:
        # Check bounds
        if r < 0 or r >= M or c < 0 or c >= M:
            print(-1)
            return
        
        cell = grid[r][c]
        
        if cell == 'X':
            print(time)
            return
        
        if (r, c) in visited:
            print(0)
            return
        
        visited[(r, c)] = time
        
        nr = r + dr[cell]
        nc = c + dc[cell]
        time += 1
        r, c = nr, nc

main()