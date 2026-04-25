
import sys

def main():
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
    visited = [[False for _ in range(N)] for _ in range(N)]
    count = 0

    def dfs(i, j, current_dir, steps_left):
        nonlocal count
        if steps_left == 0:
            return
        ni = i + directions[current_dir][0]
        nj = j + directions[current_dir][1]
        if 0 <= ni < N and 0 <= nj < N:
            if grid[ni][nj] >= grid[i][j] and not visited[ni][nj]:
                visited[ni][nj] = True
                count += 1
                dfs(ni, nj, current_dir, steps_left - 1)
                visited[ni][nj] = False
        dfs(i, j, (current_dir + 1) % 4, steps_left - 1)

    visited[I][J] = True
    count += 1
    for _ in range(4):
        dfs(I, J, 0, 4)
        I = I + directions[0][0]
        J = J + directions[0][1]
        if 0 <= I < N and 0 <= J < N:
            if not visited[I][J]:
                visited[I][J] = True
                count += 1

    print(count)

if __name__ == "__main__":
    main()
