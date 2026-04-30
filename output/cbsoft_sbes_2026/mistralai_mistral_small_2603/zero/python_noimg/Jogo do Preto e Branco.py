
import sys

def main():
    data = sys.stdin.read().split()
    idx = 0
    L = int(data[idx])
    idx += 1
    C = int(data[idx])
    idx += 1
    P = int(data[idx])
    idx += 1

    black_positions = set()
    for _ in range(P):
        x = int(data[idx])
        idx += 1
        y = int(data[idx])
        idx += 1
        black_positions.add((x, y))

    max_white = 0
    for i in range(1, L + 1):
        for j in range(1, C + 1):
            if (i, j) not in black_positions:
                has_black_neighbor = False
                for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    ni, nj = i + di, j + dj
                    if 1 <= ni <= L and 1 <= nj <= C:
                        if (ni, nj) in black_positions:
                            has_black_neighbor = True
                            break
                if has_black_neighbor:
                    max_white += 1
    print(max_white)

if __name__ == "__main__":
    main()
