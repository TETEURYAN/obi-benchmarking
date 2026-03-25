import sys
sys.setrecursionlimit(200000)

def main():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    N = int(next(it))
    M = int(next(it))
    
    if N == 0:
        return
    
    graph = [[] for _ in range(N)]
    indeg = [0] * N
    
    for _ in range(M):
        a = int(next(it))
        b = int(next(it))
        graph[a].append(b)
        indeg[b] += 1
    
    import heapq
    heap = []
    for i in range(N):
        if indeg[i] == 0:
            heapq.heappush(heap, i)
    
    result = []
    while heap:
        u = heapq.heappop(heap)
        result.append(u)
        for v in graph[u]:
            indeg[v] -= 1
            if indeg[v] == 0:
                heapq.heappush(heap, v)
    
    if len(result) != N:
        sys.stdout.write("*\n")
    else:
        sys.stdout.write("\n".join(map(str, result)) + "\n")

if __name__ == "__main__":
    main()