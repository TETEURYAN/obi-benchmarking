
import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return

    idx = 0
    L = int(data[idx])
    C = int(data[idx + 1])
    idx += 2
    A = int(data[idx])
    B = int(data[idx + 1])
    idx += 2

    grid = []
    for _ in range(L):
        row = list(map(int, data[idx:idx + C]))
        grid.append(row)
        idx += C

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    current_pos = (A - 1, B - 1)
    prev_pos = None

    while True:
        x, y = current_pos
        next_pos = None
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < L and 0 <= ny < C:
                if grid[nx][ny] == 1 and (nx, ny) != prev_pos:
                    if next_pos is None:
                        next_pos = (nx, ny)
                    else:
                        next_pos = None
                        break
        if next_pos is None:
            break
        prev_pos, current_pos = current_pos, next_pos

    print(current_pos[0] + 1, current_pos[1] + 1)

if __name__ == "__main__":
    main()
