import sys
import heapq

data = sys.stdin.read().split()
idx = 0
C = int(data[idx]); idx += 1
N = int(data[idx]); idx += 1

clients = []
for _ in range(N):
    T = int(data[idx]); idx += 1
    D = int(data[idx]); idx += 1
    clients.append((T, D))

# Min-heap of when each caixa becomes free
caixas = [0] * C
heapq.heapify(caixas)

count = 0
for T, D in clients:
    # Get the earliest free caixa
    earliest = heapq.heappop(caixas)
    # The client starts being served at max(earliest, T)
    start = max(earliest, T)
    wait = start - T
    if wait > 20:
        count += 1
    heapq.heappush(caixas, start + D)

print(count)