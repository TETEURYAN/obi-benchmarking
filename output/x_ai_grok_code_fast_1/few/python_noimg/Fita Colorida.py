import sys

input_data = sys.stdin.read().split()
N = int(input_data[0])
a = list(map(int, input_data[1:]))
dist = [float('inf')] * N
for i in range(N):
    if a[i] == 0:
        dist[i] = 0
# esquerda para direita
last = -1
for i in range(N):
    if a[i] == 0:
        last = i
    elif last != -1:
        dist[i] = min(dist[i], i - last)
# direita para esquerda
last = N
for i in range(N-1, -1, -1):
    if a[i] == 0:
        last = i
    elif last != N:
        dist[i] = min(dist[i], last - i)
# calcular cores
colors = []
for i in range(N):
    if a[i] == 0:
        colors.append(0)
    else:
        colors.append(min(9, dist[i]))
print(' '.join(map(str, colors)))