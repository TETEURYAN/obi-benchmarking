
import sys

sys.setrecursionlimit(10**6)

N = int(input())
grid = [input().strip() for _ in range(N)]

directions = {
    'V': (1, 0),
    '<': (0, -1),
    '>': (0, 1),
    'A': (-1, 0)
}

memo = [[-1 for _ in range(N)] for _ in range(N)]
# -1: not visited, 0: leads to out, 1: safe (cycle or stays in)

def dfs(i, j):
    if memo[i][j] != -1:
        return memo[i][j]
    
    memo[i][j] = 0  # assume leads to out until proven otherwise
    di, dj = directions[grid[i][j]]
    ni, nj = i + di, j + dj
    
    if not (0 <= ni < N and 0 <= nj < N):
        memo[i][j] = 0
        return 0
    
    if memo[ni][nj] == 0:
        memo[i][j] = 0
        return 0
    elif memo[ni][nj] == 1:
        memo[i][j] = 1
        return 1
    else:
        # visit next
        res = dfs(ni, nj)
        memo[i][j] = res
        return res

safe_count = 0
for i in range(N):
    for j in range(N):
        if dfs(i, j) == 1:
            safe_count += 1

print(safe_count)
