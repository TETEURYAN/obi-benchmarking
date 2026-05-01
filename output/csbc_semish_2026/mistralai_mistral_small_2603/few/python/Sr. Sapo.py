
import sys
from collections import deque

def main():
    data = sys.stdin.read().split()
    if not data:
        return

    idx = 0
    N = int(data[idx])
    M = int(data[idx+1])
    idx += 2
    P = int(data[idx])
    idx += 1

    stones = set()
    for _ in range(P):
        c = int(data[idx])
        l = int(data[idx+1])
        stones.add((c, l))
        idx += 2

    Sc = int(data[idx])
    SL = int(data[idx+1])
    idx += 2

    Rc = int(data[idx])
    RL = int(data[idx+1])

    if (Sc, SL) == (Rc, RL):
        print('S')
        return

    visited = set()
    queue = deque()
    queue.append((Sc, SL))
    visited.add((Sc, SL))

    directions = [(0, 1), (1, 0), (0, -1), (-1, 0),
                  (1, 1), (1, -1), (-1, 1), (-1, -1)]

    while queue:
        x, y = queue.popleft()
        if x == Rc and y == RL:
            print('S')
            return

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 1 <= nx <= N and 1 <= ny <= M:
                if (nx, ny) in stones and (nx, ny) not in visited:
                    visited.add((nx, ny))
                    queue.append((nx, ny))

    print('N')

if __name__ == "__main__":
    main()
