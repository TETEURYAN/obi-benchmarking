
def main():
    import sys
    data = sys.stdin.read().splitlines()
    if not data:
        print(0)
        return
    M, N = map(int, data[0].split())
    grid = []
    for i in range(1, 1 + M):
        grid.append(data[i].strip())

    count = 0
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for i in range(M):
        for j in range(N):
            if grid[i][j] == '#':
                for di, dj in directions:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < M and 0 <= nj < N:
                        if grid[ni][nj] == '.':
                            count += 1
                            break
                    else:
                        count += 1
                        break
    print(count)

if __name__ == '__main__':
    main()
