import sys
from collections import deque

def main():
    data = sys.stdin.read().split()
    idx = 0
    N = int(data[idx]); idx+=1
    M = int(data[idx]); idx+=1
    X = int(data[idx]); idx+=1
    Y = int(data[idx]); idx+=1
    K = int(data[idx]); idx+=1

    filled = set()
    for _ in range(K):
        a = int(data[idx]); idx+=1
        b = int(data[idx]); idx+=1
        filled.add((a, b))

    visited = set()
    queue = deque()
    queue.append((X, Y))
    visited.add((X, Y))
    count = 0

    directions = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]

    while queue:
        ci, cj = queue.popleft()
        count += 1
        for di, dj in directions:
            ni, nj = ci+di, cj+dj
            if 1 <= ni <= N and 1 <= nj <= M and (ni,nj) not in filled and (ni,nj) not in visited:
                visited.add((ni,nj))
                queue.append((ni,nj))

    print(count)

main()