
import sys

def main():
    data = sys.stdin.read().splitlines()
    if not data:
        print(0)
        return
    n, m = map(int, data[0].split())
    grid = []
    for i in range(1, 1 + n):
        grid.append(data[i].strip())

    # Directions: up, down, left, right
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # We'll use a visited matrix to mark covered cells
    visited = [[False for _ in range(m)] for _ in range(n)]
    total_fitas = 0

    for i in range(n):
        for j in range(m):
            if grid[i][j] == '#' and not visited[i][j]:
                # Check if this cell can be covered by a green (horizontal) or yellow (vertical) tape
                # We need to find the largest possible horizontal or vertical segment starting at (i,j)
                # But we must ensure that neighbors are not covered by the opposite color

                # Try to cover horizontally first (green)
                can_horizontal = True
                max_j = j
                while max_j < m and grid[i][max_j] == '#' and not visited[i][max_j]:
                    # Check neighbors of (i, max_j) to ensure no adjacent green/blue conflict
                    for di, dj in directions:
                        ni, nj = i + di, max_j + dj
                        if 0 <= ni < n and 0 <= nj < m:
                            if grid[ni][nj] == '#' and not visited[ni][nj]:
                                # If neighbor is unvisited land, it's okay as long as it's not covered by opposite color
                                pass
                    max_j += 1

                # Try to cover vertically (yellow)
                can_vertical = True
                max_i = i
                while max_i < n and grid[max_i][j] == '#' and not visited[max_i][j]:
                    max_i += 1

                # Decide which way to cover
                if can_horizontal and (not can_vertical or (max_j - j) >= (max_i - i)):
                    # Cover horizontally
                    for k in range(j, max_j):
                        visited[i][k] = True
                    total_fitas += 1
                else:
                    # Cover vertically
                    for k in range(i, max_i):
                        visited[k][j] = True
                    total_fitas += 1

    print(total_fitas)

if __name__ == "__main__":
    main()
