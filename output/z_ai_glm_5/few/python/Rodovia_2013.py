import sys

def solve():
    # Leitura rápida de toda a entrada
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return

    iterator = iter(input_data)
    
    try:
        n_str = next(iterator)
        N = int(n_str)
    except StopIteration:
        return

    # Estruturas de dados
    # adj[u] guarda o destino da aresta que sai de u
    adj = [0] * (N + 1)
    in_deg = [0] * (N + 1)
    out_deg = [0] * (N + 1)
    
    # Leitura das N arestas
    for _ in range(N):
        try:
            u = int(next(iterator))
            v = int(next(iterator))
        except StopIteration:
            break
            
        adj[u] = v
        in_deg[v] += 1
        out_deg[u] += 1
        
    # Verificação dos graus
    # Para que o grafo seja fortemente conexo com N arestas e N vértices,
    # é necessário que cada vértice tenha grau de entrada e saída igual a 1.
    for i in range(1, N + 1):
        if in_deg[i] != 1 or out_deg[i] != 1:
            print("N")
            return
            
    # Verificação da conectividade
    # Como cada vértice tem exatamente uma aresta de saída, o grafo é composto por ciclos disjuntos.
    # Se conseguirmos visitar N vértices partindo de um deles, existe apenas um ciclo (ou um grande ciclo),
    # o que significa que o grafo é fortemente conexo.
    visited = [False] * (N + 1)
    curr = 1
    count = 0
    
    while not visited[curr]:
        visited[curr] = True
        count += 1
        curr = adj[curr]
        
    if count == N:
        print("S")
    else:
        print("N")

if __name__ == '__main__':
    solve()