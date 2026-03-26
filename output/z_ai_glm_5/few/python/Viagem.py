
import sys
import heapq

def solve():
    # Leitura rápida de todos os dados de entrada
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return

    iterator = iter(input_data)
    
    try:
        # V: valor máximo disponível, N: número de ilhas, M: número de rotas
        V = int(next(iterator))
        N = int(next(iterator))
        M = int(next(iterator))
    except StopIteration:
        return

    # Lista de adjacência para o grafo
    adj = [[] for _ in range(N + 1)]
    
    # Leitura das M rotas
    for _ in range(M):
        try:
            u = int(next(iterator))
            v = int(next(iterator))
            t = int(next(iterator))  # Tempo
            p = int(next(iterator))  # Custo
            adj[u].append((v, t, p))
            adj[v].append((u, t, p))
        except StopIteration:
            break
            
    try:
        # X: origem, Y: destino
        X = int(next(iterator))
        Y = int(next(iterator))
    except StopIteration:
        return

    # Dijkstra com estado de custo
    # O estado é (tempo, ilha, custo_atual)
    # O custo máximo é V (pequeno, até 200), então podemos usar um array para distâncias
    # dist[u * (V + 1) + c] representa o menor tempo para chegar em u com custo c.
    
    INF = float('inf')
    # Tamanho do array de distâncias: (N+1) ilhas * (V+1) possíveis custos
    dist = [INF] * ((N + 1) * (V + 1))
    
    # Estado inicial: tempo 0, ilha X, custo 0
    start_idx = X * (V + 1)
    dist[start_idx] = 0
    
    # Fila de prioridade (min-heap): (tempo, ilha, custo)
    pq = [(0, X, 0)]
    
    while pq:
        current_time, u, current_cost = heapq.heappop(pq)
        
        # Índice linear para o estado atual
        u_idx = u * (V + 1) + current_cost
        
        # Se já encontramos um caminho melhor para este estado, ignoramos
        if current_time > dist[u_idx]:
            continue
        
        # Se chegamos ao destino, como Dijkstra ordena por tempo, este é o menor tempo possível
        if u == Y:
            print(current_time)
            return
            
        # Explorar vizinhos
        for v, t_edge, p_edge in adj[u]:
            new_cost = current_cost + p_edge
            
            # Verificar se o custo não excede o orçamento
            if new_cost <= V:
                new_time = current_time + t_edge
                v_idx = v * (V + 1) + new_cost
                
                # Relaxamento
                if new_time < dist[v_idx]:
                    dist[v_idx] = new_time
                    heapq.heappush(pq, (new_time, v, new_cost))
    
    # Se a fila esvaziar sem chegar em Y, não é possível
    print(-1)

if __name__ == '__main__':
    solve()
