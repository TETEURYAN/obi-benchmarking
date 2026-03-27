
import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return

    n = int(data[0])
    grid = []
    index = 1
    for i in range(n):
        row = list(map(int, data[index:index+n]))
        grid.append(row)
        index += n

    for i in range(1, n):
        for j in range(1, n):
            if grid[i][j] == 9:
                white = 0
                black = 0
                if grid[i][j-1] == 0:
                    white += 1
                else:
                    black += 1
                if grid[i-1][j-1] == 0:
                    white += 1
                else:
                    black += 1
                if grid[i-1][j] == 0:
                    white += 1
                else:
                    black += 1
                if black > white:
                    grid[i][j] = 0
                else:
                    grid[i][j] = 1

    print(grid[n-1][n-1])

if __name__ == "__main__":
    main()
