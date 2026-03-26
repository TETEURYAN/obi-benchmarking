import sys
from collections import deque

# Configuração de recursão conforme diretrizes
sys.setrecursionlimit(200000)

def solve():
    # Leitura rápida de entrada
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return

    iterator = iter(input_data)
    
    try:
        N = int(next(iterator))
        M = int(next(iterator))
    except StopIteration:
        return

    # Lista de adjacência para o sistema Círculo (Árvore 1)
    adj1 = [[] for _ in range(N + 1)]
    for _ in range(N - 1):
        u = int(next(iterator))
        v = int(next(iterator))
        adj1[u].append(v)
        adj1[v].append(u)

    # Lista de adjacência para o sistema Quadrado (Árvore 2)
    adj2 = [[] for _ in range(M + 1)]
    for _ in range(M - 1):
        u = int(next(iterator))
        v = int(next(iterator))
        adj2[u].append(v)
        adj2[v].append(u)

    def find_tree_center(adj, num_nodes):
        # Função auxiliar para BFS que retorna o nó mais distante e o array de distâncias/pais
        def bfs_farthest(source):
            q = deque([source])
            dist = [-1] * (num_nodes + 1)
            parent = [-1] * (num_nodes + 1)
            dist[source] = 0
            farthest_node = source
            max_dist = 0
            
            while q:
                u = q.popleft()
                for v in adj[u]:
                    if dist[v] == -1:
                        dist[v] = dist[u] + 1
                        parent[v] = u
                        q.append(v)
                        if dist[v] > max_dist:
                            max_dist = dist[v]
                            farthest_node = v
            return farthest_node, parent

        # 1. Encontra uma extremidade do diâmetro a partir de um nó arbitrário (1)
        u, _ = bfs_farthest(1)
        
        # 2. Encontra a outra extremidade do diâmetro a partir de u e recupera o caminho
        v, parent = bfs_farthest(u)
        
        # Reconstrói o caminho de v até u
        path = []
        curr = v
        while curr != -1:
            path.append(curr)
            curr = parent[curr]
            
        # O centro é o nó no meio do caminho do diâmetro
        # Se o caminho tem comprimento ímpar, há dois centros; qualquer um serve.
        # O índice inteiro // 2 seleciona o centro "superior" ou o único centro.
        return path[len(path) // 2]

    # Encontra o centro de cada árvore
    center_circle = find_tree_center(adj1, N)
    center_square = find_tree_center(adj2, M)

    # Imprime o resultado
    print(center_circle, center_square)

if __name__ == '__main__':
    solve()