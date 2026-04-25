import sys
sys.setrecursionlimit(300000)

input_data = sys.stdin.read().splitlines()
N = int(input_data[0])
grid = [list(line) for line in input_data[1:]]
memo = [[-1 for _ in range(N)] for _ in range(N)]

def get_next(i, j):
    if grid[i][j] == 'V':
        return i + 1, j
    elif grid[i][j] == 'A':
        return i - 1, j
    elif grid[i][j] == '>':
        return i, j + 1
    elif grid[i][j] == '<':
        return i, j - 1

def is_safe(i, j):
    if memo[i][j] == 1:
        return True
    if memo[i][j] == 2:
        return False
    if memo[i][j] == 0:
        return True
    memo[i][j] = 0
    ni, nj = get_next(i, j)
    if ni < 0 or ni >= N or nj < 0 or nj >= N:
        memo[i][j] = 2
        return False
    else:
        safe = is_safe(ni, nj)
        memo[i][j] = 1 if safe else 2
        return safe

count = 0
for i in range(N):
    for j in range(N):
        if is_safe(i, j):
            count += 1
print(count)