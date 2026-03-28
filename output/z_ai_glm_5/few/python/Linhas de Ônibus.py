import sys
from collections import deque

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    iterator = iter(input_data)
    
    try:
        T = int(next(iterator))
        L = int(next(iterator))
        O = int(next(iterator))
        D = int(next(iterator))
    except StopIteration:
        return

    # Grafo bipartido: Terminais (1 a T) e Linhas (T+1 a T+L)
    # Total de nós: T + L
    adj = [[] for _ in range(T + L + 1)]
    
    for i in range(1, L + 1):
        try:
            C = int(next(iterator))
            line_node = T + i
            for _ in range(C):
                terminal = int(next(iterator))
                adj[line_node].append(terminal)
                adj[terminal].append(line_node)
        except StopIteration:
            break
            
    # BFS para encontrar o caminho mínimo
    dist = [-1] * (T + L + 1)
    q = deque([O])
    dist[O] = 0
    
    while q:
        u = q.popleft()
        
        if u == D:
            break
        
        for v in adj[u]:
            if dist[v] == -1:
                dist[v] = dist[u] + 1
                q.append(v)
                
    # O caminho é Terminal -> Linha -> Terminal -> ...
    # O número de arestas é dist[D]. O número de linhas é metade desse valor.
    print(dist[D] // 2)

if __name__ == "__main__":
    solve()