import sys

def solve():
    # Leitura rápida de toda a entrada
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return

    # O primeiro elemento é C (número de lajotas)
    C = int(input_data[0])
    
    # Os próximos C elementos representam as lajotas (0 ou 1)
    # É importante converter para inteiros
    tiles = list(map(int, input_data[1:1+C]))
    
    # Caso trivial: se houver apenas 1 lajota, já estamos no destino (0 pulos)
    if C == 1:
        print(0)
        return

    # dp[i] armazena o número mínimo de pulos para chegar na lajota i.
    # Inicializamos com um valor sentinela (infinito), representando inalcançável.
    # Como C <= 10^4, C+1 é um valor seguro para "infinito".
    INF = C + 1
    dp = [INF] * C
    
    # A lajota inicial (índice 0) é sempre preta e requer 0 pulos para começar.
    dp[0] = 0
    
    # Iteramos por todas as lajotas
    for i in range(C):
        # Se a lajota atual é inalcançável, não podemos pular a partir dela
        if dp[i] == INF:
            continue
            
        # O gato pode pular para i+1 ou i+2.
        # Verificamos se o destino está dentro dos limites e se é uma lajota preta (valor 1).
        
        # Pulo de 1 lajota
        if i + 1 < C:
            if tiles[i+1] == 1:
                dp[i+1] = min(dp[i+1], dp[i] + 1)
        
        # Pulo de 2 lajotas
        if i + 2 < C:
            if tiles[i+2] == 1:
                dp[i+2] = min(dp[i+2], dp[i] + 1)
    
    # O resultado está na última lajota (índice C-1).
    # Se permaneceu como INF, é impossível chegar.
    result = dp[C-1]
    
    if result == INF:
        print(-1)
    else:
        print(result)

if __name__ == "__main__":
    solve()