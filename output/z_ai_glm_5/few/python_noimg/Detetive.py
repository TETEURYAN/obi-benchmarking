import sys
from collections import deque

def solve():
    # Leitura rápida de toda a entrada
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    iterator = iter(input_data)
    
    try:
        E = int(next(iterator))
        I = int(next(iterator))
        V = int(next(iterator))
    except StopIteration:
        return

    # Grafo de implicações diretas (A -> B)
    adj = [[] for _ in range(E + 1)]
    # Lista de pais (causas) para cada evento (reverso de adj)
    parents = [[] for _ in range(E + 1)]

    for _ in range(I):
        A = int(next(iterator))
        B = int(next(iterator))
        adj[A].append(B)
        parents[B].append(A)

    # Eventos inicialmente determinados verdadeiros
    is_true = [False] * (E + 1)
    queue = deque()

    for _ in range(V):
        Xi = int(next(iterator))
        if not is_true[Xi]:
            is_true[Xi] = True
            queue.append(Xi)

    # Processamento
    while queue:
        u = queue.popleft()

        # Propagação direta: se A é verdade, e A -> B, então B é verdade
        for v in adj[u]:
            if not is_true[v]:
                is_true[v] = True
                queue.append(v)
        
        # Propagação reversa: se B é verdade e B tem exatamente uma causa A,
        # então A deve ser verdade.
        # Lógica: "se um evento é consequência de pelo menos uma causa, 
        # então ele só pode ocorrer se pelo menos uma de suas causas ocorrer também."
        # Se temos apenas 1 causa, ela é a única opção para satisfazer a ocorrência.
        if len(parents[u]) == 1:
            p = parents[u][0]
            if not is_true[p]:
                is_true[p] = True
                queue.append(p)

    # Construção da saída
    result = []
    for i in range(1, E + 1):
        if is_true[i]:
            result.append(str(i))
    
    print(" ".join(result))

if __name__ == "__main__":
    solve()