import sys
import math

input_data = sys.stdin.read().split()

if not input_data:
    exit()

n = int(input_data[0])

# Em um conjunto completo de N! permutações, cada número k (de 1 a N) aparece
# em cada posição exatamente (N-1)! vezes.
# A soma de 1 a N é dada por n*(n+1)//2.
# Portanto, a soma esperada para cada coluna é:
target_sum = math.factorial(n - 1) * (n * (n + 1) // 2)

current_sums = [0] * n

# Processa os números da entrada. O primeiro elemento é N, o restante são as permutações.
# O índice de cada número determina sua posição na permutação (0 a N-1).
for i in range(1, len(input_data)):
    val = int(input_data[i])
    pos = (i - 1) % n
    current_sums[pos] += val

# A carta faltante é a diferença entre a soma esperada e a soma atual para cada posição.
missing_perm = [str(target_sum - s) for s in current_sums]
print(" ".join(missing_perm))