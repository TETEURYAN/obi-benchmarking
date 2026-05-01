import sys
from collections import deque

sys.setrecursionlimit(1000000)

N, M = map(int, sys.stdin.readline().split())
Xe, Ye = map(int, sys.stdin.readline().split())
Xs, Ys = map(int, sys.stdin.readline().split())

# Trabalhamos no grafo das células livres "base":
# células com pelo menos uma coordenada ímpar.
# Cada armário está em (i,j) com i,j pares e deve cair para uma das 4 células vizinhas livres.
# Isso equivale a escolher, para cada vértice "armário", exatamente uma aresta incidente
# do grafo bipartido entre células livres e armários; a célula escolhida fica bloqueada.
#
# Queremos maximizar a menor distância entre entrada e saída nas células livres não bloqueadas.
#
# Como N,M <= 11, o número de armários é <= 25 e o número de células livres <= 96.
# Fazemos busca binária na resposta L e testamos se existe configuração com distância >= L.
#
# Para um L fixo, enumeramos caminhos simples P de comprimento exatamente L entre entrada e saída
# no grafo base. Se existir uma configuração com distância >= L, então existe um menor caminho
# de comprimento d >= L; seu prefixo de L células forma um caminho simples P tal que:
# - todas as células de P devem permanecer livres;
# - nenhuma aresta "atalho" entre vértices de P pode conectar posições com diferença > 1,
#   senão haveria caminho mais curto dentro de P;
# - para cada vértice fora de P adjacente a dois ou mais vértices de P, isso também criaria atalho
#   de comprimento 2, então tais vértices devem ser bloqueados;
# - além disso, para garantir que P seja realizável, toda célula fora de P que precise ser bloqueada
#   deve poder ser escolhida por algum armário, respeitando que cada armário escolhe exatamente uma célula.
#
# Isso vira um problema de emparelhamento/perfect matching com restrições:
# cada armário escolhe uma vizinha; células de P são proibidas; células "forçadas" devem ser escolhidas.
# Como o grafo é pequeno, resolvemos por DP com memoização por componente.

# Indexação das células livres
free_cells = []
cell_id = {}
for i in range(1, N + 1):
    for j in range(1, M + 1):
        if i % 2 == 1 or j % 2 == 1:
            idx = len(free_cells)
            free_cells.append((i, j))
            cell_id[(i, j)] = idx

F = len(free_cells)

# Grafo base entre células livres adjacentes ortogonalmente
adj = [[] for _ in range(F)]
for idx, (i, j) in enumerate(free_cells):
    for di, dj in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        ni, nj = i + di, j + dj
        if 1 <= ni <= N and 1 <= nj <= M and (ni, nj) in cell_id:
            adj[idx].append(cell_id[(ni, nj)])

s = cell_id[(Xe, Ye)]
t = cell_id[(Xs, Ys)]

# Armários
cabinets = []
cab_neighbors = []
cell_to_cabs = [[] for _ in range(F)]
for i in range(2, N + 1, 2):
    for j in range(2, M + 1, 2):
        cid = len(cabinets)
        cabinets.append((i, j))
        neigh = []
        for di, dj in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            ni, nj = i + di, j + dj
            if 1 <= ni <= N and 1 <= nj <= M:
                v = cell_id[(ni, nj)]
                neigh.append(v)
                cell_to_cabs[v].append(cid)
        cab_neighbors.append(neigh)

C = len(cabinets)

# Ordem de DFS: explorar vizinhos mais próximos do alvo para achar caminhos longos úteis mais cedo
dist_to_t = [-1] * F
dq = deque([t])
dist_to_t[t] = 0
while dq:
    v = dq.popleft()
    for u in adj[v]:
        if dist_to_t[u] == -1:
            dist_to_t[u] = dist_to_t[v] + 1
            dq.append(u)

for v in range(F):
    adj[v].sort(key=lambda x: dist_to_t[x] if dist_to_t[x] != -1 else 10**9)

# Componentes do grafo bipartido armários-células livres
# úteis para decompor o teste de matching.
bip_adj_cells = [cell_to_cabs[v] for v in range(F)]
visited_c = [False] * C
visited_v = [False] * F
cab_comp = [-1] * C
cell_comp = [-1] * F
comp_cabs = []
comp_cells = []

for c in range(C):
    if visited_c[c]:
        continue
    q = deque()
    q.append(('c', c))
    visited_c[c] = True
    cabs = []
    cells = []
    comp_idx = len(comp_cabs)
    while q:
        typ, x = q.popleft()
        if typ == 'c':
            cab_comp[x] = comp_idx
            cabs.append(x)
            for v in cab_neighbors[x]:
                if not visited_v[v]:
                    visited_v[v] = True
                    q.append(('v', v))
        else:
            cell_comp[x] = comp_idx
            cells.append(x)
            for cc in bip_adj_cells[x]:
                if not visited_c[cc]:
                    visited_c[cc] = True
                    q.append(('c', cc))
    comp_cabs.append(cabs)
    comp_cells.append(cells)

