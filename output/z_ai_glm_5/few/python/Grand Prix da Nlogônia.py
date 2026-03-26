import sys
from collections import deque

# Aumentar o limite de recursão para a construção da Segment Tree
sys.setrecursionlimit(1 << 25)

def solve():
    # Leitura rápida da entrada
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    iterator = iter(input_data)
    try:
        N = int(next(iterator))
        M = int(next(iterator))
    except StopIteration:
        return

    plans = []
    for _ in range(M):
        u = int(next(iterator))
        l = int(next(iterator))
        r = int(next(iterator))
        plans.append((u, l, r))

    # Construção da Segment Tree de saída (Out-Tree)
    # Nós 1 a N são as folhas (vértices originais)
    # Nós internos começam em N+1
    capacity = N + 4 * N + 5
    adj = [[] for _ in range(capacity)]
    in_degree = [0] * capacity
    children = [None] * capacity
    
    node_counter = N
    
    def build(l, r):
        nonlocal node_counter
        if l == r:
            return l
        
        node_counter += 1
        u = node_counter
        mid = (l + r) // 2
        
        left_child = build(l, mid)
        right_child = build(mid + 1, r)
        
        children[u] = (left_child, right_child)
        
        # Arestas da árvore: pai -> filhos
        adj[u].append(left_child)
        adj[u].append(right_child)
        in_degree[left_child] += 1
        in_degree[right_child] += 1
        
        return u

    root = build(1, N)
    total_nodes = node_counter
    
    # Grafo base (apenas arestas da estrutura da Segment Tree)
    base_in_degree = list(in_degree)
    
    # Função para adicionar arestas de um plano U -> [L, R]
    # Usa a estrutura da Segment Tree para decompor o intervalo
    def add_plan_edges(U, L, R, target_in, log):
        def add_rec(node, l, r):
            if r < L or l > R:
                return
            if L <= l and r <= R:
                # Adiciona aresta U -> node
                adj[U].append(node)
                target_in[node] += 1
                log.append(U) # Registra para remoção posterior
                return
            
            # Se for folha e não totalmente coberta, não faz nada (intervalo disjunto)
            if node <= N:
                return

            left_c, right_c = children[node]
            mid = (l + r) // 2
            add_rec(left_c, l, mid)
            add_rec(right_c, mid + 1, r)
        
        add_rec(root, 1, N)

    # Busca Binária na resposta
    low = 1
    high = M
    ans = -1

    while low <= high:
        mid = (low + high) // 2
        
        # Prepara o estado do grafo para o teste 'mid'
        curr_in = list(base_in_degree)
        added_edges_log = []
        
        for i in range(mid):
            u, l, r = plans[i]
            add_plan_edges(u, l, r, curr_in, added_edges_log)
        
        # Verificação de ciclo com Kahn (Topological Sort)
        q = deque()
        for i in range(1, total_nodes + 1):
            if curr_in[i] == 0:
                q.append(i)
        
        count = 0
        while q:
            u_node = q.popleft()
            count += 1
            for v in adj[u_node]:
                curr_in[v] -= 1
                if curr_in[v] == 0:
                    q.append(v)
        
        # Limpeza das arestas adicionadas (remove da lista de adjacência)
        # Como adicionamos com append, removemos com pop (LIFO)
        for u_node in added_edges_log:
            adj[u_node].pop()
        
        # Se nem todos os nós foram visitados, existe ciclo
        if count != total_nodes:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
            
    print(ans)

if __name__ == '__main__':
    solve()