import sys
sys.setrecursionlimit(200000)

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    N = int(next(it))
    M = int(next(it))
    K = int(next(it))
    
    # Matriz de observação: 0 = livre, 1 = observado
    observed = [[0] * (M + 2) for _ in range(N + 2)]
    
    # Processar câmeras
    for _ in range(K):
        C = int(next(it))
        L = int(next(it))
        D = next(it)
        if D == 'N':
            for linha in range(1, L + 1):
                observed[C][linha] = 1
        elif D == 'S':
            for linha in range(L, M + 1):
                observed[C][linha] = 1
        elif D == 'L':
            for coluna in range(C, N + 1):
                observed[coluna][L] = 1
        elif D == 'O':
            for coluna in range(1, C + 1):
                observed[coluna][L] = 1
    
    # BFS/DFS para verificar caminho da entrada (1,1) à saída (N,M)
    visited = [[False] * (M + 2) for _ in range(N + 2)]
    stack = [(1, 1)]
    visited[1][1] = True
    
    while stack:
        col, lin = stack.pop()
        if col == N and lin == M:
            print('S')
            return
        
        # Norte
        if lin > 1 and not visited[col][lin - 1] and observed[col][lin - 1] == 0:
            visited[col][lin - 1] = True
            stack.append((col, lin - 1))
        # Sul
        if lin < M and not visited[col][lin + 1] and observed[col][lin + 1] == 0:
            visited[col][lin + 1] = True
            stack.append((col, lin + 1))
        # Oeste
        if col > 1 and not visited[col - 1][lin] and observed[col - 1][lin] == 0:
            visited[col - 1][lin] = True
            stack.append((col - 1, lin))
        # Leste
        if col < N and not visited[col + 1][lin] and observed[col + 1][lin] == 0:
            visited[col + 1][lin] = True
            stack.append((col + 1, lin))
    
    print('N')

if __name__ == "__main__":
    solve()