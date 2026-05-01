import sys
from collections import deque

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    n, m = data[0], data[1]
    vals = data[2:]

    grid = [bytearray(vals[i*m:(i+1)*m]) for i in range(n)]
    manchas = 0

    for i in range(n):
        row = grid[i]
        for j in range(m):
            if row[j] == 1:
                manchas += 1
                row[j] = 0
                q = deque([(i, j)])

                while q:
                    x, y = q.popleft()

                    nx = x - 1
                    if nx >= 0 and grid[nx][y] == 1:
                        grid[nx][y] = 0
                        q.append((nx, y))

                    nx = x + 1
                    if nx < n and grid[nx][y] == 1:
                        grid[nx][y] = 0
                        q.append((nx, y))

                    ny = y - 1
                    if ny >= 0 and grid[x][ny] == 1:
                        grid[x][ny] = 0
                        q.append((x, ny))

                    ny = y + 1
                    if ny < m and grid[x][ny] == 1:
                        grid[x][ny] = 0
                        q.append((x, ny))

    print(manchas)

if __name__ == "__main__":
    main()