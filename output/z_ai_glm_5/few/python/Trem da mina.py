import sys
import heapq

# Aumentar o limite de recursão para grafos profundos (embora a estrutura seja cactus, árvores podem ser profundas)
sys.setrecursionlimit(30000)

def solve():
    # Leitura rápida de toda a entrada
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    iterator = iter(input_data)
    try:
        E = int(next(iterator))
        R = int(next(iterator))
    except StopIteration:
        return

    # Lista de adjacência: adj[u] = [(v, weight, edge_idx), ...]
    adj = [[] for _ in range(E + 1)]
    # Lista de arestas: edges[i] = (u, v, weight)
    edges = []
    
    for i in range(R):
        u = int(next(iterator))
        v = int(next(iterator))
        w = int(next(iterator))
        adj[u].append((v, w, i))
        adj[v].append((u, w, i))
        edges.append((u, v, w))

    # Passo 1: Identificar pontes e ciclos
    # Como cada estação pertence a no máximo um ciclo, podemos usar uma abordagem de remoção de folhas (peeling)
    # para encontrar o "core" do grafo (que contém os ciclos).
    
    degree = [0] * (E + 1)
    for u in range(1, E + 1):
        degree[u] = len(adj[u])
    
    # Fila para processar nós de grau 1 (folhas)
    q = []
    is_tree_node = [False] * (E + 1)
    is_bridge = [False] * R
    
    for u in range(1, E + 1):
        if degree[u] == 1:
            q.append(u)
    
    head = 0
    while head < len(q):
        u = q[head]
        head += 1
        is_tree_node[u] = True
        
        for v, w, idx in adj[u]:
            if not is_bridge[idx]:
                is_bridge[idx] = True
                degree[v] -= 1
                if degree[v] == 1:
                    q.append(v)

    # Passo 2: Extrair ciclos do grafo restante (core)
    # Nós restantes (não são tree_nodes) fazem parte de ciclos.
    # Como cada nó pertence a no máximo um ciclo, o core é uma floresta de ciclos (possivelmente conectados por pontes não removidas).
    
    cycle_id = [-1] * (E + 1) # ID do ciclo ao qual o nó pertence (-1 se nenhum)
    cycles = [] # Lista de dicionários: {'len': int, 'nodes': list}
    
    visited = [False] * (E + 1)
    
    # DFS no core para encontrar os ciclos
    # Precisamos diferenciar arestas de ciclo de pontes entre ciclos no core.
    # Usaremos entrada/saída (tin/tout) para detectar arestas de retorno (back edges) que formam ciclos.
    # Estado: 0 = não visitado, 1 = visitando (na pilha), 2 = processado
    state = [0] * (E + 1)
    parent_edge = [-1] * (E + 1) # Índice da aresta que levou a este nó
    parent_node = [-1] * (E + 1)
    
    # Pilha para DFS iterativa para evitar estouro de recursão se o core for grande (improvável, mas seguro)
    # Na verdade, a estrutura garante que o core é pequeno ou simples. Recursão com limite alto funciona.
    
    def find_cycle(u, p_node, p_edge):
        # Marca como visitando
        state[u] = 1
        parent_node[u] = p_node
        parent_edge[u] = p_edge
        
        for v, w, idx in adj[u]:
            # Ignorar arestas que já sabemos que são pontes (da fase de peeling)
            if is_bridge[idx]:
                continue
            
            if state[v] == 0:
                # Recursão
                find_cycle(v, u, idx)
            elif state[v] == 1 and v != p_node:
                # Encontrou uma aresta de retorno (back edge) para um ancestral.
                # Isso define um ciclo.
                # O ciclo é: v -> ... -> u -> v
                # Reconstruir o ciclo subindo de u até v
                curr_cycle_len = w
                curr_cycle_nodes = []
                
                curr = u
                while curr != v:
                    curr_cycle_nodes.append(curr)
                    # Adicionar o peso da aresta que conecta curr ao seu pai na árvore DFS
                    # A aresta é parent_edge[curr]
                    pe = parent_edge[curr]
                    if pe != -1:
                        # Encontrar o peso da aresta pe
                        # Arestas são armazenadas como (u, v, w). pe é o índice.
                        u_pe, v_pe, w_pe = edges[pe]
                        curr_cycle_len += w_pe
                    curr = parent_node[curr]
                
                curr_cycle_nodes.append(v)
                
                # Registrar o ciclo
                cid = len(cycles)
                cycles.append({'len': curr_cycle_len, 'nodes': curr_cycle_nodes})
                
                for node in curr_cycle_nodes:
                    cycle_id[node] = cid
                    
                # Marcar as arestas deste ciclo?
                # Não é estritamente necessário marcar as arestas do ciclo como "não ponte" aqui,
                # porque o Dijkstra só usa pontes. Mas precisamos saber quais nós são de ciclos.
                # cycle_id já faz isso.
                
            # Se state[v] == 2, é uma aresta transversal ou ponta de outro ciclo já processado.
            # Como cada nó pertence a no máximo 1 ciclo, arestas entre ciclos (state 2) são pontes.
            # Não precisamos fazer nada especial, pois is_bridge já é False para elas,
            # mas o Dijkstra tratará como aresta comum (peso 2*W).
        
        state[u] = 2

    # Executar DFS para encontrar ciclos
    for u in range(1, E + 1):
        if not is_tree_node[u] and state[u] == 0:
            find_cycle(u, -1, -1)

    # Passo 3: Construir o grafo de pontes para Dijkstra
    # O grafo para Dijkstra contém apenas as pontes (com peso 2*W) e nós.
    # Nós de ciclo são fontes potenciais.
    
    bridge_adj = [[] for _ in range(E + 1)]
    for idx, (u, v, w) in enumerate(edges):
        if is_bridge[idx]:
            bridge_adj[u].append((v, 2 * w))
            bridge_adj[v].append((u, 2 * w))
        else:
            # Se não é ponte, é aresta de ciclo.
            # Verificar se conecta dois nós do mesmo ciclo.
            # Se sim, não entra no grafo de pontes.
            # Se conecta nós de ciclos diferentes (impossível pela restrição "max 1 ciclo por estação"? 
            # Não, estações de ciclos diferentes são ligadas por pontes. 
            # Se is_bridge é False, ou é aresta de ciclo ou bug.
            # O peeling removeu as pontes de árvores. 
            # A DFS identificou as arestas de ciclo.
            # Arestas no core que não são de ciclo seriam pontes entre ciclos.
            # Mas o peeling não as removeu porque o grau não baixou para 1?
            # Exemplo: Ciclo A -- Ciclo B. Nó de conexão tem grau 2 no ciclo + 1 ponte = 3.
            # Peeling não remove. DFS encontra Ciclo A e Ciclo B.
            # A aresta entre eles... como é tratada?
            # Na DFS, se vamos de A para B, B é visitado (state 0), recursão.
            # Se voltamos de B para A (outra aresta), A é state 2 (processado).
            # Essa aresta não é marcada como ciclo. Ela permanece is_bridge=False.
            # Mas ela funciona como uma ponte no Dijkstra.
            # Para o Dijkstra, qualquer caminho que não seja "entrar no ciclo" é ponte.
            # Simplificação: Vamos adicionar TODAS as arestas que NÃO são de ciclo ao grafo de pontes?
            # Não. Arestas de ciclo não devem ser traversadas no Dijkstra (exceto como fonte).
            # Arestas entre ciclos DEVEM ser traversadas.
            # Como distinguir?
            # Se (u, v) tem cycle_id[u] != -1 e cycle_id[v] != -1 e cycle_id[u] != cycle_id[v], é ponte entre ciclos.
            # Se cycle_id[u] == cycle_id[v], é aresta de ciclo (ignorar).
            # Se um dos dois é tree_node, é ponte (já marcada is_bridge=True).
            
            cid_u = cycle_id[u]
            cid_v = cycle_id[v]
            
            if cid_u != -1 and cid_v != -1 and cid_u != cid_v:
                # Ponte entre ciclos
                bridge_adj[u].append((v, 2 * w))
                bridge_adj[v].append((u, 2 * w))
            elif cid_u != -1 or cid_v != -1:
                # Um é de ciclo, outro não.
                # Se o não-ciclo é tree_node, is_bridge já é True.
                # Se o não-ciclo é... o que mais? Apenas tree_node ou ciclo.
                # Se is_bridge é False aqui, significa que o peeling não pegou.
                # Isso só acontece se for aresta de ciclo ou ponte entre ciclos.
                # Se chegou aqui, is_bridge é False.
                # Se cid_u == -1 e cid_v != -1 (ou vice versa), então u é tree_node?
                # Se u é tree_node, is_bridge deveria ser True.
                # Conclusão: Se is_bridge é False, ou é aresta de ciclo, ou ponte entre ciclos.
                # O código acima cobre ponte entre ciclos.
                # Arestas de ciclo (cid_u == cid_v) são ignoradas.
                pass

    # Passo 4: Processar consultas
    K = int(next(iterator))
    queries = []
    # Agrupar consultas por T para rodar Dijkstra em batch
    # T <= 100
    query_indices_by_T = [[] for _ in range(101)]
    
    for k_idx in range(K):
        X = int(next(iterator))
        T = int(next(iterator))
        queries.append((X, T))
        if T <= 100:
            query_indices_by_T[T].append(k_idx)
            
    results = [-1] * K
    
    # Pré-calcular quais ciclos são válidos para cada T
    # cycle_valid_for_T[t] = lista de IDs de ciclos com comprimento >= t
    cycle_valid_for_T = [[] for _ in range(101)]
    for cid, c_data in enumerate(cycles):
        clen = c_data['len']
        # Ciclo é válido para todos T <= clen
        for t in range(1, min(100, clen) + 1):
            cycle_valid_for_T[t].append(cid)
            
    # Executar Dijkstra para cada T necessário
    for t in range(1, 101):
        if not query_indices_by_T[t]:
            continue
        
        valid_cids = cycle_valid_for_T[t]
        if not valid_cids:
            # Sem ciclos válidos para este T, todos os resultados são -1
            for k_idx in query_indices_by_T[t]:
                results[k_idx] = -1
            continue
        
        # Dijkstra Multi-fonte
        dist = [float('inf')] * (E + 1)
        pq = []
        
        # Inicializar fontes
        for cid in valid_cids:
            clen = cycles[cid]['len']
            for node in cycles[cid]['nodes']:
                if dist[node] > clen:
                    dist[node] = clen
                    heapq.heappush(pq, (clen, node))
        
        # Processar
        while pq:
            d, u = heapq.heappop(pq)
            if d > dist[u]:
                continue
            
            for v, w in bridge_adj[u]:
                if dist[v] > d + w:
                    dist[v] = d + w
                    heapq.heappush(pq, (dist[v], v))
        
        # Responder consultas
        for k_idx in query_indices_by_T[t]:
            X, _ = queries[k_idx]
            ans = dist[X]
            if ans == float('inf'):
                results[k_idx] = -1
            else:
                results[k_idx] = ans

    # Imprimir resultados
    out = []
    for res in results:
        out.append(str(res))
    print('\n'.join(out))

if __name__ == '__main__':
    solve()