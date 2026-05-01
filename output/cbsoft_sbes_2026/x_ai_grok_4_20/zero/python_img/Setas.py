
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

memo = [[-1] * N for _ in range(N)]
# -1: not visited, 0: leads to cycle or out, 1: leads to safe loop

def dfs(i, j):
    if memo[i][j] != -1:
        return memo[i][j]
    
    memo[i][j] = 0  # mark as visiting (cycle detection)
    di, dj = directions[grid[i][j]]
    ni, nj = i + di, j + dj
    
    if not (0 <= ni < N and 0 <= nj < N):
        memo[i][j] = 0  # goes out
        return 0
    
    if memo[ni][nj] == 0:
        # cycle detected or part of unsafe path
        memo[i][j] = 0
        return 0
    
    res = dfs(ni, nj)
    memo[i][j] = res
    return res

safe_count = 0
for i in range(N):
    for j in range(N):
        if dfs(i, j) == 1:
            safe_count += 1
        elif memo[i][j] == -1:
            # if still not visited after dfs (should not happen)
            pass

# Now, any cell that is part of a cycle that doesn't go out is safe
# We need to mark all cells in safe cycles
visited = [[False] * N for _ in range(N)]
def mark_cycle(i, j, path):
    if visited[i][j]:
        return
    visited[i][j] = True
    di, dj = directions[grid[i][j]]
    ni, nj = i + di, j + dj
    if 0 <= ni < N and 0 <= nj < N and not visited[ni][nj]:
        mark_cycle(ni, nj, path)
    # if we reach a safe cell, all in path are safe

# Recompute properly: a cell is safe if following the path never goes out
# That means it eventually reaches a cycle that is entirely inside the board.

# Better approach: simulate for all cells with path compression like union-find but for paths

# Let's reset and use a different strategy that works in O(N^2)

# We will simulate the path for each cell but memoize the final result
# To handle cycles correctly, we use three states: not visited, visiting, visited

state = [[0] * N for _ in range(N)]  # 0 not, 1 visiting, 2 done
safe = [[False] * N for _ in range(N)]

def is_safe(i, j):
    if state[i][j] == 2:
        return safe[i][j]
    
    if state[i][j] == 1:
        # cycle found - since we reached here without going out, it's a safe cycle
        return True
    
    state[i][j] = 1  # visiting
    di, dj = directions[grid[i][j]]
    ni, nj = i + di, j + dj
    
    if not (0 <= ni < N and 0 <= nj < N):
        safe[i][j] = False
        state[i][j] = 2
        return False
    
    res = is_safe(ni, nj)
    safe[i][j] = res
    state[i][j] = 2
    return res

count = 0
for i in range(N):
    for j in range(N):
        if is_safe(i, j):
            count += 1

print(count)
