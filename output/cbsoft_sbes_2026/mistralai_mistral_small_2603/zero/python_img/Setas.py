
def main():
    import sys
    data = sys.stdin.read().splitlines()
    if not data:
        print(0)
        return
    n = int(data[0])
    grid = []
    for i in range(1, n+1):
        grid.append(data[i].strip())

    safe = [[False] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            x, y = i, j
            visited = set()
            path = []
            while True:
                if (x, y) in visited:
                    idx = path.index((x, y))
                    cycle = path[idx:]
                    for (cx, cy) in cycle:
                        safe[cx][cy] = True
                    break
                if x < 0 or x >= n or y < 0 or y >= n:
                    break
                visited.add((x, y))
                path.append((x, y))
                cell = grid[x][y]
                if cell == '>':
                    y += 1
                elif cell == '<':
                    y -= 1
                elif cell == 'V':
                    x += 1
                elif cell == 'A':
                    x -= 1

    count = 0
    for i in range(n):
        for j in range(n):
            if safe[i][j]:
                count += 1
    print(count)

if __name__ == "__main__":
    main()
