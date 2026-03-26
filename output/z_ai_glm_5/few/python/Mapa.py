import sys

# O problema descreve uma árvore (grafo conexo acíclico).
# O objetivo é calcular o número de pares de nós (A, B) tal que o caminho
# entre eles contenha pelo menos uma aresta "importante" (C=1).
#
# Estratégia:
# O total de pares de nós é N*(N-1)/2.
# É mais fácil calcular o número de pares que NÃO possuem arestas importantes (U)
# e subtrair do total: E = Total - U.
# Um par (A, B) não tem arestas importantes se o caminho entre eles é feito
# inteiramente por arestas "não importantes" (C=0).
# Isso significa que A e B pertencem à mesma componente conexa se considerarmos
# apenas as arestas C=0.
# Portanto, calculamos os tamanhos das componentes conexas no subgrafo de arestas C=0.
# Se uma componente tem tamanho K, ela contribui com K*(K-1)/2 pares para U.

# Aumentar o limite de recursão para segurança, embora a implementação use DSU iterativo.
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

    # Inicialização do DSU (Union-Find)
    parent = list(range(n + 1))
    size = [1] * (n + 1)

    def find(i):
        # Função find iterativa com compressão de caminho
        root = i
        while parent[root] != root:
            root = parent[root]
        
        # Compressão do caminho
        while i != root:
            temp = parent[i]
            parent[i] = root
            i = temp
            
        return root

    def union(i, j):
        root_i = find(i)
        root_j = find(j)
        if root_i != root_j:
            # Union by size
            if size[root_i] < size[root_j]:
                root_i, root_j = root_j, root_i
            parent[root_j] = root_i
            size[root_i] += size[root_j]

    # Processamento das N-1 arestas
    for _ in range(n - 1):
        try:
            u = int(next(iterator))
            v = int(next(iterator))
            c = int(next(iterator))
            
            # Se a aresta não é importante (C=0), unimos os nós
            if c == 0:
                union(u, v)
        except StopIteration:
            break
            
    # Contagem dos tamanhos das componentes
    component_counts = {}
    for i in range(1, n + 1):
        root = find(i)
        component_counts[root] = component_counts.get(root, 0) + 1
        
    # Cálculo dos pares sem arestas importantes (U)
    unimportant_pairs = 0
    for count in component_counts.values():
        if count >= 2:
            unimportant_pairs += count * (count - 1) // 2
            
    # Total de pares
    total_pairs = n * (n - 1) // 2
    
    # Resultado
    result = total_pairs - unimportant_pairs
    
    print(result)

if __name__ == "__main__":
    solve()