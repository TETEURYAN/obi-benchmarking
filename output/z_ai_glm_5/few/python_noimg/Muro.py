import sys

# Aumentar o limite de recursão, embora a solução seja iterativa
sys.setrecursionlimit(200000)

def solve():
    # Leitura rápida de toda a entrada
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return

    n = int(input_data[0])
    
    MOD = 10**9 + 7
    
    # Casos base baseados no enunciado e na análise dos casos de teste
    # A recorrência identificada é:
    # dp[i] = dp[i-1] + 4*dp[i-2] + 2*dp[i-3]
    # Isso corresponde às 7 maneiras possíveis de terminar a mureta:
    # 1 maneira de terminar com uma peça de largura 1 (1 * dp[i-1])
    # 4 maneiras de terminar com configurações de largura 2 (4 * dp[i-2])
    # 2 maneiras de terminar com configurações de largura 3 (2 * dp[i-3])
    # Total: 1 + 4 + 2 = 7 maneiras.
    
    if n == 0:
        print(1)
        return
    if n == 1:
        print(1)
        return
    if n == 2:
        print(5)
        return
        
    # Inicialização do array dp
    # Tamanho suficiente para armazenar até n
    dp = [0] * (n + 1)
    
    dp[0] = 1
    dp[1] = 1
    dp[2] = 5
    
    # Preenchimento iterativo
    for i in range(3, n + 1):
        # Aplicação da recorrência com módulo
        term1 = dp[i-1]
        term2 = (4 * dp[i-2]) % MOD
        term3 = (2 * dp[i-3]) % MOD
        
        dp[i] = (term1 + term2 + term3) % MOD
        
    print(dp[n])

if __name__ == '__main__':
    solve()