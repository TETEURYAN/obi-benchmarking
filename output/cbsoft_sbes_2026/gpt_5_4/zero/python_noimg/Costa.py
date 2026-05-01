import sys

def main():
    input = sys.stdin.readline
    m, n = map(int, input().split())
    grid = [input().strip() for _ in range(m)]

    coast = 0
    for i in range(m):
        row = grid[i]
        for j in range(n):
            if row[j] == '#':
                if i == 0 or grid[i - 1][j] == '.':
                    coast += 1
                if i == m - 1 or grid[i + 1][j] == '.':
                    coast += 1
                if j == 0 or row[j - 1] == '.':
                    coast += 1
                if j == n - 1 or row[j + 1] == '.':
                    coast += 1

    print(coast)

if __name__ == "__main__":
    main()