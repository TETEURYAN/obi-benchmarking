import sys
import heapq

def main():
    data = sys.stdin.read().split()
    if not data:
        print("*")
        return
    
    idx = 0
    n = int(data[idx]); idx += 1
    m = int(data[idx]); idx += 1
    
    if n == 0:
        return
    
    in_degree = [0] * n
    adj = [[] for _ in range(n)]
    
    for _ in range(m):
        a = int(data[idx]); idx += 1
        b = int(data[idx]); idx += 1
        adj[a].append(b)
        in_degree[b] += 1
    
    heap = []
    for i in range(n):
        if in_degree[i] == 0:
            heapq.heappush(heap, i)
    
    result = []
    while heap:
        task = heapq.heappop(heap)
        result.append(task)
        for neighbor in adj[task]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                heapq.heappush(heap, neighbor)
    
    if len(result) != n:
        print("*")
    else:
        sys.stdout.write("\n".join(map(str, result)) + "\n")

main()