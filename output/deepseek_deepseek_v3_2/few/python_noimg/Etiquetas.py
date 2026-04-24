import sys

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    N, K, C = map(int, data[:3])
    A = list(map(int, data[3:]))
    
    # Precompute prefix sums
    prefix = [0] * (N + 1)
    for i in range(N):
        prefix[i + 1] = prefix[i] + A[i]
    
    # DP: dp[i][j] = max soma de descobertos usando j etiquetas até posição i
    # Mas N e K são <= 10000 -> dp[N][K] pode ser 10^8 estados, grande
    # Observação: dp[i][j] depende de dp[i-C][j-1] (colocar uma etiqueta terminando em i)
    # ou dp[i-1][j] (não colocar etiqueta terminando em i)
    # Podemos usar DP rolling (2D) ou calcular de outra forma:
    # Máximo de descobertos = soma total - mínimo de cobertos
    # Queremos minimizar soma dos números cobertos por K etiquetas de tamanho C sem overlap
    # Isso é equivalente a escolher K blocos de tamanho C com soma mínima
    # Blocos são subarrays de tamanho C: soma[i] = prefix[i+C] - prefix[i] para i de 0..N-C
    
    if K == 0:
        print(sum(A))
        return
    
    # Precompute sums of all windows of size C
    window_sums = []
    for i in range(N - C + 1):
        window_sums.append(prefix[i + C] - prefix[i])
    
    # DP to pick K non-overlapping windows with minimum total sum
    # dp_min[i][j] = min soma usando j windows até posição i (i é índice do último window)
    # Mas i pode ser até N-C, j até K
    # Usaremos DP 1D rolling por j
    # Ordem: para cada j de 1..K, compute best usando j windows
    # dp_prev = array para j-1 windows
    # dp_cur = array para j windows
    # dp_cur[i] = min(dp_cur[i-1], dp_prev[i-C] + window_sums[i])
    # (não usar window em i, ou usar window em i e antes usar j-1 windows terminando em i-C)
    # Inicializar dp_prev com 0 para j=0? Não, para j=0 soma coberta=0.
    # Mas dp_prev[i] = 0 para todos i? Não, porque não podemos usar 0 windows e depois usar 1?
    # Na primeira etapa (j=1) dp_cur[i] = min(dp_cur[i-1], window_sums[i]) (pois dp_prev[i-C] = 0)
    # Vamos inicializar dp_prev com 0 para i >= 0
    
    # Para j=1..K, calcular dp_cur
    INF = 10**18
    M = len(window_sums)  # N-C+1
    dp_prev = [0] * (M + 1)  # extra sentinel
    for j in range(1, K + 1):
        dp_cur = [INF] * (M + 1)
        # dp_cur[i] = min soma usando j windows até window i (i indexado de 1..M)
        for i in range(1, M + 1):
            # not use window at i -> dp_cur[i-1]
            use = INF
            if i - C >= 0:
                use = dp_prev[i - C] + window_sums[i - 1]  # window_sums[i-1] pois i index 1..M corresponde window index 0..M-1
            dp_cur[i] = min(dp_cur[i - 1], use)
        dp_prev = dp_cur
    
    min_covered = dp_prev[M]  # min soma coberta usando K windows
    total = sum(A)
    answer = total - min_covered
    print(answer)

if __name__ == "__main__":
    main()