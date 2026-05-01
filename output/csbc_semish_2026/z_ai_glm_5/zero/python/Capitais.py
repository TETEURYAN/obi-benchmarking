
import sys

# Aumentar o limite de recursão para lidar com árvores profundas (até 10^5 nós)
sys.setrecursionlimit(300000)

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

    # Caso trivial embora o problema garanta N >= 2
    if N < 2:
        print(0)
        return

    # Lista de adjacência e graus
    adj = [[] for _ in range(N + 1)]
    degree = [0] * (N + 1)

    for _ in range(N - 1):
        try:
            u = int(next(iterator))
            v = int(next(iterator))
        except StopIteration:
            break
        
        adj[u].append(v)
        adj[v].append(u)
        degree[u] += 1
        degree[v] += 1

    # in_dist[u]: distância de u para a folha mais próxima em sua subárvore
    in_dist = [0] * (N + 1)
    
    # Primeira DFS: calcular in_dist
    def dfs1(u, p):
        # Se é folha (grau 1), a distância para a folha mais próxima na subárvore é 0 (ele mesmo)
        if degree[u] == 1:
            in_dist[u] = 0
            return

        min_val = float('inf')
        for v in adj[u]:
            if v != p:
                dfs1(v, u)
                if in_dist[v] < min_val:
                    min_val = in_dist[v]
        
        in_dist[u] = min_val + 1

    # Raiz da árvore pode ser qualquer nó, escolhemos 1 (assumindo grafo conectado e nós 1..N)
    dfs1(1, 0)

    # Variável global para armazenar a menor distância encontrada
    min_ans = float('inf')

    # Segunda DFS: calcular up_val (distância para folha mais próxima fora da subárvore)
    # e atualizar a resposta mínima.
    def dfs2(u, p, up_val):
        nonlocal min_ans
        
        # A menor distância entre pares de folhas passando por u (ou tendo u como LCA implícito na rota)
        # é a soma das duas menores distâncias para folhas chegando em u.
        # Essas distâncias vêm de: in_dist dos filhos e up_val (vindo do pai).
        
        # Coletar todas as distâncias de vizinhos
        dists = []
        
        # Se up_val não for infinito, é uma distância válida vinda de "cima"
        if up_val != float('inf'):
            dists.append(up_val)
            
        for v in adj[u]:
            if v != p:
                dists.append(in_dist[v] + 1)
        
        # Para haver um caminho entre duas capitais (folhas) passando por u,
        # u deve conectar pelo menos duas direções distintas com folhas.
        if len(dists) >= 2:
            dists.sort()
            current_min = dists[0] + dists[1]
            if current_min < min_ans:
                min_ans = current_min
        
        # Preparar valores para passar para os filhos
        # Encontramos os dois menores valores em dists para otimizar o cálculo do up_val dos filhos
        # m1: menor valor, m2: segundo menor valor
        m1 = float('inf')
        m2 = float('inf')
        for d in dists:
            if d < m1:
                m2 = m1
                m1 = d
            elif d < m2:
                m2 = d
        
        # Recursão para os filhos
        for v in adj[u]:
            if v != p:
                # Calcular o up_val para o filho v
                # O up_val de v é 1 + min(distância de u para folha que NÃO passa por v)
                
                # A contribuição vindo do filho v para u é (in_dist[v] + 1)
                val_from_v = in_dist[v] + 1
                
                # Verificamos se o caminho mais curto de u para uma folha passava por v
                # Se sim, usamos o segundo menor caminho (m2). Caso contrário, usamos o menor (m1).
                best_from_u = m2 if (val_from_v == m1) else m1
                
                # Se u é uma folha (grau 1), ele próprio é uma capital.
                # Isso é tratado implicitamente pois up_val virá de m1/m2 ou da inicialização.
                # Mas precisamos cuidar se best_from_u é infinito (ex: árvore linha e subindo para a raiz)
                
                next_up = best_from_u + 1
                dfs2(v, u, next_up)

    # Iniciar a segunda DFS a partir da raiz 1.
    # A raiz 1 não tem pai, então up_val inicial é infinito.
    dfs2(1, 0, float('inf'))

    print(min_ans)

if __name__ == '__main__':
    solve()
