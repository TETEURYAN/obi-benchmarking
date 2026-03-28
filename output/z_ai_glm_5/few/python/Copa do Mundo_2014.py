import sys

def solve():
    # Leitura rápida de toda a entrada
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    iterator = iter(input_data)
    
    try:
        N = int(next(iterator))
        F = int(next(iterator))
        R = int(next(iterator))
    except StopIteration:
        return

    edges = []

    # Leitura das Ferrovias (prioridade 0)
    for _ in range(F):
        u = int(next(iterator))
        v = int(next(iterator))
        c = int(next(iterator))
        edges.append((0, c, u, v))

    # Leitura das Rodovias (prioridade 1)
    for _ in range(R):
        u = int(next(iterator))
        v = int(next(iterator))
        c = int(next(iterator))
        edges.append((1, c, u, v))

    # Ordenação: primeiro por tipo (ferrovias antes), depois por custo
    edges.sort()

    # Estrutura Union-Find (DSU)
    parent = list(range(N + 1))
    rank = [0] * (N + 1)

    def find(i):
        if parent[i] != i:
            parent[i] = find(parent[i])
        return parent[i]

    def union(i, j):
        root_i = find(i)
        root_j = find(j)
        if root_i != root_j:
            if rank[root_i] < rank[root_j]:
                parent[root_i] = root_j
            elif rank[root_i] > rank[root_j]:
                parent[root_j] = root_i
            else:
                parent[root_i] = root_j
                rank[root_j] += 1
            return True
        return False

    total_cost = 0
    edges_used = 0

    # Algoritmo de Kruskal
    for typ, cost, u, v in edges:
        if union(u, v):
            total_cost += cost
            edges_used += 1
            if edges_used == N - 1:
                break

    print(total_cost)

if __name__ == '__main__':
    solve()