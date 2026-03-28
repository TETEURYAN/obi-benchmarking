import sys
import math

# Lê a entrada completa e divide em tokens
input_data = sys.stdin.read().split()

# Verifica se há dados de entrada
if not input_data:
    sys.exit(0)

# Extrai N e M. As restrições permitem valores até 10^18, que Python lida nativamente.
n = int(input_data[0])
m = int(input_data[1])

# Começa a busca pelo maior X a partir de M (decrementando)
# A condição é que gcd(N, X) == 1.
# Graças à propriedade da função totiente e à distribuição de coprimos,
# a distância entre coprimos é pequena (gap máximo é limitado por função de Jacobsthal),
# logo este loop executará pouquíssimas iterações (tipicamente < 200 para N até 10^18).
x = m
while x > 0:
    if math.gcd(n, x) == 1:
        print(x)
        break
    x -= 1