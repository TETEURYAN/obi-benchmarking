import sys
from collections import deque

sys.setrecursionlimit(1000000)

N, M = map(int, sys.stdin.readline().split())
Xe, Ye = map(int, sys.stdin.readline().split())
Xs, Ys = map(int, sys.stdin.readline().split())

Xe -= 1
Ye -= 1
Xs -= 1
Ys -= 1

# Células livres "base": todas exceto armários em pé (i,j pares em 1-based => índices ímpares em 0-based)
free_cells = []
id_of = [[-1] * M for _ in range(N)]
for i in range(N):
    for j in range(M):
        if not (i % 2 == 1 and j % 2 == 1):
            id_of[i][j] = len(free_cells)
            free_cells.append((i, j))

F = len(free_cells)
start = id_of[Xe][Ye]
target = id_of[Xs][Ys]

# Armários
cabinets = []
cab_id = {}
for i in range(1, N, 2):
    for j in range(1, M, 2):
        cab_id[(i, j)] = len(cabinets)
        cabinets.append((i, j))

K = len(cabinets)

# Para cada célula livre, quais armários adjacentes podem ocupá-la quando caídos
cell_adj_cabs = [[] for _ in range(F)]
for idx, (i, j) in enumerate(free_cells):
    for di, dj in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        ci, cj = i + di, j + dj
        if (ci, cj) in cab_id:
            cell_adj_cabs[idx].append(cab_id[(ci, cj)])

# Máscara de células livres adjacentes a cada armário: ordem [right, left, down, up]
dir_defs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
cab_dir_cell = [[-1] * 4 for _ in range(K)]
for k, (i, j) in enumerate(cabinets):
    for d, (di, dj) in enumerate(dir_defs):
        ni, nj = i + di, j + dj
        cab_dir_cell[k][d] = id_of[ni][nj]

# Ordem dos armários para branching: mais próximos do centro primeiro
cx, cy = (N - 1) / 2.0, (M - 1) / 2.0
order = list(range(K))
order.sort(key=lambda k: abs(cabinets[k][0] - cx) + abs(cabinets[k][1] - cy))

assigned = [-1] * K  # direção escolhida 0..3

best = -1

def bfs_distance():
    blocked = [False] * F
    for k in range(K):
        d = assigned[k]
        if d != -1:
            blocked[cab_dir_cell[k][d]] = True

    if blocked[start] or blocked[target]:
        return -1

    dist = [-1] * F
    q = deque([start])
    dist[start] = 1

    while q:
        u = q.popleft()
        if u == target:
            return dist[u]
        i, j = free_cells[u]
        nd = dist[u] + 1
        if i > 0:
            v = id_of[i - 1][j]
            if v != -1 and not blocked[v] and dist[v] == -1:
                dist[v] = nd
                q.append(v)
        if i + 1 < N:
            v = id_of[i + 1][j]
            if v != -1 and not blocked[v] and dist[v] == -1:
                dist[v] = nd
                q.append(v)
        if j > 0:
            v = id_of[i][j - 1]
            if v != -1 and not blocked[v] and dist[v] == -1:
                dist[v] = nd
                q.append(v)
        if j + 1 < M:
            v = id_of[i][j + 1]
            if v != -1 and not blocked[v] and dist[v] == -1:
                dist[v] = nd
                q.append(v)
    return -1

def optimistic_upper_bound():
    # Considera que armários não atribuídos podem bloquear qualquer célula adjacente a eles.
    # Uma célula é certamente livre apenas se todos armários adjacentes já foram atribuídos
    # e nenhum deles a ocupa.
    maybe_blocked = [False] * F
    for idx in range(F):
        for k in cell_adj_cabs[idx]:
            d = assigned[k]
            if d == -1:
                maybe_blocked[idx] = True
                break
            if cab_dir_cell[k][d] == idx:
                maybe_blocked[idx] = True
                break

    if maybe_blocked[start] or maybe_blocked[target]:
        return -1

    dist = [-1] * F
    q = deque([start])
    dist[start] = 1
    best_local = -1

    while q:
        u = q.popleft()
        if u == target:
            best_local = dist[u]
            break
        i, j = free_cells[u]
        nd = dist[u] + 1
        if i > 0:
            v = id_of[i - 1][j]
            if v != -1 and not maybe_blocked[v] and dist[v] == -1:
                dist[v] = nd
                q.append(v)
        if i + 1 < N:
            v = id_of[i + 1][j]
            if v != -1 and not maybe_blocked[v] and dist[v] == -1:
                dist[v] = nd
                q.append(v)
        if j > 0:
            v = id_of[i][j - 1]
            if v != -1 and not maybe_blocked[v] and dist[v] == -1:
                dist[v] = nd
                q.append(v)
        if j + 1 < M:
            v = id_of[i][j + 1]
            if v != -1 and not maybe_blocked[v] and dist[v] == -1:
                dist[v] = nd
                q.append(v)

    if best_local == -1:
        return -1

    # Número de células certamente livres alcançáveis dá um limite superior simples para o comprimento do menor caminho
    cnt = 0
    for d in dist:
        if d != -1:
            cnt += 1
    return cnt

def dfs(pos):
    global best

    ub = optimistic_upper_bound()
    if ub <= best:
        return

    if pos == K:
        val = bfs_distance()
        if val > best:
            best = val
        return

    k = order[pos]

    # Heurística: tentar direções que não bloqueiem start/target primeiro
    dirs = [0, 1, 2, 3]
    dirs.sort(key=lambda d: (cab_dir_cell[k][d] == start) + (cab_dir_cell[k][d] == target))

    for d in dirs:
        assigned[k] = d
        dfs(pos + 1)
    assigned[k] = -1

dfs(0)
print(best)