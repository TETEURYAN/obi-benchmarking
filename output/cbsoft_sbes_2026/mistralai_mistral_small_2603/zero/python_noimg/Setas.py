
import sys

def main():
    data = sys.stdin.read().splitlines()
    if not data:
        print(0)
        return
    N = int(data[0])
    grid = []
    for i in range(1, N+1):
        grid.append(data[i].strip())

    directions = {
        'V': (1, 0),
        'A': (-1, 0),
        '<': (0, -1),
        '>': (0, 1)
    }

    safe = 0

    for i in range(N):
        for j in range(N):
            x, y = i, j
            visited = set()
            path = []
            while True:
                if (x, y) in visited:
                    break
                if x < 0 or x >= N or y < 0 or y >= N:
                    break
                visited.add((x, y))
                path.append((x, y))
                dx, dy = directions[grid[x][y]]
                x += dx
                y += dy

            if x >= 0 and x < N and y >= 0 and y < N:
                safe += 1

    print(safe)

if __name__ == "__main__":
    main()
