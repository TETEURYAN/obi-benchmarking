
import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return

    idx = 0
    M = int(data[idx])
    idx += 1

    grid = []
    for _ in range(M):
        row = data[idx]
        grid.append(row)
        idx += 1

    A = int(data[idx])
    B = int(data[idx + 1])

    directions = {
        'N': (-1, 0),
        'S': (1, 0),
        'L': (0, 1),
        'O': (0, -1)
    }

    visited = [[False for _ in range(M)] for _ in range(M)]
    time = 0
    current_i, current_j = A - 1, B - 1

    while True:
        if current_i < 0 or current_i >= M or current_j < 0 or current_j >= M:
            print(-1)
            return

        if grid[current_i][current_j] == 'X':
            print(time)
            return

        if visited[current_i][current_j]:
            print(0)
            return

        visited[current_i][current_j] = True
        direction = grid[current_i][current_j]
        di, dj = directions[direction]
        current_i += di
        current_j += dj
        time += 1

if __name__ == "__main__":
    main()
