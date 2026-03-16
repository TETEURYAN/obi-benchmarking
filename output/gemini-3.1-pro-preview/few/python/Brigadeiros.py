import sys

# Aumentar o limite de recursão por precaução
sys.setrecursionlimit(200000)

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    N = int(input_data[0])
    K = int(input_data[1])
    T = int(input_data[2])
    
    P = [int(x) for x in input_data[3:3+N]]
    G = [int(x) for x in input_data[3+N:3+2*N]]
    
    # Posições iniciais dos amigos (1-indexed)
    pos = [i + 1 for i in range(N) if G[i] == 1]
            
    # frontiers[j] armazena a fronteira de Pareto para j amigos posicionados.
    # Cada elemento é uma tupla (valor_total, custo_total).
    # A fronteira mantém os estados não dominados: valores estritamente crescentes e custos estritamente crescentes.
    frontiers = [[] for _ in range(K + 1)]
    frontiers[0] = [(0, 0)]
    
    for i in range(1, N + 1):
        p_val = P[i-1]
        
        # Iterar j de min(i, K) até 1 para atualizar o DP in-place (otimização de espaço)
        for j in range(min(i, K), 0, -1):
            cost_add = abs(pos[j-1] - i)
            
            f_prev = frontiers[j-1]
            if not f_prev:
                continue
                
            # Gerar a nova fronteira baseada na posição i sendo escolhida para o j-ésimo amigo
            new_f = [(v + p_val, c + cost_add) for v, c in f_prev]
            
            f_curr = frontiers[j]
            if not f_curr:
                frontiers[j] = new_f
            else:
                # Fazer o merge de f_curr e new_f mantendo a propriedade da fronteira de Pareto
                res = []
                append = res.append
                pop = res.pop
                
                idx1 = 0
                idx2 = 0
                n1 = len(f_curr)
                n2 = len(new_f)
                
                while idx1 < n1 and idx2 < n2:
                    v1, c1 = f_curr[idx1]
                    v2, c2 = new_f[idx2]
                    
                    if v1 < v2:
                        v, c = v1, c1
                        idx1 += 1
                    elif v1 > v2:
                        v, c = v2, c2
                        idx2 += 1
                    else:
                        v = v1
                        c = c1 if c1 < c2 else c2
                        idx1 += 1
                        idx2 += 1
                        
                    # Remover estados dominados
                    while res and res[-1][1] >= c:
                        pop()
                    append((v, c))
                    
                while idx1 < n1:
                    v, c = f_curr[idx1]
                    idx1 += 1
                    while res and res[-1][1] >= c:
                        pop()
                    append((v, c))
                    
                while idx2 < n2:
                    v, c = new_f[idx2]
                    idx2 += 1
                    while res and res[-1][1] >= c:
                        pop()
                    append((v, c))
                    
                frontiers[j] = res

    ans = 0
    # A fronteira está ordenada por valor crescente.
    # Iteramos de trás para frente para encontrar o maior valor com custo <= T.
    for v, c in reversed(frontiers[K]):
        if c <= T:
            ans = v
            break
            
    print(ans)

if __name__ == '__main__':
    solve()