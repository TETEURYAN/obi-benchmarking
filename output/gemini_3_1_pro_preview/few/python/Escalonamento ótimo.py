import sys
import heapq

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    m = int(input_data[1])
    
    adj = [[] for _ in range(n)]
    indegree = [0] * n
    
    it = iter(input_data[2:])
    for u_str, v_str in zip(it, it):
        u = int(u_str)
        v = int(v_str)
        adj[u].append(v)
        indegree[v] += 1
        
    heap = [i for i in range(n) if indegree[i] == 0]
    heapq.heapify(heap)
    
    order = []
    while heap:
        u = heapq.heappop(heap)
        order.append(u)
        for v in adj[u]:
            indegree[v] -= 1
            if indegree[v] == 0:
                heapq.heappush(heap, v)
                
    if len(order) == n:
        if n > 0:
            sys.stdout.write('\n'.join(map(str, order)) + '\n')
    else:
        sys.stdout.write("*\n")

if __name__ == '__main__':
    solve()