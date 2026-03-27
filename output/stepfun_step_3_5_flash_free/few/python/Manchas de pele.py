import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    n = int(data[0])
    m = int(data[1])
    grid = []
    idx = 2
    for i in range(n):
        row = list(map(int, data[idx:idx+m]))
        grid.append(row)
        idx += m

    count = 0
    directions = [(1,0), (-1,0), (0,1), (0,-1)]
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1:
                count += 1
                stack = [(i, j)]
                grid[i][j] = 0
                while stack:
                    x, y = stack.pop()
                    for dx, dy in directions:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] == 1:
                            grid[nx][ny] = 0
                            stack.append((nx, ny))
    print(count)

if __name__ == "__main__":
    main()