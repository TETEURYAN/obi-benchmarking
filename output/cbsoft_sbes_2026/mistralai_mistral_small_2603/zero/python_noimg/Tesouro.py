
def main():
    import sys
    data = sys.stdin.read().splitlines()
    M = int(data[0])
    grid = []
    for i in range(1, M + 1):
        grid.append(data[i].strip())
    A, B = map(int, data[M + 1].split())
    A -= 1
    B -= 1

    directions = {'N': (-1, 0), 'S': (1, 0), 'L': (0, 1), 'O': (0, -1)}
    visited = [[False for _ in range(M)] for _ in range(M)]
    time = 0
    x_pos = -1
    y_pos = -1
    for i in range(M):
        for j in range(M):
            if grid[i][j] == 'X':
                x_pos = i
                y_pos = j
                break
        if x_pos != -1:
            break

    current_i, current_j = A, B
    while True:
        if current_i < 0 or current_i >= M or current_j < 0 or current_j >= M:
            print(-1)
            return
        if visited[current_i][current_j]:
            print(0)
            return
        if current_i == x_pos and current_j == y_pos:
            print(time)
            return
        visited[current_i][current_j] = True
        cell = grid[current_i][current_j]
        di, dj = directions[cell]
        current_i += di
        current_j += dj
        time += 1

if __name__ == "__main__":
    main()
