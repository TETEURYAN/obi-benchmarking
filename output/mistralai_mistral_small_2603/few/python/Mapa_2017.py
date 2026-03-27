
import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return

    L = int(data[0])
    C = int(data[1])
    grid = data[2:2+L]

    start_i, start_j = -1, -1
    for i in range(L):
        for j in range(C):
            if grid[i][j] == 'o':
                start_i, start_j = i, j
                break
        if start_i != -1:
            break

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    current_i, current_j = start_i, start_j
    visited = set()
    visited.add((current_i, current_j))

    while True:
        count = 0
        next_i, next_j = -1, -1
        for di, dj in directions:
            ni, nj = current_i + di, current_j + dj
            if 0 <= ni < L and 0 <= nj < C:
                if (ni, nj) not in visited and grid[ni][nj] == 'H':
                    count += 1
                    next_i, next_j = ni, nj

        if count != 1:
            break

        visited.add((next_i, next_j))
        current_i, current_j = next_i, next_j

    print(current_i + 1, current_j + 1)

if __name__ == "__main__":
    main()
