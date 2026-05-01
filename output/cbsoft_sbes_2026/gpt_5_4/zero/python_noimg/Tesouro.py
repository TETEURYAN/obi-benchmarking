import sys

def main():
    input = sys.stdin.readline
    M = int(input())
    grid = [input().strip() for _ in range(M)]
    A, B = map(int, input().split())
    i, j = A - 1, B - 1

    visited = {}
    steps = 0

    while True:
        if i < 0 or i >= M or j < 0 or j >= M:
            print(-1)
            return

        if grid[i][j] == 'X':
            print(steps)
            return

        state = (i, j)
        if state in visited:
            print(0)
            return
        visited[state] = steps

        c = grid[i][j]
        if c == 'N':
            i -= 1
        elif c == 'S':
            i += 1
        elif c == 'L':
            j += 1
        else:  # 'O'
            j -= 1
        steps += 1

if __name__ == "__main__":
    main()
