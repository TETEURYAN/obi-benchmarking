
import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    N = int(input_data[0])
    F = float(input_data[1])
    
    A = [int(x) for x in input_data[2:N+2]]
    
    # Duplicar o array para lidar com a circularidade
    A = A + A
    
    # Array de somas de prefixos para consultas O(1)
    pref = [0] * (2 * N + 1)
    for i in range(2 * N):
        pref[i+1] = pref[i] + A[i]
        
    # dp[i][j] armazenará o custo mínimo para mesclar o subarray de i até j
    dp = [[0] * (2 * N) for _ in range(2 * N)]
    
    for length in range(2, N + 1):
        for i in range(2 * N - length + 1):
            j = i + length - 1
            pref_i = pref[i]
            sum_ij = pref[j+1] - pref_i
            
            min_cost = 10**18
            dpi = dp[i]
            
            for k in range(i, j):
                sum_ik = pref[k+1] - pref_i
                sum_kj = sum_ij - sum_ik
                
                # O custo da divisão é proporcional ao máximo entre as duas partes
                cost = dpi[k] + dp[k+1][j] + (sum_ik if sum_ik > sum_kj else sum_kj)
                if cost < min_cost:
                    min_cost = cost
                    
            dp[i][j] = min_cost
            
    # Encontrar a melhor resposta entre todas as janelas de tamanho N
    ans = min(dp[i][i+N-1] for i in range(N))
    
    # Multiplicar pelo fator F no final para evitar operações com float no DP
    print(f"{ans * F:.2f}")

if __name__ == '__main__':
    solve()
