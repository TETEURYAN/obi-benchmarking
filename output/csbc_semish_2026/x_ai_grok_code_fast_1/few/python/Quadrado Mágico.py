import sys

input_data = sys.stdin.read().split()

N = int(input_data[0])

matriz = []

idx = 1

for _ in range(N):
    linha = [int(x) for x in input_data[idx:idx+N]]
    matriz.append(linha)
    idx += N

# Encontrar zero
i, j = -1, -1
for r in range(N):
    for c in range(N):
        if matriz[r][c] == 0:
            i, j = r, c
            break
    if i != -1:
        break

# Calcular S
possiveis_S = []

# Linhas
somas_linhas = []
for r in range(N):
    if r != i:
        soma = sum(matriz[r])
        somas_linhas.append(soma)
if len(set(somas_linhas)) == 1:
    possiveis_S.append(somas_linhas[0])

# Colunas
somas_cols = []
for c in range(N):
    if c != j:
        soma = sum(matriz[r][c] for r in range(N))
        somas_cols.append(soma)
if len(set(somas_cols)) == 1:
    possiveis_S.append(somas_cols[0])

# Diagonal principal
if i != j:
    soma_diag1 = sum(matriz[k][k] for k in range(N))
    possiveis_S.append(soma_diag1)

# Diagonal secundária
if i != N-1-j:
    soma_diag2 = sum(matriz[k][N-1-k] for k in range(N))
    possiveis_S.append(soma_diag2)

S = possiveis_S[0]

# Calcular valor
soma_linha_sem_zero = sum(matriz[i][c] for c in range(N) if c != j)
valor = S - soma_linha_sem_zero

print(valor)
print(i+1)
print(j+1)