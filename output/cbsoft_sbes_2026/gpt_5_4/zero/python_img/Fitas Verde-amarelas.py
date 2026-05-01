import sys

def main():
    input = sys.stdin.readline
    N, M = map(int, input().split())
    grid = [input().strip() for _ in range(N)]

    visited = [bytearray(M) for _ in range(N)]
    ans = 0

    for i in range(N):
        row = grid[i]
        for j in range(M):
            if row[j] == '#' and not visited[i][j]:
                stack = [(i, j)]
                visited[i][j] = 1
                cells = []
                rows = set()
                cols = set()

                while stack:
                    x, y = stack.pop()
                    cells.append((x, y))
                    rows.add(x)
                    cols.add(y)

                    nx = x - 1
                    if nx >= 0 and grid[nx][y] == '#' and not visited[nx][y]:
                        visited[nx][y] = 1
                        stack.append((nx, y))
                    nx = x + 1
                    if nx < N and grid[nx][y] == '#' and not visited[nx][y]:
                        visited[nx][y] = 1
                        stack.append((nx, y))
                    ny = y - 1
                    if ny >= 0 and grid[x][ny] == '#' and not visited[x][ny]:
                        visited[x][ny] = 1
                        stack.append((x, ny))
                    ny = y + 1
                    if ny < M and grid[x][ny] == '#' and not visited[x][ny]:
                        visited[x][ny] = 1
                        stack.append((x, ny))

                if len(rows) == 1 or len(cols) == 1:
                    ans += 1
                else:
                    ans += min(len(rows), len(cols))

    print(ans)

if __name__ == "__main__":
    main()
