import sys

# Aumentar o limite de recursão, embora a solução seja iterativa
sys.setrecursionlimit(200000)

def solve():
    # Leitura rápida de toda a entrada
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return

    # Iterador para processar os tokens
    iterator = iter(input_data)
    
    try:
        N = int(next(iterator))
        X1 = int(next(iterator))
        X2 = int(next(iterator))
    except StopIteration:
        return

    lines = []
    for _ in range(N):
        A = int(next(iterator))
        B = int(next(iterator))
        # Calcula os valores L e R
        # L = B + X1 * A
        # R = B + X2 * A
        L = B + X1 * A
        R = B + X2 * A
        lines.append((L, R))

    # Caso especial: X1 == X2
    # A interseção ocorre em x = X1. A condição é L_i == L_j.
    if X1 == X2:
        counts = {}
        for L, R in lines:
            counts[L] = counts.get(L, 0) + 1
        
        ans = 0
        for count in counts.values():
            ans += count * (count - 1) // 2
        print(ans)
        return

    # Caso geralal: X1 < X2
    # Ordena as linhas pelo valor de L
    lines.sort(key=lambda x: x[0])
    
    # Compressão de coordenadas para os valores de R
    # Necessária porque os valores de R podem ser muito grandes (até 10^18)
    unique_R = sorted(list(set([r for l, r in lines])))
    rank_map = {val: i + 1 for i, val in enumerate(unique_R)}
    K = len(unique_R)
    
    # Fenwick Tree (BIT) para contagem de frequências
    bit = [0] * (K + 2)
    
    def update(i, delta):
        while i <= K:
            bit[i] += delta
            i += i & -i
            
    def query(i):
        s = 0
        while i > 0:
            s += bit[i]
            i -= i & -i
        return s

    ans = 0
    i = 0
    while i < N:
        j = i
        # Encontra o grupo de linhas com o mesmo valor de L
        while j < N and lines[j][0] == lines[i][0]:
            j += 1
        
        count = j - i
        
        # Conta pares dentro do mesmo grupo (mesmo L)
        # Isso corresponde a interseções em x = X1
        ans += count * (count - 1) // 2
        
        # Conta pares com grupos anteriores (L_prev < L_curr)
        # A condição para interseção válida é R_prev >= R_curr
        # O número de elementos anteriores é 'i'
        # O número de elementos anteriores com R < R_curr é query(rank - 1)
        # Logo, queremos i - query(rank - 1)
        
        for k in range(i, j):
            r_val = lines[k][1]
            r_rank = rank_map[r_val]
            # Conta quantos R anteriores são maiores ou iguais a r_val
            ans += i - query(r_rank - 1)
            
        # Atualiza a BIT com os elementos do grupo atual
        for k in range(i, j):
            r_val = lines[k][1]
            r_rank = rank_map[r_val]
            update(r_rank, 1)
            
        i = j
        
    print(ans)

if __name__ == '__main__':
    solve()