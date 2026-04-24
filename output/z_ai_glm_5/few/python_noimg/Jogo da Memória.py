import sys

# Aumentar o limite de recursão para lidar com árvores de até 50.000 nós
sys.setrecursionlimit(200000)

def main():
    # Leitura rápida de toda a entrada
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return

    iterator = iter(input_data)
    
    try:
        n_str = next(iterator)
        n = int(n_str)
    except StopIteration:
        return

    # Leitura das cartas e mapeamento dos pares
    # Encontra os índices (base 1) de cada par de cartas iguais
    pair_indices = {}
    for i in range(1, n + 1):
        val = int(next(iterator))
        if val not in pair_indices:
            pair_indices[val] = []
        pair_indices[val].append(i)
    
    # Construção do grafo (lista de adjacência)
    adj = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        u = int(next(iterator))
        v = int(next(iterator))
        adj[u].append(v)
        adj[v].append(u)
    
    # Preparação para LCA (Binary Lifting)
    # LOG = 16 é suficiente para 2^16 = 65536 > 50000
    LOG = 16
    up = [[0] * (n + 1) for _ in range(LOG)]
    depth = [0] * (n + 1)
    
    # DFS para preencher profundidade e tabela 'up'
    def dfs(u, p):
        up[0][u] = p
        for i in range(1, LOG):
            up[i][u] = up[i-1][up[i-1][u]]
        
        for v in adj[u]:
            if v != p:
                depth[v] = depth[u] + 1
                dfs(v, u)
    
    # Raiz em 1, pai de 1 é 1 (para evitar índice 0)
    dfs(1, 1)
    
    # Função para encontrar o LCA de dois nós
    def lca(u, v):
        if depth[u] < depth[v]:
            u, v = v, u
        
        diff = depth[u] - depth[v]
        for i in range(LOG):
            if (diff >> i) & 1:
                u = up[i][u]
        
        if u == v:
            return u
        
        for i in range(LOG - 1, -1, -1):
            if up[i][u] != up[i][v]:
                u = up[i][u]
                v = up[i][v]
        
        return up[0][u]
    
    # Array para a técnica de diferença nas arestas
    # val[u] guarda o valor a ser somado para a subárvore de u
    val = [0] * (n + 1)
    
    # Processar cada par de cartas
    for k in range(1, n // 2 + 1):
        u, v = pair_indices[k]
        ancestor = lca(u, v)
        
        val[u] += 1
        val[v] += 1
        val[ancestor] -= 2
    
    total_distance = 0
    
    # Segunda DFS para calcular a soma acumulada e a resposta
    def solve(u, p):
        nonlocal total_distance
        current_sum = val[u]
        
        for v in adj[u]:
            if v != p:
                child_sum = solve(v, u)
                current_sum += child_sum
        
        # A soma acumulada em 'u' (exceto a raiz) representa o número de caminhos
        # que passam pela aresta (p -> u). Isso contribui para a distância total.
        if u != 1:
            total_distance += current_sum
            
        return current_sum
    
    solve(1, 1)
    
    print(total_distance)

if __name__ == "__main__":
    main()