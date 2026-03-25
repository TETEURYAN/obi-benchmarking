
import sys

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    
    N, K, T = map(int, data[:3])
    P = list(map(int, data[3:3+N]))
    G = list(map(int, data[3+N:3+N+N]))
    
    # indices dos amigos
    friends_idx = [i for i in range(N) if G[i] == 1]
    
    # DP: dp[pos][moves] = max brigaderios que os primeiros pos amigos podem comer usando moves trocas
    # pos: 0..K, moves: 0..T (limitado por N*N)
    max_moves = min(T, N*N)  # não precisamos mais que N*N movimentos
    dp = [[-10**18]*(max_moves+1) for _ in range(K+1)]
    dp[0][0] = P[friends_idx[0]] if K > 0 else 0
    
    for pos in range(1, K):
        for moves in range(max_moves+1):
            best = -10**18
            for prev_moves in range(moves+1):
                if dp[pos-1][prev_moves] == -10**18:
                    continue
                used = moves - prev_moves
                # amigo atual pode ir até friends_idx[pos] + used (direita)
                # mas também pode ir até friends_idx[pos] - used (esquerda)
                # limitado por [0, N-1]
                left_limit = max(0, friends_idx[pos] - used)
                right_limit = min(N-1, friends_idx[pos] + used)
                for target in range(left_limit, right_limit+1):
                    # precisa verificar se target não foi usado por amigos anteriores
                    # isso é complexo, vamos mudar abordagem
    
    # Abordagem: matching entre amigos e posições usando movimentos limitados
    # custo[i][j] = movimentos necessários para amigo i ir para posição j
    # só podemos usar T movimentos total
    # maximizar soma P[j] para matching
    
    custo = []
    for i in range(K):
        fi = friends_idx[i]
        row = []
        for j in range(N):
            dist = abs(fi - j)
            row.append(dist)
        custo.append(row)
    
    # DP com dimensão [amigo][movimentos] = max brigaderios
    # vamos permitir que amigos sejam ordenados e usemos movimentos acumulados
    
    INF = -10**9
    dp2 = [[INF]*(max_moves+1) for _ in range(K+1)]
    dp2[0][0] = 0
    
    for i in range(K):  # amigo i (0-index)
        for moves in range(max_moves+1):
            if dp2[i][moves] == INF:
                continue
            # amigo i pode ir para qualquer posição j
            for j in range(N):
                need = custo[i][j]
                if moves + need <= max_moves:
                    new_val = dp2[i][moves] + P[j]
                    if new_val > dp2[i+1][moves+need]:
                        dp2[i+1][moves+need] = new_val
    
    answer = 0
    for moves in range(max_moves+1):
        if dp2[K][moves] > answer:
            answer = dp2[K][moves]
    
    # mas precisamos garantir que posições não se sobreponham
    # isso é um assignment problem: K amigos -> K posições distintas
    
    # vamos usar DP com bitmask das posições ocupadas
    # N <= 300, K <= N, T <= 1e9 -> não podemos bitmask todas posições
    # mas podemos bitmask dos amigos em ordem
    
    # reformulando: dp[amigo][movimentos][posição] não funciona
    # melhor: dp[amigo][movimentos] com último posição, mas precisamos evitar conflito
    
    # Solução: transformar em problema de matching mínimo em bipartite com custo de movimento
    # e maximizar peso (P[j])
    
    # Ideia: cada amigo i tem custo[i][j] para ir para posição j
    # queremos escolher K posições distintas maximizando soma P[j] - lambda*custo
    # mas custo total <= T
    
    # Podemos usar DP onde processamos posições 0..N-1 e escolhemos K delas
    # dp[pos][k][moves] = max brigaderios usando k amigos até posição pos com moves movimentos
    
    dp3 = [[[INF]*(max_moves+1) for _ in range(K+1)] for _ in range(N+1)]
    for pos in range(N+1):
        dp3[pos][0][0] = 0
    
    for pos in range(1, N+1):
        for k in range(1, K+1):
            for moves in range(max_moves+1):
                # não usar posição pos-1
                dp3[pos][k][moves] = dp3[pos-1][k][moves]
                # usar posição pos-1 para amigo k
                # precisamos saber qual amigo vai aqui
                # mas amigos têm posições inicial diferentes
                # vamos ordenar amigos e tentar assignar em ordem crescente de posição inicial
                friends_sorted = sorted(friends_idx)
                # amigo k-1 (0-index) tem pos inicial friends_sorted[k-1]
                need = abs(friends_sorted[k-1] - (pos-1))
                if need <= moves:
                    prev = dp3[pos-1][k-1][moves-need]
                    if prev != INF:
                        val = prev + P[pos-1]
                        if val > dp3[pos][k][moves]:
                            dp3[pos][k][moves] = val
    
    answer = 0
    for moves in range(max_moves+1):
        if dp3[N][K][moves] > answer:
            answer = dp3[N][K][moves]
    
    print(answer)

if __name__ == "__main__":
    solve()
