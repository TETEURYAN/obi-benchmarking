
import sys
from collections import deque

def main():
    data = sys.stdin.read().split()
    if not data:
        return

    idx = 0
    N = int(data[idx]); idx += 1
    M = int(data[idx]); idx += 1
    X = int(data[idx]); idx += 1
    Y = int(data[idx]); idx += 1
    K = int(data[idx]); idx += 1

    occupied = set()
    for _ in range(K):
        A = int(data[idx]); idx += 1
        B = int(data[idx]); idx += 1
        occupied.add((A, B))

    directions = [(-1, -1), (-1, 0), (-1, 1),
                  (0, -1),          (0, 1),
                  (1, -1),  (1, 0), (1, 1)]

    visited = set()
    queue = deque()
    start = (X, Y)
    if start not in occupied:
        queue.append(start)
        visited.add(start)

    count = 0
    while queue:
        i, j = queue.popleft()
        count += 1
        for di, dj in directions:
            ni, nj = i + di, j + dj
            if 1 <= ni <= N and 1 <= nj <= M:
                if (ni, nj) not in occupied and (ni, nj) not in visited:
                    visited.add((ni, nj))
                    queue.append((ni, nj))

    print(count)

if __name__ == "__main__":
    main()
