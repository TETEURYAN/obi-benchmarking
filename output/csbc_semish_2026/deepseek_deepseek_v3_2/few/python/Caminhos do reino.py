import sys
sys.setrecursionlimit(200000)

def main():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    N = int(next(it))
    F = [0] + [int(next(it)) for _ in range(N)]
    Q = int(next(it))
    queries = [(int(next(it)), int(next(it))) for _ in range(Q)]

    # 1. Encontrar o ciclo
    visited = [0] * (N + 1)  # 0 = não visitado, 1 = visitando, 2 = processado
    cycle_id = [0] * (N + 1)  # id do ciclo (0 se não pertence ao ciclo)
    cycle_pos = [0] * (N + 1)  # posição no ciclo (0 se não pertence)
    cycle_len = [0] * (N + 1)  # tamanho do ciclo (0 se não pertence)
    cycle_index = 1

    for start in range(1, N + 1):
        if visited[start]:
            continue
        stack = []
        node = start
        while not visited[node]:
            visited[node] = 1
            stack.append(node)
            node = F[node]
        if visited[node] == 1:  # encontrou um ciclo
            # extrair ciclo
            cycle_nodes = []
            while stack:
                cur = stack.pop()
                cycle_nodes.append(cur)
                if cur == node:
                    break
            cycle_nodes.reverse()
            size = len(cycle_nodes)
            for idx, city in enumerate(cycle_nodes):
                cycle_id[city] = cycle_index
                cycle_pos[city] = idx
                cycle_len[city] = size
            cycle_index += 1
        # marcar todos como processados
        while stack:
            cur = stack.pop()
            visited[cur] = 2

    # 2. Calcular distâncias até o ciclo
    dist_to_cycle = [-1] * (N + 1)
    for city in range(1, N + 1):
        if cycle_id[city]:
            dist_to_cycle[city] = 0

    # processar em ordem topológica reversa (DFS a partir do ciclo)
    for city in range(1, N + 1):
        if dist_to_cycle[city] != -1:
            continue
        path = []
        cur = city
        while dist_to_cycle[cur] == -1:
            path.append(cur)
            cur = F[cur]
        d = dist_to_cycle[cur]
        for node in reversed(path):
            d += 1
            dist_to_cycle[node] = d

    # 3. Pré‑computar ancestrais comuns (LCA) nos caminhos periféricos
    # Construir árvore reversa (quem aponta para quem)
    parent = [0] * (N + 1)
    depth = [0] * (N + 1)
    for i in range(1, N + 1):
        parent[i] = F[i]

    # Para cada cidade no ciclo, sua profundidade é 0 e seu pai é ela mesma
    for i in range(1, N + 1):
        if cycle_id[i]:
            parent[i] = i
            depth[i] = 0

    # Calcular profundidades para cidades fora do ciclo
    for i in range(1, N + 1):
        if cycle_id[i]:
            continue
        if depth[i] == 0:
            stack = []
            cur = i
            while depth[cur] == 0 and not cycle_id[cur]:
                stack.append(cur)
                cur = parent[cur]
            base_depth = depth[cur]
            d = base_depth + 1
            while stack:
                node = stack.pop()
                depth[node] = d
                d += 1

    # 4. Tabela de ancestrais binários
    LOG = 18  # pois N <= 10^5
    up = [[0] * (N + 1) for _ in range(LOG)]
    for i in range(1, N + 1):
        up[0][i] = parent[i]
    for k in range(1, LOG):
        for i in range(1, N + 1):
            up[k][i] = up[k-1][up[k-1][i]]

    def lca(u, v):
        if depth[u] < depth[v]:
            u, v = v, u
        diff = depth[u] - depth[v]
        for k in range(LOG-1, -1, -1):
            if diff & (1 << k):
                u = up[k][u]
        if u == v:
            return u
        for k in range(LOG-1, -1, -1):
            if up[k][u] != up[k][v]:
                u = up[k][u]
                v = up[k][v]
        return parent[u]

    # 5. Responder consultas
    out_lines = []
    for a, b in queries:
        if a == b:
            out_lines.append("0")
            continue

        # Se ambos estão no mesmo ciclo
        if cycle_id[a] and cycle_id[b] and cycle_id[a] == cycle_id[b]:
            pos_a = cycle_pos[a]
            pos_b = cycle_pos[b]
            size = cycle_len[a]
            dist_on_cycle = min((pos_a - pos_b) % size, (pos_b - pos_a) % size)
            out_lines.append(str(dist_on_cycle))
            continue

        # Se ambos estão em ciclos diferentes
        if cycle_id[a] and cycle_id[b] and cycle_id[a] != cycle_id[b]:
            # Eles só podem se encontrar em algum nó do ciclo de um deles,
            # mas como são ciclos distintos, o encontro só pode ser em algum nó
            # que seja alcançável a partir de ambos? Na verdade, como cada ciclo
            # é isolado e não há conexão entre ciclos, eles nunca se encontram.
            # Mas o problema garante que há exatamente um ciclo.
            # Portanto, essa situação não ocorre.
            pass

        # Caso geral: pelo menos um está fora do ciclo
        # Encontrar o nó de encontro no ciclo ou no caminho periférico
        if cycle_id[a] and not cycle_id[b]:
            a, b = b, a  # agora a é o que está fora do ciclo

        if not cycle_id[a] and not cycle_id[b]:
            l = lca(a, b)
            if cycle_id[l]:  # LCA está no ciclo
                da = depth[a] - depth[l]
                db = depth[b] - depth[l]
                out_lines.append(str(da + db))
            else:
                # LCA está fora do ciclo
                da = depth[a] - depth[l]
                db = depth[b] - depth[l]
                out_lines.append(str(da + db))
        elif not cycle_id[a] and cycle_id[b]:
            # a está fora, b está no ciclo
            # a sobe até o ciclo, depois anda pelo ciclo até b
            root_a = a
            while not cycle_id[root_a]:
                root_a = parent[root_a]
            dist_to_root = depth[a]
            pos_root = cycle_pos[root_a]
            pos_b = cycle_pos[b]
            size = cycle_len[root_a]
            dist_on_cycle = min((pos_root - pos_b) % size, (pos_b - pos_root) % size)
            total = dist_to_root + dist_on_cycle
            out_lines.append(str(total))
        else:
            # ambos no ciclo, mas já tratado acima
            pass

    sys.stdout.write("\n".join(out_lines))

if __name__ == "__main__":
    main()