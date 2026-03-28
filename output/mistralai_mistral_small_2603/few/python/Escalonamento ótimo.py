
import sys
from collections import deque

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    idx = 0
    N = int(data[idx])
    M = int(data[idx + 1])
    idx += 2

    adj = [[] for _ in range(N)]
    in_degree = [0] * N

    for _ in range(M):
        A = int(data[idx])
        B = int(data[idx + 1])
        adj[A].append(B)
        in_degree[B] += 1
        idx += 2

    heap = []
    for i in range(N):
        if in_degree[i] == 0:
            heapq.heappush(heap, i)

    topo_order = []
    while heap:
        u = heapq.heappop(heap)
        topo_order.append(u)
        for v in adj[u]:
            in_degree[v] -= 1
            if in_degree[v] == 0:
                heapq.heappush(heap, v)

    if len(topo_order) != N:
        print('*')
    else:
        for task in topo_order:
            print(task)

if __name__ == '__main__':
    import heapq
    main()
