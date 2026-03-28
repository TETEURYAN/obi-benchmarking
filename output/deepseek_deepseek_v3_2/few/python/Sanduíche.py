import sys

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    N = int(next(it))
    M = int(next(it))
    
    # Representar restrições como máscara de bits
    conflict = [0] * N
    for _ in range(M):
        x = int(next(it)) - 1
        y = int(next(it)) - 1
        conflict[x] |= 1 << y
        conflict[y] |= 1 << x
    
    # DP sobre subconjuntos
    dp = [0] * (1 << N)
    dp[0] = 1  # conjunto vazio é válido (mas não conta como sanduíche)
    
    for mask in range(1 << N):
        if dp[mask] == 0:
            continue
        # Encontrar o menor bit não usado
        for i in range(N):
            if (mask >> i) & 1:
                continue
            # Verificar se podemos adicionar i ao conjunto mask
            if (mask & conflict[i]) == 0:
                new_mask = mask | (1 << i)
                dp[new_mask] = 1
    
    # Contar todos os subconjuntos não vazios que são válidos
    result = sum(dp) - 1  # subtrai o conjunto vazio
    print(result)

if __name__ == "__main__":
    solve()