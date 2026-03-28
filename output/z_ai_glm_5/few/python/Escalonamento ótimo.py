import sys
import heapq

sys.setrecursionlimit(200000)

def solve():
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return

    iterator = iter(input_data)
    
    try:
        N = int(next(iterator))
        M = int(next(iterator))
    except StopIteration:
        return

    adj = [[] for _ in range(N)]
    in_degree = [0] * N

    for _ in range(M):
        try:
            u = int(next(iterator))
            v = int(next(iterator))
            adj[u].append(v)
            in_degree[v] += 1
        except StopIteration:
            break

    pq = []
    
    for i in range(N):
        if in_degree[i] == 0:
            heapq.heappush(pq, i)

    result = []
    
    while pq:
        u = heapq.heappop(pq)
        result.append(u)
        
        for v in adj[u]:
            in_degree[v] -= 1
            if in_degree[v] == 0:
                heapq.heappush(pq, v)

    if len(result) != N:
        sys.stdout.write("*\n")
    else:
        if result:
            sys.stdout.write("\n".join(map(str, result)) + "\n")

if __name__ == "__main__":
    solve()