import sys

input_data = sys.stdin.read().split()

if not input_data:
    exit()

N = int(input_data[0])
D = int(input_data[1])
A = int(input_data[2])

# O movimento é cíclico e sempre avança (1 -> 2 -> ... -> N -> 1).
# Calculamos a distância circular de A até D.
# A fórmula (D - A + N) % N garante o resultado correto para qualquer caso.
result = (D - A + N) % N

print(result)