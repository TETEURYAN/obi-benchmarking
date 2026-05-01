
def main():
    import sys
    N, S = map(int, sys.stdin.readline().split())
    if N == 1:
        print(S)
        return

    base = S // N
    remainder = S % N

    grid = [[0] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if i == j:
                grid[i][j] = base + remainder
            else:
                grid[i][j] = base

    for i in range(N):
        for j in range(N):
            if i != j:
                grid[i][j] += i + j

    for row in grid:
        print(' '.join(map(str, row)))

if __name__ == '__main__':
    main()
