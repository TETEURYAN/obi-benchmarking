import sys
import heapq

input_data = sys.stdin.read().split()
idx = 0

N = int(input_data[idx])
K1 = int(input_data[idx + 1])
K2 = int(input_data[idx + 2])
P = int(input_data[idx + 3])
idx += 4

# Grafo com 2*N nós: 2*(i-1) para metrô, 2*(i-1)+1 para ônibus
V = 2 * N
graph = [[] for _ in range(V)]

# Adicionar arestas de metrô (sistema 0)
for _ in range(K1):
    Vi = int(input_data[idx]) - 1
    Ui = int(input_data[idx + 1]) - 1
    idx += 2
    # De metrô Vi a metrô Ui, custo 0
    graph[2 * Vi].append((2 * Ui, 0))
    graph[2 * Ui].append((2 * Vi, 0))

# Adicionar arestas de ônibus (sistema 1)
for _ in range(K2):
    Xj = int(input_data[idx]) - 1
    Yj = int(input_data[idx + 1]) - 1
    idx += 2
    # De ônibus Xj a ônibus Yj, custo 0
    graph[2 * Xj + 1].append((2 * Yj + 1, 0))
    graph[2 * Yj + 1].append((2 * Xj + 1, 0))

# Adicionar arestas de troca de sistema
for i in range(N):
    # De metrô i a ônibus i, custo P
    graph[2 * i].append((2 * i + 1, P))
    # De ônibus i a metrô i, custo P
    graph[2 * i + 1].append((2 * i, P))

A = int(input_data[idx]) - 1
B = int(input_data[idx + 1]) - 1

# Nó fonte fictício
source = V
graph.append([])  # Adicionar nó fonte
# Conectar fonte a (A,0) e (A,1) com custo P
graph[source].append((2 * A, P))
graph[source].append((2 * A + 1, P))

# Dijkstra
INF = float('inf')
dist = [INF] * (V + 1)
dist[source] = 0
pq = [(0, source)]  # (dist, node)

while pq:
    d, u = heapq.heappop(pq)
    if d > dist[u]:
        continue
    for v, w in graph[u]:
        if dist[v] > dist[u] + w:
            dist[v] = dist[u] + w
            heapq.heappush(pq, (dist[v], v))

# Menor custo para (B,0) ou (B,1)
ans = min(dist[2 * B], dist[2 * B + 1])
if ans == INF:
    print(-1)
else:
    print(ans)