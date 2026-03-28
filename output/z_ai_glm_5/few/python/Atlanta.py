import sys
import math

# Ler todos os dados de entrada de uma vez
input_data = sys.stdin.read().split()

if not input_data:
    sys.exit()

# Parsear os valores de A e B
A = int(input_data[0])
B = int(input_data[1])

# A quantidade de azulejos azuis A corresponde ao perímetro menos os cantos contados duas vezes.
# A = 2*L + 2*C - 4 => A = 2*(L + C - 2)
# Logo, A deve ser par.
if A % 2 != 0:
    print("-1 -1")
    sys.exit()

# Definimos x = L - 2 e y = C - 2, que são as dimensões do retângulo interno de azulejos brancos.
# Temos que:
# x * y = B
# x + y = A/2 - 2
# Como B >= 1 (pelo enunciado), x e y devem ser inteiros positivos (>= 1).
# Isso implica que a soma S = x + y deve ser >= 2.

S = A // 2 - 2

if S < 2:
    print("-1 -1")
    sys.exit()

# Para que x e y existam como inteiros, o discriminante da equação do segundo grau deve ser um quadrado perfeito.
# t^2 - St + B = 0
# Delta = S^2 - 4B
delta = S * S - 4 * B

if delta < 0:
    print("-1 -1")
    sys.exit()

raiz_delta = math.isqrt(delta)

if raiz_delta * raiz_delta != delta:
    print("-1 -1")
    sys.exit()

# As raízes são (S - raiz_delta) / 2 e (S + raiz_delta) / 2.
# Como S e raiz_delta têm mesma paridade (garantido pelo fato de delta ser congruente a S^2 mod 4),
# a divisão por 2 resultará em inteiros.
x = (S - raiz_delta) // 2
y = (S + raiz_delta) // 2

# Verificação de segurança para garantir que x e y são positivos.
# Como B >= 1, x e y não podem ser zero. Como S >= 2, eles são >= 1.
if x < 1 or y < 1:
    print("-1 -1")
    sys.exit()

# Recuperar as dimensões da sala
L = x + 2
C = y + 2

# Imprimir na ordem crescente (menor dimensão primeiro)
if L > C:
    L, C = C, L

print(f"{L} {C}")