import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    N = int(input_data[0])
    K = int(input_data[1])
    T = int(input_data[2])
    
    P = [int(x) for x in input_data[3:3+N]]
    G = [int(x) for x in input_data[3+N:3+2*N]]
    
    pos_amigos = [i for i, val in enumerate(G) if val == 1]
    
    # dp[i][j][t] = max brigadeiros usando os primeiros i amigos, 
    # terminando na posição j, com t trocas usadas.
    # Como T pode ser grande, mas o deslocamento máximo útil é N,
    # limitamos T a N*N.
    max_t = min(T, N * N)
    
    # dp[k_idx][pos] = {custo: max_brigadeiros}
    # Para otimizar, usamos um array de dicionários ou uma matriz
    # dp[k_idx][pos][custo]
    dp = [[-1] * (N * N + 1) for _ in range(K)]
    
    for j in range(N):
        custo = abs(j - pos_amigos[0])
        if custo <= max_t:
            dp[0][j][custo] = P[j]
            
    for i in range(1, K):
        for j in range(i, N):
            for prev_j in range(i - 1, j):
                custo_mov = abs(j - pos_amigos[i])
                for c in range(max_t - custo_mov + 1):
                    if dp[i-1][prev_j][c] != -1:
                        dp[i][j][c + custo_mov] = max(dp[i][j][c + custo_mov], dp[i-1][prev_j][c] + P[j])
                        
    ans = 0
    for j in range(K - 1, N):
        for c in range(max_t + 1):
            if dp[K-1][j][c] > ans:
                ans = dp[K-1][j][c]
                
    print(ans)

solve()