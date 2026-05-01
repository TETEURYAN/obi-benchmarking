
def main():
    import sys
    data = sys.stdin.read().split()
    ptr = 0
    N = int(data[ptr])
    ptr += 1
    I = int(data[ptr]) - 1
    J = int(data[ptr+1]) - 1
    ptr += 2

    grid = []
    for _ in range(N):
        row = list(map(int, data[ptr:ptr+N]))
        ptr += N
        grid.append(row)

    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    current_dir = 0
    x, y = I, J
    raised = [[False for _ in range(N)] for __ in range(N)]

    for _ in range(4):
        dx, dy = directions[current_dir]
        nx, ny = x + dx, y + dy
        if 0 <= nx < N and 0 <= ny < N:
            if grid[nx][ny] >= grid[x][y] and not raised[nx][ny]:
                raised[x][y] = True
                x, y = nx, ny
                current_dir = (current_dir + 1) % 4
                continue
        current_dir = (current_dir + 1) % 4

    count = 0
    for i in range(N):
        for j in range(N):
            if raised[i][j]:
                count += 1
    print(count)

if __name__ == "__main__":
    main()
