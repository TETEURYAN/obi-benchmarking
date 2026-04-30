
import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    N = int(input_data[0])
    F = [int(x) - 1 for x in input_data[1:N+1]]
    Q = int(input_data[N+1])
    
    # Encontrar o único ciclo no grafo
    visited = [-1] * N
    curr = 0
    while visited[curr] == -1:
        visited[curr] = 1
        curr = F[curr]
    
    C_start = curr
    cycle_nodes = []
    curr = C_start
    while True:
        cycle_nodes.append(curr)
        curr = F[curr]
        if curr == C_start:
            break
            
    pos = [-1] * N
    for idx, node in enumerate(cycle_nodes):
        pos[node] = idx
    L = len(cycle_nodes)
    
    # Determinar a raiz no ciclo e a distância até ela para cada nó
    root = [-1] * N
    dist = [-1] * N
    for c in cycle_nodes:
        root[c] = c
        dist[c] = 0
        
    for i in range(N):
        if root[i] != -1:
            continue
        path = []
        curr = i
        while root[curr] == -1:
            path.append(curr)
            curr = F[curr]
        r = root[curr]
        d = dist[curr]
        for node in reversed(path):
            d += 1
            root[node] = r
            dist[node] = d
            
    # Processar as consultas
    out = []
    idx = N + 2
    for _ in range(Q):
        A = int(input_data[idx]) - 1
        B = int(input_data[idx+1]) - 1
        idx += 2
        
        rA = root[A]
        rB = root[B]
        dA = dist[A]
        dB = dist[B]
        
        if rA == rB:
            # Se estão no mesmo caminho para o ciclo (ou no mesmo nó do ciclo)
            ans = abs(dA - dB)
        else:
            # Se chegam em nós diferentes do ciclo
            pA = pos[rA]
            pB = pos[rB]
            D_AB = (pB - pA) % L
            D_BA = (pA - pB) % L
            
            # Opção 1: Encontrar-se na raiz de A no ciclo
            t1 = dA if dA >= dB + D_BA else dB + D_BA
            # Opção 2: Encontrar-se na raiz de B no ciclo
            t2 = dA + D_AB if dA + D_AB >= dB else dB
            
            ans = t1 if t1 < t2 else t2
            
        out.append(str(ans))
        
    sys.stdout.write('\n'.join(out) + '\n')

if __name__ == '__main__':
    solve()
