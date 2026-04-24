
import sys

def solve():
    # Lê a linha de entrada e remove o caractere de nova linha
    s = sys.stdin.readline().strip()
    
    # Array para armazenar o tamanho da maior subsequência crescente terminando com cada letra.
    # dp[0] corresponde a 'A', dp[25] a 'Z'.
    dp = [0] * 26
    
    for char in s:
        idx = ord(char) - ord('A')
        
        # Encontrar o tamanho da maior subsequência que pode ser estendida pelo caractere atual.
        # Podemos estender qualquer subsequência que termine com uma letra 'c' tal que c <= char.
        # Isso corresponde a verificar todos os dp[i] onde 0 <= i <= idx.
        max_prev = 0
        for i in range(idx + 1):
            if dp[i] > max_prev:
                max_prev = dp[i]
        
        # Atualiza o valor para o caractere atual.
        # A nova subsequência tem tamanho max_prev + 1.
        if max_prev + 1 > dp[idx]:
            dp[idx] = max_prev + 1
            
    # A resposta é o maior valor encontrado entre todas as letras possíveis
    print(max(dp))

if __name__ == '__main__':
    solve()
