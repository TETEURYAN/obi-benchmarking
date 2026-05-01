
def main():
    import sys
    data = sys.stdin.read().split()
    ptr = 0
    N = int(data[ptr])
    ptr += 1
    I = int(data[ptr])
    J = int(data[ptr + 1])
    ptr += 2

    grid = []
    for _ in range(N):
        row = list(map(int, data[ptr:ptr + N]))
        ptr += N
        grid.append(row)

    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    current_dir = 0
    x, y = I - 1, J - 1
    visited = [[False for _ in range(N)] for _ in range(N)]
    count = 0

    for _ in range(4):
        dx, dy = directions[current_dir]
        nx, ny = x + dx, y + dy
        if 0 <= nx < N and 0 <= ny < N:
            if grid[nx][ny] >= grid[x][y] and not visited[nx][ny]:
                visited[x][y] = True
                count += 1
                x, y = nx, ny
                current_dir = (current_dir + 1) % 4
            else:
                current_dir = (current_dir + 1) % 4
        else:
            current_dir = (current_dir + 1) % 4

    total = 0
    for i in range(N):
        for j in range(N):
            if visited[i][j]:
                total += 1

    print(total)

if __name__ == "__main__":
    main()
