import sys

# Aumentar o limite de recursão para segurança, embora para N <= 36 seja desnecessário.
sys.setrecursionlimit(200000)

def main():
    # Leitura rápida de toda a entrada
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return

    iterator = iter(input_data)
    
    try:
        L = int(next(iterator))
        C = int(next(iterator))
        P = int(next(iterator))
    except StopIteration:
        return

    # Conjunto para armazenar as posições das peças pretas
    black_pieces = set()
    for _ in range(P):
        r = int(next(iterator))
        c = int(next(iterator))
        black_pieces.add((r, c))

    # Identificar candidatos para peças brancas
    # Um candidato deve:
    # 1. Estar vazio (não ter peça preta)
    # 2. Ter pelo menos um vizinho preto
    candidates = []
    
    # Direções: cima, baixo, esquerda, direita
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    for r in range(1, L + 1):
        for c in range(1, C + 1):
            if (r, c) in black_pieces:
                continue
            
            has_black_neighbor = False
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if (nr, nc) in black_pieces:
                    has_black_neighbor = True
                    break
            
            if has_black_neighbor:
                candidates.append((r, c))

    # Se não houver candidatos, a resposta é 0
    if not candidates:
        print(0)
        return

    # O problema se resume a encontrar o Conjunto Independente Máximo em um grafo
    # onde os vértices são os candidatos e arestas conectam candidatos adjacentes.
    # Como o grafo é uma grade (bidirecional), ele é bipartido.
    # MIS em grafo bipartido = Total de Vértices - Emparelhamento Máximo.
    
    # Mapear candidatos para índices
    pos_to_idx = {pos: i for i, pos in enumerate(candidates)}
    K = len(candidates)
    
    # Construir o grafo bipartido
    # Divisão baseada na paridade da soma das coordenadas (r + c)
    # Grupo A: (r + c) par
    # Grupo B: (r + c) ímpar
    
    adj = [[] for _ in range(K)]
    candidate_set = set(candidates)
    nodes_A = []
    
    for i, (r, c) in enumerate(candidates):
        if (r + c) % 2 == 0:
            nodes_A.append(i)
            # Verificar vizinhos para construir arestas
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if (nr, nc) in candidate_set:
                    # Vizinho sempre terá paridade oposta
                    neighbor_idx = pos_to_idx[(nr, nc)]
                    adj[i].append(neighbor_idx)

    # Algoritmo de Kuhn para Emparelhamento Máximo
    match = [-1] * K
    
    def dfs(u, visited):
        for v in adj[u]:
            if visited[v]:
                continue
            visited[v] = True
            if match[v] == -1 or dfs(match[v], visited):
                match[v] = u
                return True
        return False

    matching_size = 0
    for u in nodes_A:
        visited = [False] * K
        if dfs(u, visited):
            matching_size += 1

    # Resultado: |Candidatos| - |Emparelhamento Máximo|
    print(K - matching_size)

if __name__ == '__main__':
    main()