num_comp = len(comp_cabs)

# Pré-cálculos por componente
comp_cell_pos = []
comp_cab_pos = []
comp_cab_masks = []
for k in range(num_comp):
    cells = comp_cells[k]
    cabs = comp_cabs[k]
    posv = {v: i for i, v in enumerate(cells)}
    posc = {c: i for i, c in enumerate(cabs)}
    masks = []
    for c in cabs:
        m = 0
        for v in cab_neighbors[c]:
            m |= 1 << posv[v]
        masks.append(m)
    comp_cell_pos.append(posv)
    comp_cab_pos.append(posc)
    comp_cab_masks.append(masks)

from functools import lru_cache

def component_feasible(comp_idx, path_set_global, forced_set_global):
    cells = comp_cells[comp_idx]
    cabs = comp_cabs[comp_idx]
    posv = comp_cell_pos[comp_idx]
    masks = comp_cab_masks[comp_idx]
    n_cells = len(cells)
    n_cabs = len(cabs)

    forbidden = 0
    forced = 0
    for v in cells:
        bit = 1 << posv[v]
        if v in path_set_global:
            forbidden |= bit
        elif v in forced_set_global:
            forced |= bit

    # Cada armário deve escolher exatamente uma célula permitida.
    # Células forçadas devem ser escolhidas por algum armário.
    allowed_masks = []
    for m in masks:
        am = m & ~forbidden
        if am == 0:
            return False
        allowed_masks.append(am)

    # poda simples: número de células forçadas não pode exceder armários
    if forced.bit_count() > n_cabs:
        return False

    # Ordena armários por menor domínio
    order = list(range(n_cabs))
    order.sort(key=lambda i: (allowed_masks[i].bit_count(), -(allowed_masks[i] & forced).bit_count()))

    @lru_cache(maxsize=None)
    def dp(idx, covered_forced):
        if idx == n_cabs:
            return covered_forced == forced
        ci = order[idx]
        opts = allowed_masks[ci]

        # Se faltam k células forçadas descobertas e restam menos de k armários, impossível
        rem = n_cabs - idx
        missing = (forced & ~covered_forced).bit_count()
        if missing > rem:
            return False

        x = opts
        while x:
            b = x & -x
            x -= b
            if dp(idx + 1, covered_forced | (b & forced)):
                return True
        return False

    return dp(0, 0)

def feasible_for_path(path):
    path_set = set(path)
    pos = {v: i for i, v in enumerate(path)}
    forced = set()

    # 1) Nenhuma aresta entre vértices do caminho pode pular posições
    for i, v in enumerate(path):
        for u in adj[v]:
            if u in pos:
                if abs(pos[u] - i) != 1:
                    return False

    # 2) Qualquer vértice fora do caminho adjacente a >=2 vértices do caminho cria atalho de comprimento 2
    # (ou comprimento 1 se fosse aresta direta, já tratado acima), então deve ser bloqueado.
    for v in range(F):
        if v in path_set:
            continue
        cnt = 0
        neigh_pos = []
        for u in adj[v]:
            if u in pos:
                cnt += 1
                neigh_pos.append(pos[u])
                if cnt >= 2:
                    break
        if cnt >= 2:
            forced.add(v)

    # 3) Células forçadas não podem estar no caminho e precisam ser bloqueáveis
    for v in forced:
        if not cell_to_cabs[v]:
            return False

    # 4) Verifica por componente do grafo bipartido
    touched = set()
    for v in path_set:
        touched.add(cell_comp[v])
    for v in forced:
        touched.add(cell_comp[v])

    for comp_idx in touched:
        if not component_feasible(comp_idx, path_set, forced):
            return False

    # Componentes não tocados sempre são viáveis (cada armário escolhe qualquer vizinha)
    return True

def exists_path_of_length(L):
    # comprimento em número de células
    if L == 1:
        return s == t

    visited = [False] * F
    path = [s]
    visited[s] = True

    # poda por distância mínima até t no grafo base
    def dfs(v, depth):
        # depth = tamanho atual do caminho em células
        rem = L - depth
        dmin = dist_to_t[v]
        if dmin == -1 or dmin > rem:
            return False
        if depth == L:
            if v != t:
                return False
            return feasible_for_path(path)

        # Para terminar exatamente em t sem repetir, se já estamos em t antes da hora, não serve
        if v == t:
            return False

        for u in adj[v]:
            if not visited[u]:
                visited[u] = True
                path.append(u)
                if dfs(u, depth + 1):
                    return True
                path.pop()
                visited[u] = False
        return False

    return dfs(s, 1)

# Limite superior: número de células livres
lo, hi = 1, F
ans = 1
while lo <= hi:
    mid = (lo + hi) // 2
    if exists_path_of_length(mid):
        ans = mid
        lo = mid + 1
    else:
        hi = mid - 1

print(ans)