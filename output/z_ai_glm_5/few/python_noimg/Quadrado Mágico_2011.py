import sys

# Leitura rápida de toda a entrada
input_data = sys.stdin.read().split()

if not input_data:
    exit()

iterator = iter(input_data)

try:
    N = int(next(iterator))
except StopIteration:
    exit()

# Restrições: 3 <= N <= 1000.
# Precisamos verificar se o quadrado contém todos os números de 1 a N^2.
# Como N é no máximo 1000, N^2 é no máximo 1.000.000.
# Podemos usar um bytearray para verificar a presença e unicidade dos números com eficiência de memória.
limit = N * N
seen = bytearray(limit + 1)

# Arrays para armazenar as somas das colunas.
# As somas das linhas e diagonais podem ser calculadas e verificadas incrementalmente.
col_sums = [0] * N
diag1_sum = 0
diag2_sum = 0

target_sum = -1
is_magic = True

# Processar o quadrado linha por linha
for r in range(N):
    row_sum = 0
    for c in range(N):
        try:
            val = int(next(iterator))
        except StopIteration:
            is_magic = False
            break
        
        # Verificar se o valor está no intervalo [1, N^2]
        if val < 1 or val > limit:
            is_magic = False
        # Verificar duplicatas
        elif seen[val]:
            is_magic = False
        else:
            seen[val] = 1
        
        if not is_magic:
            break
        
        # Acumular somas
        row_sum += val
        col_sums[c] += val
        
        # Diagonal principal (r == c)
        if c == r:
            diag1_sum += val
        
        # Diagonal secundária (c == N - 1 - r)
        if c == N - 1 - r:
            diag2_sum += val

    if not is_magic:
        break
    
    # Verificar soma da linha atual
    if r == 0:
        target_sum = row_sum
    else:
        if row_sum != target_sum:
            is_magic = False
            break

# Se passou na verificação inicial, verificar colunas e diagonais
if is_magic:
    # Verificar se todas as colunas somam o valor alvo
    for s in col_sums:
        if s != target_sum:
            is_magic = False
            break
    
    # Verificar diagonais
    if is_magic:
        if diag1_sum != target_sum or diag2_sum != target_sum:
            is_magic = False

# Imprimir o resultado
if is_magic:
    print(target_sum)
else:
    print(0)