import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    n = int(data[0])
    grid = []
    idx = 1
    for i in range(n):
        row = list(map(int, data[idx:idx+n]))
        idx += n
        grid.append(row)
    
    for i in range(1, n):
        for j in range(1, n):
            soma = grid[i-1][j] + grid[i][j-1] + grid[i-1][j-1]
            grid[i][j] = 1 if soma <= 1 else 0
    
    print(grid[n-1][n-1])

if __name__ == "__main__":
    main()