
import heapq

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    idx = 0
    N = int(data[idx])
    idx += 1
    M = int(data[idx])
    idx += 1

    adj = [[] for _ in range(N)]
    for _ in range(M):
        P = int(data[idx])
        idx += 1
        Q = int(data[idx])
        idx += 1
        U = int(data[idx])
        idx += 1
        adj[P].append((Q, U))
        adj[Q].append((P, U))

    total_min = float('inf')

    for root in range(N):
        heap = []
        visited = [False] * N
        heapq.heappush(heap, (0, root))
        visited[root] = True
        sum_cost = 0

        while heap:
            cost, u = heapq.heappop(heap)
            sum_cost += cost
            for (v, w) in adj[u]:
                if not visited[v]:
                    visited[v] = True
                    heapq.heappush(heap, (w, v))

        if sum_cost < total_min:
            total_min = sum_cost

    print(total_min)

if __name__ == "__main__":
    main()
