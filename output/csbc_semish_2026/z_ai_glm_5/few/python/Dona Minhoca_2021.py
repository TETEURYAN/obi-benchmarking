
import sys
from collections import deque

# Definir um limite de recursão alto, embora usemos BFS iterativo
sys.setrecursionlimit(200000)

def solve():
    # Leitura rápida de toda a entrada
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return

    iterator = iter(input_data)
    
    try:
        n = int(next(iterator))
    except StopIteration:
        return

    # Lista de adjacência para o grafo
    adj = [[] for _ in range(n + 1)]
    
    for _ in range(n - 1):
        try:
            u = int(next(iterator))
            v = int(next(iterator))
            adj[u].append(v)
            adj[v].append(u)
        except StopIteration:
            break
            
    # Função BFS para calcular distâncias a partir de um nó inicial
    def bfs(start_node):
        dist = [-1] * (n + 1)
        q = deque([start_node])
        dist[start_node] = 0
        while q:
            u = q.popleft()
            for v in adj[u]:
                if dist[v] == -1:
                    dist[v] = dist[u] + 1
                    q.append(v)
        return dist

    # 1. Encontrar uma extremidade do diâmetro (u) começando de um nó arbitrário (1)
    dist1 = bfs(1)
    u = 0
    max_dist = -1
    for i in range(1, n + 1):
        if dist1[i] > max_dist:
            max_dist = dist1[i]
            u = i
            
    # 2. Encontrar a outra extremidade do diâmetro (v) começando de u
    dist_u = bfs(u)
    v = 0
    max_dist = -1
    for i in range(1, n + 1):
        if dist_u[i] > max_dist:
            max_dist = dist_u[i]
            v = i
            
    D = dist_u[v]
    
    # 3. Obter distâncias a partir de v
    dist_v = bfs(v)
    
    # Primeira saída: número de salas do maior ciclo
    # Comprimento do ciclo = Diâmetro + 1
    print(D + 1)
    
    # 4. Contar o número de pares que formam o ciclo máximo
    if D % 2 == 0:
        # Caso par: Centro é um nó único C
        k = D // 2
        C = -1
        # Encontrar C: único nó no caminho u-v com distância k de ambos
        for i in range(1, n + 1):
            if dist_u[i] == k and dist_v[i] == k:
                C = i
                break
        
        # BFS a partir de C para agrupar nós por subárvore
        dist_C = [-1] * (n + 1)
        # root_neighbor[x] armazena o vizinho de C que leva ao nó x
        root_neighbor = [0] * (n + 1)
        
        q = deque([C])
        dist_C[C] = 0
        
        while q:
            curr = q.popleft()
            for neighbor in adj[curr]:
                if dist_C[neighbor] == -1:
                    dist_C[neighbor] = dist_C[curr] + 1
                    if curr == C:
                        root_neighbor[neighbor] = neighbor
                    else:
                        root_neighbor[neighbor] = root_neighbor[curr]
                    q.append(neighbor)
        
        # Contar nós com distância k de C, agrupados pelo vizinho raiz
        counts = {}
        for i in range(1, n + 1):
            if dist_C[i] == k:
                rn = root_neighbor[i]
                if rn != 0:
                    counts[rn] = counts.get(rn, 0) + 1
        
        # Calcular pares: soma de c_i * c_j para i != j
        # Fórmula: (soma^2 - soma_quad) // 2
        total_nodes = sum(counts.values())
        sum_sq = sum(c * c for c in counts.values())
        ways = (total_nodes * total_nodes - sum_sq) // 2
        print(ways)
        
    else:
        # Caso ímpar: Centro é uma aresta (C1, C2)
        k = D // 2 # Isso é (D-1)/2
        
        C1 = -1
        C2 = -1
        # Encontrar C1 e C2
        for i in range(1, n + 1):
            if dist_u[i] == k and dist_v[i] == k + 1:
                C1 = i
            if dist_u[i] == k + 1 and dist_v[i] == k:
                C2 = i
        
        # BFS a partir de C1 e C2
        dist_C1 = bfs(C1)
        dist_C2 = bfs(C2)
        
        cnt1 = 0
        cnt2 = 0
        
        # Contar nós à distância k de C1 e C2
        for i in range(1, n + 1):
            if dist_C1[i] == k:
                cnt1 += 1
            if dist_C2[i] == k:
                cnt2 += 1
        
        print(cnt1 * cnt2)

if __name__ == '__main__':
    solve()
