
n = int(input())
fita = list(map(int, input().split()))

# Encontrar todas as posições com 0
zeros = [i for i in range(n) if fita[i] == 0]

# Para cada posição, calcular a distância mínima para algum zero
for i in range(n):
    if fita[i] == -1:
        min_dist = min(abs(i - pos) for pos in zeros)
        fita[i] = min(min_dist, 9)

# Imprimir o resultado
print(' '.join(map(str, fita)))
