
import sys

def main():
    M = int(sys.stdin.readline())
    grid = []
    for _ in range(M):
        line = sys.stdin.readline().strip()
        grid.append(line)

    A, B = map(int, sys.stdin.readline().split())
    A -= 1
    B -= 1

    visited = [[False for _ in range(M)] for _ in range(M)]
    time = 0
    x_pos = -1
    y_pos = -1

    for i in range(M):
        for j in range(M):
            if grid[i][j] == 'X':
                x_pos = i
                y_pos = j
                break
        if x_pos != -1:
            break

    current_i, current_j = A, B
    while True:
        if current_i == x_pos and current_j == y_pos:
            print(time)
            return

        if visited[current_i][current_j]:
            print(0)
            return

        visited[current_i][current_j] = True

        cell = grid[current_i][current_j]
        if cell == 'N':
            next_i = current_i - 1
            next_j = current_j
        elif cell == 'S':
            next_i = current_i + 1
            next_j = current_j
        elif cell == 'L':
            next_i = current_i
            next_j = current_j + 1
        elif cell == 'O':
            next_i = current_i
            next_j = current_j - 1

        if next_i < 0 or next_i >= M or next_j < 0 or next_j >= M:
            print(-1)
            return

        time += 1
        current_i, current_j = next_i, next_j

if __name__ == "__main__":
    main()
