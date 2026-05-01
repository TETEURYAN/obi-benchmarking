import sys

def main():
    input = sys.stdin.readline
    M = int(input())
    grid = [input().strip() for _ in range(M)]
    A, B = map(int, input().split())
    A -= 1
    B -= 1

    state = [[0] * M for _ in range(M)]  # 0=unvisited, 1=visiting, 2=done
    result = [[None] * M for _ in range(M)]  # distance, 0, or -1

    def nxt(i, j):
        c = grid[i][j]
        if c == 'N':
            return i - 1, j
        if c == 'S':
            return i + 1, j
        if c == 'L':
            return i, j + 1
        if c == 'O':
            return i, j - 1
        return None

    i, j = A, B
    path = []
    pos_in_path = {}

    while True:
        if not (0 <= i < M and 0 <= j < M):
            val = -1
            break

        if grid[i][j] == 'X':
            val = 0
            break

        if state[i][j] == 2:
            val = result[i][j]
            break

        if (i, j) in pos_in_path:
            val = 0
            break

        pos_in_path[(i, j)] = len(path)
        path.append((i, j))
        ni, nj = nxt(i, j)
        i, j = ni, nj

    for x, y in reversed(path):
        if val > 0 or val == 0 and grid[x][y] != 'X':
            if val != -1:
                val += 1
        state[x][y] = 2
        result[x][y] = val

    print(result[A][B])

if __name__ == "__main__":
    main()
