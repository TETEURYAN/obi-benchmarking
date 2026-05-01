
import sys

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    N = int(input_data[0])
    
    grid = []
    idx = 1
    for i in range(N):
        row = []
        for j in range(N):
            row.append(int(input_data[idx]))
            idx += 1
        grid.append(row)
        
    for i in range(1, N):
        for j in range(1, N):
            s = grid[i][j-1] + grid[i-1][j-1] + grid[i-1][j]
            if s >= 2:
                grid[i][j] = 0
            else:
                grid[i][j] = 1
                
    print(grid[N-1][N-1])

if __name__ == '__main__':
    main()
