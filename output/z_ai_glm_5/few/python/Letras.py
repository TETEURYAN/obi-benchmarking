import sys

# Otimização de leitura de entrada
input_data = sys.stdin.read().split()

if not input_data:
    sys.exit(0)

s = input_data[0]
n = len(s)

# dp[i] armazena o tamanho da maior subsequência crescente terminando com a letra de índice i (0='A', 25='Z')
dp = [0] * 26
offset = ord('A')

for char in s:
    idx = ord(char) - offset
    
    # Encontrar o máximo valor em dp[0...idx]
    # Como o alfabeto é pequeno (26), uma busca linear é eficiente e evita overhead de slicing
    max_prev = 0
    for i in range(idx + 1):
        if dp[i] > max_prev:
            max_prev = dp[i]
            
    # Atualizar o valor para a letra atual
    # A nova subsequência termina com 'char', então seu tamanho é 1 + max_prev
    if max_prev + 1 > dp[idx]:
        dp[idx] = max_prev + 1

# O resultado é o maior valor encontrado no array dp
print(max(dp))