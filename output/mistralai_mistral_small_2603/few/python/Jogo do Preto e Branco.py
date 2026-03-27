
import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        print(0)
        return

    idx = 0
    L = int(data[idx])
    C = int(data[idx+1])
    idx += 2
    P = int(data[idx])
    idx += 1

    black = set()
    for _ in range(P):
        x = int(data[idx])
        y = int(data[idx+1])
        black.add((x, y))
        idx += 2

    max_white = 0
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for i in range(1, L+1):
        for j in range(1, C+1):
            if (i, j) in black:
                continue
            has_black_neighbor = False
            for dx, dy in directions:
                ni, nj = i + dx, j + dy
                if 1 <= ni <= L and 1 <= nj <= C:
                    if (ni, nj) in black:
                        has_black_neighbor = True
                        break
            if has_black_neighbor:
                valid = True
                for dx, dy in directions:
                    ni, nj = i + dx, j + dy
                    if 1 <= ni <= L and 1 <= nj <= C:
                        if (ni, nj) not in black and (ni, nj) != (i, j):
                            valid = False
                            break
                if valid:
                    max_white += 1

    print(max_white)

if __name__ == "__main__":
    main()
