import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    R = int(input_data[0])
    K = int(input_data[1])

    # Otimização: A soma mínima de K inteiros positivos distintos é K*(K+1)/2.
    # Se R for menor que isso, é impossível, resultado 0.
    if K * (K + 1) // 2 > R:
        print(0)
        return

    # dp[s][c] = número de maneiras de obter soma 's' usando 'c' números distintos.
    # Dimensões: (R + 1) x (K + 1)
    dp = [[0] * (K + 1) for _ in range(R + 1)]
    
    # Caso base: 1 maneira de obter soma 0 com 0 números.
    dp[0][0] = 1
    
    # Iteramos por cada número possível (item) de 1 até R.
    # Para garantir que os números sejam distintos, usamos a lógica da Mochila 0/1:
    # iteramos a soma de trás para frente.
    for x in range(1, R + 1):
        for s in range(R, x - 1, -1):
            for c in range(K, 0, -1):
                dp[s][c] += dp[s - x][c - 1]
                
    print(dp[R][K])

if __name__ == '__main__':
    solve()