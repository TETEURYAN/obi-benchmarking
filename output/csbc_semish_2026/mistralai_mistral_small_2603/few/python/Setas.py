
import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        print(0)
        return

    n = int(data[0])
    grid = data[1:n+1]

    directions = {
        'V': (1, 0),
        'A': (-1, 0),
        '<': (0, -1),
        '>': (0, 1)
    }

    safe = [[False for _ in range(n)] for _ in range(n)]
    count = 0

    for i in range(n):
        for j in range(n):
            if safe[i][j]:
                count += 1
                continue

            visited = set()
            current_i, current_j = i, j
            path = []

            while True:
                if (current_i, current_j) in visited:
                    if (current_i, current_j) in path:
                        idx = path.index((current_i, current_j))
                        for (x, y) in path[idx:]:
                            safe[x][y] = True
                        count += len(path) - idx
                    break

                if current_i < 0 or current_i >= n or current_j < 0 or current_j >= n:
                    break

                visited.add((current_i, current_j))
                path.append((current_i, current_j))

                di, dj = directions[grid[current_i][current_j]]
                current_i += di
                current_j += dj

    print(count)

if __name__ == "__main__":
    main()
