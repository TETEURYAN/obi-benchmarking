import sys

def main():
    input = sys.stdin.readline
    N, M = map(int, input().split())
    grid = [list(input().strip()) for _ in range(N)]

    changed = True
    while changed:
        changed = False
        for i in range(N):
            row = grid[i]
            for j in range(M):
                if row[j] != '.':
                    continue

                wet = False

                if i > 0 and grid[i - 1][j] == 'o':
                    wet = True
                elif j > 0 and row[j - 1] == 'o' and i + 1 < N and grid[i + 1][j - 1] == '#':
                    wet = True
                elif j + 1 < M and row[j + 1] == 'o' and i + 1 < N and grid[i + 1][j + 1] == '#':
                    wet = True

                if wet:
                    row[j] = 'o'
                    changed = True

    sys.stdout.write('\n'.join(''.join(row) for row in grid))

if __name__ == "__main__":
    main()
