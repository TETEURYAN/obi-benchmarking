import sys

data = sys.stdin.read().split()
if not data:
    sys.exit()

n = int(data[0])
grid = data[1:1 + n]

m = n * n
n1 = n - 1

nxt = [-1] * m

for i in range(n):
    row = grid[i]
    base = i * n
    for j, c in enumerate(row):
        u = base + j
        if c == 'V':
            if i == n1:
                nxt[u] = -1
            else:
                nxt[u] = u + n
        elif c == 'A':
            if i == 0:
                nxt[u] = -1
            else:
                nxt[u] = u - n
        elif c == '>':
            if j == n1:
                nxt[u] = -1
            else:
                nxt[u] = u + 1
        else:  # '<'
            if j == 0:
                nxt[u] = -1
            else:
                nxt[u] = u - 1

state = [0] * m
safe = [False] * m

for s in range(m):
    if state[s] != 0:
        continue

    path = []
    pos = {}

    u = s
    while True:
        if u == -1:
            for v in path:
                state[v] = 2
                safe[v] = False
            break

        st = state[u]
        if st == 2:
            res = safe[u]
            for v in path:
                state[v] = 2
                safe[v] = res
            break

        if u in pos:
            start = pos[u]
            for k in range(start, len(path)):
                v = path[k]
                state[v] = 2
                safe[v] = True
            for k in range(start):
                v = path[k]
                state[v] = 2
                safe[v] = True
            break

        pos[u] = len(path)
        path.append(u)
        state[u] = 1
        u = nxt[u]

print(sum(safe))