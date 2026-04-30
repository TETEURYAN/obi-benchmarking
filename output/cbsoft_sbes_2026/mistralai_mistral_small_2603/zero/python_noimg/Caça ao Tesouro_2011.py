
import sys

def main():
    data = sys.stdin.read().split()
    idx = 0
    N = int(data[idx])
    K = int(data[idx+1])
    idx += 2

    clues = []
    for _ in range(K):
        x = int(data[idx])
        y = int(data[idx+1])
        d = int(data[idx+2])
        clues.append((x, y, d))
        idx += 3

    possible_positions = set()
    for x in range(N):
        for y in range(N):
            possible_positions.add((x, y))

    for (x, y, d) in clues:
        new_positions = set()
        for (px, py) in possible_positions:
            if abs(px - x) + abs(py - y) == d:
                new_positions.add((px, py))
        possible_positions = new_positions
        if not possible_positions:
            break

    if len(possible_positions) == 1:
        (x, y) = possible_positions.pop()
        print(f"{x} {y}")
    else:
        print("-1 -1")

if __name__ == "__main__":
    main()
