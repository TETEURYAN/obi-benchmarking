import sys

# Aumentar o limite de recursão é uma boa prática, embora Union-Find seja iterativo aqui
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

    points = []
    for _ in range(n):
        x = int(next(iterator))
        y = int(next(iterator))
        points.append((x, y))
    
    a = int(next(iterator))
    
    # Otimização baseada na geometria do problema.
    # O mapa é limitado a [0, 1000] x [0, 1000].
    # A distância máxima possível entre dois pontos é a diagonal: sqrt(1000^2 + 1000^2) approx 1414.21.
    # Se o alcance A for >= 1415, qualquer torre alcança qualquer outra.
    # O grafo será completo, logo conexo.
    if a >= 1415:
        print("S")
        return

    # Estrutura Union-Find (Disjoint Set Union)
    parent = list(range(n))
    rank = [0] * n
    num_components = n

    def find(i):
        # Path compression
        if parent[i] == i:
            return i
        parent[i] = find(parent[i])
        return parent[i]

    def union(i, j):
        nonlocal num_components
        root_i = find(i)
        root_j = find(j)
        if root_i != root_j:
            # Union by rank
            if rank[root_i] < rank[root_j]:
                parent[root_i] = root_j
            elif rank[root_i] > rank[root_j]:
                parent[root_j] = root_i
            else:
                parent[root_j] = root_i
                rank[root_i] += 1
            num_components -= 1
            return True
        return False

    # Otimização espacial (Spatial Hashing / Grid)
    # Dividimos o mapa em baldes de tamanho A.
    # Uma torre só pode se conectar a torres no mesmo balde ou em baldes adjacentes.
    buckets = {}
    
    for i in range(n):
        x, y = points[i]
        # Índice do balde
        bx = x // a
        by = y // a
        if (bx, by) not in buckets:
            buckets[(bx, by)] = []
        buckets[(bx, by)].append(i)
        
    a_sq = a * a

    # Iterar sobre cada torre para verificar conexões
    for i in range(n):
        x, y = points[i]
        bx = x // a
        by = y // a
        
        # Verificar os 9 baldes possíveis (atual + 8 vizinhos)
        for dx in range(-1, 2):
            for dy in range(-1, 2):
                target_bucket = (bx + dx, by + dy)
                if target_bucket in buckets:
                    for j in buckets[target_bucket]:
                        # Evitar contar duplicatas e auto-conexão
                        if j > i:
                            x2, y2 = points[j]
                            # Otimização: comparar quadrados das distâncias evita sqrt
                            dist_sq = (x - x2)**2 + (y - y2)**2
                            if dist_sq <= a_sq:
                                union(i, j)
                                # Se tudo já está conectado, podemos parar e imprimir 'S'
                                if num_components == 1:
                                    print("S")
                                    return
    
    # Verificação final da conectividade
    if num_components == 1:
        print("S")
    else:
        print("N")

if __name__ == "__main__":
    solve()