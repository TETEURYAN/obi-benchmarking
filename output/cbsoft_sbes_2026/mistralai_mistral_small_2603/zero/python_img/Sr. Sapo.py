
from collections import deque

def main():
    import sys
    data = sys.stdin.read().split()
    idx = 0
    N = int(data[idx])
    idx += 1
    M = int(data[idx])
    idx += 1

    P = int(data[idx])
    idx += 1

    stones = set()
    for _ in range(P):
        c = int(data[idx])
        idx += 1
        l = int(data[idx])
        idx += 1
        stones.add((c, l))

    SC = int(data[idx])
    idx += 1
    SL = int(data[idx])
    idx += 1

    RC = int(data[idx])
    idx += 1
    RL = int(data[idx])
    idx += 1

    if (SC, SL) not in stones or (RC, RL) not in stones:
        print('N')
        return

    visited = set()
    queue = deque()
    queue.append((SC, SL))
    visited.add((SC, SL))

    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    while queue:
        x, y = queue.popleft()
        if x == RC and y == RL:
            print('S')
            return

        for dx, dy in directions:
            for step in range(1, 4):
                nx = x + dx * step
                ny = y + dy * step
                if 1 <= nx <= N and 1 <= ny <= M:
                    if (nx, ny) in stones and (nx, ny) not in visited:
                        visited.add((nx, ny))
                        queue.append((nx, ny))
                else:
                    break

    print('N')

if __name__ == '__main__':
    main()
