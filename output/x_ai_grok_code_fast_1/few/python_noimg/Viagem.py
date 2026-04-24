import sys
import heapq

input_data = sys.stdin.read().split()
idx = 0

V = int(input_data[idx])
N = int(input_data[idx + 1])
M = int(input_data[idx + 2])
idx += 3

adj = [[] for _ in range(N + 1)]
for _ in range(M):
    A = int(input_data[idx])
    B = int(input_data[idx + 1])
    T = int(input_data[idx + 2])
    P = int(input_data[idx + 3])
    adj[A].append((B, T, P))
    adj[B].append((A, T, P))
    idx += 4

X = int(input_data[idx])
Y = int(input_data[idx + 1])

INF = float('inf')
dist = [[INF] * (V + 1) for _ in range(N + 1)]
dist[X][0] = 0

pq = [(0, X, 0)]  # (tempo, ilha, custo)

while pq:
    tempo, u, c = heapq.heappop(pq)
    if tempo > dist[u][c]:
        continue
    for v, t, p in adj[u]:
        novo_c = c + p
        if novo_c <= V:
            novo_tempo = tempo + t
            if novo_tempo < dist[v][novo_c]:
                dist[v][novo_c] = novo_tempo
                heapq.heappush(pq, (novo_tempo, v, novo_c))

min_tempo = min(dist[Y])
if min_tempo == INF:
    print(-1)
else:
    print(min_tempo)