from collections import deque
import sys
input = sys.stdin.readline

def solve():
    N, M = map(int, input().split())
    grid = []
    start = None
    for i in range(N):
        row = list(map(int, input().split()))
        grid.append(row)
        for j in range(M):
            if row[j] == 2:
                start = (i, j)
    
    # BFS/path following: from start (2), follow cells with value 1, 2, or 3
    # The path is unique (no ambiguity), so we just follow it
    # Count rooms including start and exit (3)
    
    directions = [(-1,0),(1,0),(0,-1),(0,1)]
    
    visited = [[False]*M for _ in range(N)]
    visited[start[0]][start[1]] = True
    
    count = 1  # count current room
    current = start
    
    while True:
        found_next = False
        ci, cj = current
        for di, dj in directions:
            ni, nj = ci+di, cj+dj
            if 0 <= ni < N and 0 <= nj < M and not visited[ni][nj]:
                val = grid[ni][nj]
                if val == 1 or val == 3:
                    visited[ni][nj] = True
                    count += 1
                    current = (ni, nj)
                    found_next = True
                    if val == 3:
                        print(count)
                        return
                    break
        if not found_next:
            break
    
    print(count)

solve()