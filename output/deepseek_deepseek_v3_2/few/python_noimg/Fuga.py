import sys
sys.setrecursionlimit(200000)

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    N = int(next(it))
    M = int(next(it))
    Xe = int(next(it))
    Ye = int(next(it))
    Xs = int(next(it))
    Ys = int(next(it))
    
    # Armários estão em (i,j) com i e j pares
    # Mas como índices são 1‑based, paridade é (i%2==0 and j%2==0)
    # Vamos converter para 0‑based internamente
    Xe -= 1; Ye -= 1; Xs -= 1; Ys -= 1
    
    # Estados: cada armário pode estar em 5 estados:
    # 0: em pé (ocupa (i,j))
    # 1: derrubado para cima (ocupa (i,j) e (i-1,j))
    # 2: derrubado para baixo (ocupa (i,j) e (i+1,j))
    # 3: derrubado para esquerda (ocupa (i,j) e (i,j-1))
    # 4: derrubado para direita (ocupa (i,j) e (i,j+1))
    # Armários são independentes? Não, porque a queda pode bloquear outro armário.
    # Mas N,M ≤ 11, então número de células com armário é floor(N/2)*floor(M/2) ≤ 25.
    # Podemos fazer busca completa com BFS/DFS para cada configuração.
    
    # Lista de posições dos armários (cada uma é (i,j) com i,j pares em 0‑based)
    cabinets = []
    for i in range(1, N, 2):  # i par em 1‑based -> ímpar em 0‑based? Não.
        # Em 1‑based: i par -> i%2==0. Em 0‑based: i+1 par? Vamos recalcular.
        # Melhor: em 0‑based, armário em (i,j) onde i%2==1 e j%2==1 (porque 1‑based par -> 0‑based ímpar)
        pass
    # Refazer: em 1‑based, armário se i e j são pares.
    # Convertendo para 0‑based: i' = i-1, j' = j-1.
    # Então em 0‑based, armário se (i'+1) par e (j'+1) par => i' ímpar e j' ímpar.
    # Portanto, armários estão em células com coordenadas ímpares (0‑based).
    cabinets = []
    for i in range(N):
        for j in range(M):
            if i % 2 == 1 and j % 2 == 1:
                cabinets.append((i, j))
    
    # Número de armários
    K = len(cabinets)
    # Direções: 0:up, 1:down, 2:left, 3:right
    dirs = [(-1,0), (1,0), (0,-1), (0,1)]
    
    # Função para, dado um estado (tupla de tamanho K com valores 0..4), retornar grade ocupada
    def build_grid(state):
        # state é lista de inteiros 0..4
        occ = [[False]*M for _ in range(N)]
        for idx, (ci, cj) in enumerate(cabinets):
            s = state[idx]
            occ[ci][cj] = True
            if s == 0:
                continue
            di, dj = dirs[s-1]
            ni, nj = ci + di, cj + dj
            if 0 <= ni < N and 0 <= nj < M:
                occ[ni][nj] = True
        return occ
    
    # Verifica se estado é válido:
    # 1. Nenhum armário cai para fora da sala.
    # 2. Nenhuma célula é ocupada por mais de um armário.
    def valid_state(state):
        occ = [[0]*M for _ in range(N)]
        for idx, (ci, cj) in enumerate(cabinets):
            s = state[idx]
            if occ[ci][cj] > 0:
                return False
            occ[ci][cj] += 1
            if s == 0:
                continue
            di, dj = dirs[s-1]
            ni, nj = ci + di, cj + dj
            if not (0 <= ni < N and 0 <= nj < M):
                return False
            if occ[ni][nj] > 0:
                return False
            occ[ni][nj] += 1
        return True
    
    # BFS para menor caminho em grade com obstáculos
    def bfs(occ, start, end):
        if occ[start[0]][start[1]] or occ[end[0]][end[1]]:
            return -1
        from collections import deque
        dist = [[-1]*M for _ in range(N)]
        dq = deque()
        dq.append(start)
        dist[start[0]][start[1]] = 1
        while dq:
            i, j = dq.popleft()
            if (i, j) == end:
                return dist[i][j]
            for di, dj in dirs:
                ni, nj = i + di, j + dj
                if 0 <= ni < N and 0 <= nj < M and not occ[ni][nj] and dist[ni][nj] == -1:
                    dist[ni][nj] = dist[i][j] + 1
                    dq.append((ni, nj))
        return -1
    
    # Busca exaustiva sobre todos os estados (5^K) com poda.
    # K ≤ 25, 5^25 é enorme, mas muitas são inválidas.
    # Podemos usar DFS com backtracking.
    best = 0
    
    # Ordenar cabinets para poda? Não necessário.
    # Vamos gerar estados recursivamente.
    current_state = [0]*K
    
    # Pré‑computar se entrada/saída são adjacentes a armário em pé (não pode acontecer pelo enunciado, mas verificamos)
    # Pelo enunciado, entrada e saída nunca são adjacentes a armário (em pé). Mas após derrubar podem ficar adjacentes? Sim.
    # Isso é permitido? O enunciado diz: "A entrada e a saída nunca são adjacentes a um armário." (em pé). Após derrubar, não são mais armários em pé, então ok.
    
    def dfs(idx):
        nonlocal best
        if idx == K:
            if valid_state(current_state):
                occ = build_grid(current_state)
                d = bfs(occ, (Xe, Ye), (Xs, Ys))
                if d > best:
                    best = d
            return
        # Tentar todas as 5 opções para este armário
        for opt in range(5):
            current_state[idx] = opt
            # Poda: verificar se já é inválido com os armários até idx
            # Podemos verificar colisão parcial
            occ_partial = [[0]*M for _ in range(N)]
            ok = True
            for i in range(idx+1):
                ci, cj = cabinets[i]
                s = current_state[i]
                if occ_partial[ci][cj] > 0:
                    ok = False
                    break
                occ_partial[ci][cj] += 1
                if s == 0:
                    continue
                di, dj = dirs[s-1]
                ni, nj = ci + di, cj + dj
                if not (0 <= ni < N and 0 <= nj < M):
                    ok = False
                    break
                if occ_partial[ni][nj] > 0:
                    ok = False
                    break
                occ_partial[ni][nj] += 1
            if ok:
                dfs(idx+1)
    
    dfs(0)
    print(best)

if __name__ == "__main__":
    solve()