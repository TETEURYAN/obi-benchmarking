import sys
import heapq

# Aumentar o limite de recursão, embora não seja estritamente necessário para Dijkstra
sys.setrecursionlimit(200000)

def solve():
    # Leitura rápida de toda a entrada
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return

    iterator = iter(input_data)
    
    try:
        N = int(next(iterator))
        M = int(next(iterator))
        K = int(next(iterator))
    except StopIteration:
        return

    # Preços dos sistemas (1-based index)
    P = [0] * (K + 1)
    for i in range(1, K + 1):
        P[i] = int(next(iterator))
    
    # Leitura das arestas
    edges = []
    for _ in range(M):
        u = int(next(iterator))
        v = int(next(iterator))
        t = int(next(iterator))
        edges.append((u, v, t))
        
    try:
        A = int(next(iterator))
        B = int(next(iterator))
    except StopIteration:
        return

    # Mapeamento de estados (estação, sistema) para um ID de nó único.
    # Os nós 1 a N representam as estações.
    # Os nós a partir de N+1 representam os estados "estar na estação u dentro do sistema t".
    state_map = {}
    next_node_id = N + 1
    
    # Atribuir IDs para os estados
    for u, v, t in edges:
        if (u, t) not in state_map:
            state_map[(u, t)] = next_node_id
            next_node_id += 1
        if (v, t) not in state_map:
            state_map[(v, t)] = next_node_id
            next_node_id += 1
            
    # Lista de adjacência para o grafo expandido
    adj = [[] for _ in range(next_node_id)]
    
    # Adicionar arestas de movimento dentro do sistema (custo 0)
    # Aresta entre (u, t) e (v, t)
    for u, v, t in edges:
        u_id = state_map[(u, t)]
        v_id = state_map[(v, t)]
        adj[u_id].append((v_id, 0))
        adj[v_id].append((u_id, 0))
        
    # Adicionar arestas de entrada e saída de sistemas
    # Estação u -> Estado (u, t): custo P[t] (entrar no sistema)
    # Estado (u, t) -> Estação u: custo 0 (sair do sistema)
    for (u, t), node_id in state_map.items():
        cost = P[t]
        adj[u].append((node_id, cost))
        adj[node_id].append((u, 0))
        
    # Algoritmo de Dijkstra
    INF = float('inf')
    dist = [INF] * next_node_id
    dist[A] = 0
    pq = [(0, A)]
    
    while pq:
        d, u = heapq.heappop(pq)
        
        if d > dist[u]:
            continue
        
        # Se chegarmos ao destino B, podemos parar pois Dijkstra garante o menor caminho
        if u == B:
            break
        
        for v, w in adj[u]:
            if dist[v] > d + w:
                dist[v] = d + w
                heapq.heappush(pq, (dist[v], v))
                
    if dist[B] == INF:
        print(-1)
    else:
        print(dist[B])

if __name__ == '__main__':
    solve()