import sys

data = sys.stdin.read().split()
if not data:
    sys.exit()

m = int(data[0])
grid = data[1:1 + m]
a = int(data[1 + m]) - 1
b = int(data[2 + m]) - 1

n = m * m
nxt = [-2] * n
treasure = -1

for i in range(m):
    row = grid[i]
    base = i * m
    for j, c in enumerate(row):
        idx = base + j
        if c == 'X':
            treasure = idx
            nxt[idx] = -2
        elif c == 'N':
            ni, nj = i - 1, j
            nxt[idx] = ni * m + nj if ni >= 0 else -1
        elif c == 'S':
            ni, nj = i + 1, j
            nxt[idx] = ni * m + nj if ni < m else -1
        elif c == 'L':
            ni, nj = i, j + 1
            nxt[idx] = ni * m + nj if nj < m else -1
        else:  # 'O'
            ni, nj = i, j - 1
            nxt[idx] = ni * m + nj if nj >= 0 else -1

start = a * m + b

state = [0] * n
dist = [0] * n

def solve(s):
    path = []
    pos = {}
    cur = s
    while True:
        if cur == -1:
            res = -1
            break
        if cur == treasure:
            res = 0
            break
        st = state[cur]
        if st == 2:
            res = dist[cur]
            break
        if st == 1:
            res = 0
            break
        if cur in pos:
            res = 0
            break
        pos[cur] = len(path)
        path.append(cur)
        state[cur] = 1
        cur = nxt[cur]

    d = res
    for v in reversed(path):
        if d > 0:
            dist[v] = d
            state[v] = 2
            d += 1
        else:
            dist[v] = d
            state[v] = 2

    return dist[s]

print(solve(start))