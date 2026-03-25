import sys
sys.setrecursionlimit(100000)

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    n = int(data[0])
    adj = [[] for _ in range(n + 1)]
    idx = 1
    for _ in range(n - 1):
        x = int(data[idx])
        y = int(data[idx + 1])
        adj[x].append(y)
        adj[y].append(x)
        idx += 2

    # Função para encontrar os dois endpoints do diametro (BFS dupla)
    def bfs(start):
        dist = [-1] * (n + 1)
        q = [start]
        dist[start] = cluster_id[start]
        farthest = start
        for node in q:
            for nb in adj[node]:
                if dist[nb] == -1:
                    dist[nb] = cluster_id[nb]
                    q.append(nb)
                    farthest = nb
        return farthest, dist

    # DFS para marcar clusters (árvores) após remover o centro do diametro
    cluster_id = [-1] * (n + 1)
    clusters = []
    visited = [False] * (n + 1)

    def dfs(u, cid):
        stack = [u]
        visited[u] = True
        cluster_id[u] = cid
        size = 1
        while stack:
            v = stack.pop()
            for nb in adj[v]:
                if not visited[nb]:
                    visited[nb] = True
                    cluster_id[nb] = cid
                    stack.append(nb)
                    size += 1
        return size

    # Primeiro diametro
    far1, _ = bfs(1)
    far2, _ = bfs(far1)
    _, dist_from_far2 = bfs(far2)

    # Encontrar centro(s) do diametro
    path = []
    u = far2
    d = dist_from_far2[far2]
    while d > 0:
        path.append(u)
        for nb in adj[u]:
            if dist_from_far2[nb] == d - 1:
                u = nb
                d -= 1
                break
    path.append(u)

    diam_len = len(path)
    if diam_len % 2 == 1:
        center = path[diam_len // 2]
        visited[center] = True
        cid = 0
        for nb in adj[center]:
            if not visited[nb]:
                sz = dfs(nb, cid)
                clusters.append(sz)
                cid += 1
    else:
        center1 = path[diam_len // 2 - 1]
        center2 = path[diam_len // 2]
        visited[center1] = True
        visited[center2] = True
        cid = 0
        for nb in adj[center1]:
            if nb != center2 and not visited[nb]:
                sz = dfs(nb, cid)
                clusters.append(sz)
                cid += 1
        for nb in adj[center2]:
            if nb != center1 and not visited[nb]:
                sz = dfs(nb, cid)
                clusters.append(sz)
                cid += 1

    # Calcular o maior ciclo possível
    # O maior ciclo é diam_len + 1 (se diametro impar) ou diam_len (se diametro par)
    # Mas precisamos verificar se há dois clusters grandes para o caso par
    if diam_len % 2 == 0:
        # Diametro par: centro são dois vértices conectados
        # O maior ciclo possível é diam_len se conectarmos dois vértices em clusters diferentes dos centros
        # Ou diam_len + 1 se conectarmos os dois centros? Não, conectando os centros não cria ciclo novo (já são conectados).
        # Portanto, o maior ciclo é diam_len + 1 se tivermos dois clusters grandes para os dois centros.
        # Mas o ciclo seria: centro1 -> clusterA -> ... -> centro2 -> clusterB -> ... -> centro1 (com nova aresta entre vertices dos clusters)
        # O ciclo teria tamanho: tamanho do caminho entre os dois vértices nos clusters + 2 (para passar pelos centros) + 1 (nova aresta)
        # Isso fica: depthA + depthB + 2 + 1 = depthA + depthB + 3.
        # O máximo depthA e depthB são os maiores depths em cada cluster (que são os tamanhos dos clusters? Não, é a maior distância de um vértice ao centro dentro do cluster).
        # Para simplificar, assumimos que o maior depth é o tamanho do cluster (árvore).
        # Então o maior ciclo possível é: max(cluster[i]) + max(cluster[j]) + 3, para i != j (centros diferentes).
        # Além disso, o diam_len (ciclo usando apenas os centros) é diam_len, mas isso é menor que o acima se clusters grandes.
        # Portanto, precisamos calcular:
        #   candidato1: diam_len (ciclo formado pelos vértices do diametro + nova aresta entre dois vértices não adjacentes no diametro)
        #   candidato2: diam_len + 1 (ciclo que passa pelos dois centros e pelos dois maiores clusters)
        # Mas o problema original sugere que o maior ciclo é diam_len + 1 para diametro impar, e diam_len para diametro par?
        # Reanalisando exemplos:
        # Teste 1: N=5, diam_len=4 (par), maior ciclo=4 (resposta).
        # Teste 2: N=8, diam_len=5 (impar), maior ciclo=5 (resposta).
        # Nos exemplos, o maior ciclo é igual ao diam_len.
        # Portanto, para diametro par, o maior ciclo é diam_len.
        # Para diametro impar, o maior ciclo é diam_len + 1.
        # Isso porque:
        # - Diametro par: os dois centros estão conectados, então o ciclo pode incluir ambos centros e os clusters, mas a nova aresta conectando dois vértices de clusters diferentes faz um ciclo de tamanho diam_len.
        # - Diametro impar: o centro é único, então precisamos de dois vértices no mesmo cluster? Não, o ciclo é diam_len + 1 usando dois vértices em clusters diferentes (ou mesmo cluster?) Vamos calcular corretamente.

        # Algoritmo conhecido:
        # 1) Encontrar diametro D.
        # 2) Se D é impar (centro único), maior ciclo = D+1.
        #    Número de maneiras = soma sobre todos os pares de clusters: (size_i * size_j) para i != j, mais (size_i * (size_i-1))/2 se houver mais de um vértice no cluster? Não.
        #    Realmente: para centro único, nova aresta entre dois vértices em clusters diferentes cria ciclo de tamanho D+1.
        #    Portanto, contamos pares de vértices em clusters diferentes.
        #    Total = soma_{i < j} size_i * size_j.
        # 3) Se D é par (dois centros), maior ciclo = D.
        #    Número de maneiras: escolher dois vértices, um em cada cluster dos dois centros, mas não nos centros.
        #    Portanto, (size_clusterA) * (size_clusterB), onde clusterA é do centro1, clusterB é do centro2.
        #    Se houver mais clusters para cada centro, soma sobre todos.

        # Implementação:
        if diam_len % 2 == 1:
            max_cycle = diam_len + 1
            total_pairs = 0
            total_nodes_in_clusters = sum(clusters)
            for sz in clusters:
                total_pairs += sz * (total_nodes_in_clusters - sz)
            total_pairs //= 2  # porque cada par foi contado duas vezes (i,j e j,i)
            ways = total_pairs
        else:
            max_cycle = diam_len
            # clusters são divididos pelos dois centros
            # precisamos separar clusters por centro
            clusters_center1 = []
            clusters_center2 = []
            # refazer a DFS marcando qual centro
            # Mas já temos cluster_id, podemos usar a distância para determinar qual centro
            # Para centro1 (center1), cluster_id é atribuido para seus vizinhos.
            # Para centro2 (center2), cluster_id é atribuido para seus vizinhos.
            # No caso par, clusters foram atribuidos sequencialmente: primeiro vizinhos de center1, depois vizinhos de center2.
            # Vamos contar os clusters de cada centro.
            # Reconstruir a lista de clusters por centro.
            visited = [False] * (n + 1)
            cluster_id = [-1] * (n + 1)
            clusters_center1 = []
            clusters_center2 = []
            visited[center1] = True
            visited[center2] = True
            cid = 0
            for nb in adj[center1]:
                if nb != center2 and not visited[nb]:
                    sz = dfs(nb, cid)
                    clusters_center1.append(sz)
                    cid += 1
            for nb in adj[center2]:
                if nb != center1 and not visited[nb]:
                    sz = dfs(nb, cid)
                    clusters_center2.append(sz)
                    cid += 1

            ways = 0
            for sz1 in clusters_center1:
                for sz2 in clusters_center2:
                    ways += sz1 * sz2
    else:
        # diam_len impar
        max_cycle = diam_len + 1
        total_pairs = 0
        total = sum(clusters)
        for sz in clusters:
            total_pairs += sz * (total - sz)
        total_pairs //= 2
        ways = total_pairs

    print(max_cycle)
    print(ways)

if __name__ == "__main__":
    solve()