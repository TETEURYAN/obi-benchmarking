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
    
    # dp[k][pos] = max brigadeiros usando k amigos terminando na posição pos
    # O custo para mover o i-ésimo amigo para a posição j é |pos_amigos[i] - j|
    # A restrição é que a soma dos custos de movimento <= T
    # Como os amigos não podem trocar a ordem relativa, se o i-ésimo amigo vai para j,
    # o (i+1)-ésimo deve ir para pelo menos j+1.
    
    # dp[i][j][t] seria muito grande. 
    # Mas N é pequeno (300). Podemos usar dp[i][j] = custo mínimo para posicionar 
    # os primeiros i amigos terminando na posição j.
    # Como queremos maximizar brigadeiros com custo <= T, invertemos:
    # dp[i][j] = (custo_minimo, max_brigadeiros) - não funciona bem.
    
    # dp[i][j] = custo mínimo para colocar os primeiros i amigos nas primeiras j posições
    # tal que o i-ésimo amigo esteja na posição j.
    # dp[i][j] = min(dp[i-1][p] + abs(pos_amigos[i-1] - j)) para p < j
    
    # Como queremos maximizar brigadeiros com custo <= T:
    # dp[i][j][c] = max brigadeiros com i amigos, i-ésimo na posição j, custo c
    # c <= N*N = 90000. 300*300*90000 é muito.
    
    # Observação: O custo total é a soma das distâncias.
    # dp[i][j] = lista de (custo, soma_brigadeiros)
    # Como queremos apenas o máximo para cada custo, dp[i][j][custo] = max_brigadeiros
    
    dp = [[-1] * (N + 1) for _ in range(K + 1)]
    # dp[i][j] armazena um dicionário {custo: max_brigadeiros}
    dp = [[{} for _ in range(N)] for _ in range(K)]
    
    for j in range(N):
        custo = abs(pos_amigos[0] - j)
        if custo <= T:
            dp[0][j][custo] = P[j]
            
    for i in range(1, K):
        for j in range(i, N):
            custo_atual = abs(pos_amigos[i] - j)
            for prev_j in range(i - 1, j):
                for prev_custo, val in dp[i-1][prev_j].items():
                    novo_custo = prev_custo + custo_atual
                    if novo_custo <= T:
                        novo_val = val + P[j]
                        if novo_val > dp[i][j].get(novo_custo, -1):
                            dp[i][j][novo_custo] = novo_val
                            
    ans = 0
    for j in range(K - 1, N):
        for val in dp[K-1][j].values():
            if val > ans:
                ans = val
    print(ans)

solve()