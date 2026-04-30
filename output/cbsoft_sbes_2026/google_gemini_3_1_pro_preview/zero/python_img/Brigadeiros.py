
import sys

def solve():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    
    N = int(data[0])
    K = int(data[1])
    T = int(data[2])
    
    # O número máximo de trocas úteis é limitado por N * N
    T = min(T, N * N)
    
    P = [int(x) for x in data[3:3+N]]
    G = [int(x) for x in data[3+N:3+2*N]]
    
    x = []
    for i in range(N):
        if G[i] == 1:
            x.append(i + 1)
            
    INF = float('inf')
    
    # A quantidade máxima possível de brigadeiros que o grupo pode comer
    sorted_P = sorted(P, reverse=True)
    max_possible_b = sum(sorted_P[:K])
    
    # dp[i][b] armazena o custo mínimo (número de trocas) para alocar i amigos
    # obtendo exatamente b brigadeiros.
    dp = [[INF] * (max_possible_b + 1) for _ in range(K + 1)]
    dp[0][0] = 0
    
    # valid_b[i] mantém um conjunto de quantidades de brigadeiros (b) alcançáveis
    # para i amigos, otimizando a iteração apenas para estados válidos.
    valid_b = [set() for _ in range(K + 1)]
    valid_b[0].add(0)
    
    for j in range(1, N + 1):
        p = P[j-1]
        # Iteramos de trás para frente para usar o array dp in-place
        for i in range(min(j, K), 0, -1):
            cost_dist = abs(x[i-1] - j)
            dp_i = dp[i]
            dp_prev = dp[i-1]
            valid_curr = valid_b[i]
            
            for prev_b in valid_b[i-1]:
                new_c = dp_prev[prev_b] + cost_dist
                if new_c <= T:
                    b = prev_b + p
                    if new_c < dp_i[b]:
                        if dp_i[b] == INF:
                            valid_curr.add(b)
                        dp_i[b] = new_c

    # A resposta será o valor máximo de brigadeiros alcançável com K amigos
    ans = max(valid_b[K]) if valid_b[K] else 0
    print(ans)

if __name__ == '__main__':
    solve()
