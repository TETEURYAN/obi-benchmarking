import sys

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    
    grid = []
    idx = 1
    for _ in range(n):
        grid.append([int(x) for x in input_data[idx:idx+n]])
        idx += n
        
    for i in range(1, n):
        for j in range(1, n):
            total = grid[i][j-1] + grid[i-1][j-1] + grid[i-1][j]
            grid[i][j] = 1 if total <= 1 else 0
            
    print(grid[n-1][n-1])

if __name__ == '__main__':
    main()