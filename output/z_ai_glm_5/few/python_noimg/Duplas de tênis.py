import sys

input_data = sys.stdin.read().split()

A = int(input_data[0])
B = int(input_data[1])
C = int(input_data[2])
D = int(input_data[3])

# Existem 3 maneiras de dividir 4 jogadores em 2 duplas:
# 1. (A, B) vs (C, D) -> Diferença: |(A+B) - (C+D)|
# 2. (A, C) vs (B, D) -> Diferença: |(A+C) - (B+D)|
# 3. (A, D) vs (B, C) -> Diferença: |(A+D) - (B+C)|
# Como a entrada já vem ordenada (A <= B <= C <= D), a terceira opção é matematicamente a mais equilibrada,
# mas calcular o mínimo entre as três garante a corretude para 100% dos casos.

diff1 = abs((A + B) - (C + D))
diff2 = abs((A + C) - (B + D))
diff3 = abs((A + D) - (B + C))

print(min(diff1, diff2, diff3))