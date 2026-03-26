import sys

def solve():
    # Leitura rápida de toda a entrada
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return

    iterator = iter(input_data)
    
    try:
        # N: número de cidades, A: origem, B: destino
        N = int(next(iterator))
        A = int(next(iterator))
        B = int(next(iterator))
    except StopIteration:
        return

    # Lista de adjacência para representar a árvore
    # Índices de 1 a N
    adj = [[] for _ in range(N + 1)]

    # Leitura das N-1 arestas
    for _ in range(N - 1):
        try:
            P = int(next(iterator))
            Q = int(next(iterator))
            D = int(next(iterator))
            
            adj[P].append((Q, D))
            adj[Q].append((P, D))
        except StopIteration:
            break

    # Busca em profundidade (DFS) iterativa para encontrar a distância de A até B
    # Como o grafo é uma árvore, existe um caminho único entre quaisquer dois nós.
    # Pilha armazena tuplas: (nó_atual, distância_acumulada_desde_A)
    stack = [(A, 0)]
    visited = [False] * (N + 1)
    visited[A] = True
    
    while stack:
        u, dist = stack.pop()
        
        if u == B:
            print(dist)
            return
        
        for v, weight in adj[u]:
            if not visited[v]:
                visited[v] = True
                stack.append((v, dist + weight))

if __name__ == "__main__":
    solve()