
import sys

input = sys.stdin.read
data = input().split()

N = int(data[0])
lista = list(map(int, data[1:]))

dist = [float('inf')] * N

# Primeira passada: esquerda para direita
last_zero = -1
for i in range(N):
    if lista[i] == 0:
        dist[i] = 0
        last_zero = i
    else:
        if last_zero != -1:
            dist[i] = i - last_zero

# Segunda passada: direita para esquerda
last_zero = N
for i in range(N-1, -1, -1):
    if lista[i] == 0:
        last_zero = i
    else:
        if last_zero != N:
            dist[i] = min(dist[i], last_zero - i)

# Output
for i in range(N):
    if lista[i] == 0:
        print(0, end=' ')
    else:
        print(min(dist[i], 9), end=' ')
print()
