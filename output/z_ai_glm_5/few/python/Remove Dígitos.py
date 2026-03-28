import sys

input_data = sys.stdin.read().split()

if input_data:
    n = int(input_data[0])
    
    # dp[i] armazena o mínimo de rodadas para reduzir i a 0.
    # Inicializamos com n + 1 (equivalente a infinito), pois o máximo de passos é n.
    dp = [n + 1] * (n + 1)
    dp[0] = 0
    
    for i in range(1, n + 1):
        temp = i
        while temp > 0:
            digit = temp % 10
            if digit != 0:
                dp[i] = min(dp[i], dp[i - digit] + 1)
            temp //= 10
            
    print(dp[n])