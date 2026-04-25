import sys
sys.setrecursionlimit(200000)
input_data = sys.stdin.read().split()
idx = 0
N = int(input_data[idx])
idx += 1
F = [0] * (N + 1)
for i in range(1, N + 1):
    F[i] = int(input_data[idx])
    idx += 1
Q = int(input_data[idx])
idx += 1
queries = []
for _ in range(Q):
    A = int(input_data[idx])
    B = int(input_data[idx + 1])
    queries.append((A, B))
    idx += 2
dist = [-1] * (N + 1)
entry = [0] * (N + 1)
state = [0] * (N + 1)
cycle_start = -1
def dfs(node):
    global cycle_start
    if state[node] == 2:
        return dist[node], entry[node]
    if state[node] == 1:
        cycle_start = node
        return 0, node
    state[node] = 1
    next_d, next_e = dfs(F[node])
    if cycle_start == -1:
        dist[node] = 1 + next_d
        entry[node] = next_e
    else:
        dist[node] = 0
        entry[node] = node
        if node == cycle_start:
            cycle_start = -1
    state[node] = 2
    return dist[node], entry[node]
for i in range(1, N + 1):
    if state[i] == 0:
        dfs(i)
start = entry[1]
cycle = []
visited = [False] * (N + 1)
current = start
while not visited[current]:
    visited[current] = True
    cycle.append(current)
    current = F[current]
pos_in_cycle = [-1] * (N + 1)
for i, node in enumerate(cycle):
    pos_in_cycle[node] = i
cycle_len = len(cycle)
for A, B in queries:
    if A == B:
        print(0)
        continue
    a = A
    b = B
    da = dist[a]
    db = dist[b]
    posA = 0
    posB = 0
    while da > db:
        a = F[a]
        da -= 1
        posA += 1
    while db > da:
        b = F[b]
        db -= 1
        posB += 1
    found = False
    while da > 0:
        if a == b:
            found = True
            break
        a = F[a]
        b = F[b]
        da -= 1
        db -= 1
        posA += 1
        posB += 1
    if found:
        time = max(posA, posB)
    else:
        p = a
        q = b
        pp = pos_in_cycle[p]
        pq = pos_in_cycle[q]
        movesP = 0
        movesQ = 0
        while p != q:
            if pp > pq:
                p = F[p]
                pp = (pp + 1) % cycle_len
                movesP += 1
            elif pq > pp:
                q = F[q]
                pq = (pq + 1) % cycle_len
                movesQ += 1
        time = max(posA + movesP, posB + movesQ)
    print(time)