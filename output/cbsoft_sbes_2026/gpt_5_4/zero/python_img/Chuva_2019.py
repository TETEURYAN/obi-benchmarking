import sys

def main():
    input = sys.stdin.readline
    N, M = map(int, input().split())
    grid = [list(input().strip()) for _ in range(N)]

    for i in range(N):
        if i == 0:
            continue
        if i % 2 == 1:
            for j in range(M):
                if grid[i][j] == '.':
                    if grid[i - 1][j] == 'o':
                        grid[i][j] = 'o'
        else:
            for j in range(M):
                if grid[i][j] == '.':
                    if grid[i - 1][j] == 'o':
                        grid[i][j] = 'o'
            for j in range(1, M):
                if grid[i][j] == '.' and grid[i][j - 1] == 'o' and grid[i - 1][j - 1] == '#':
                    grid[i][j] = 'o'
            for j in range(M - 2, -1, -1):
                if grid[i][j] == '.' and grid[i][j + 1] == 'o' and grid[i - 1][j + 1] == '#':
                    grid[i][j] = 'o'

    sys.stdout.write('\n'.join(''.join(row) for row in grid))

if __name__ == "__main__":
    main()
