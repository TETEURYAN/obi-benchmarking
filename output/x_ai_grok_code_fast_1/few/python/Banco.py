import sys
import heapq

input_data = sys.stdin.read().split()
idx = 0
C = int(input_data[idx])
idx += 1
N = int(input_data[idx])
idx += 1

clientes = []
for _ in range(N):
    T = int(input_data[idx])
    D = int(input_data[idx + 1])
    clientes.append((T, D))
    idx += 2

heap = [0] * C
heapq.heapify(heap)
contador = 0

for T, D in clientes:
    min_free = heapq.heappop(heap)
    start = max(T, min_free)
    if start - T > 20:
        contador += 1
    heapq.heappush(heap, start + D)

print(contador)