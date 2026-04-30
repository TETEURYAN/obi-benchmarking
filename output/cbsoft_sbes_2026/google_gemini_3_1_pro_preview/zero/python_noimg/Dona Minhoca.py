
import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    adj = [[] for _ in range(n + 1)]
    
    idx = 1
    for _ in range(n - 1):
        u = int(input_data[idx])
        v = int(input_data[idx+1])
        idx += 2
        adj[u].append(v)
        adj[v].append(u)
        
    def bfs(start):
        dist = [-1] * (n + 1)
        parent = [-1] * (n + 1)
        q = [start]
        dist[start] = 0
        
        farthest_node = start
        max_dist = 0
        
        head = 0
        while head < len(q):
            u = q[head]
            head += 1
            
            if dist[u] > max_dist:
                max_dist = dist[u]
                farthest_node = u
                
            for v in adj[u]:
                if dist[v] == -1:
                    dist[v] = dist[u] + 1
                    parent[v] = u
                    q.append(v)
                    
        return farthest_node, max_dist, parent

    A, _, _ = bfs(1)
    B, D, parent = bfs(A)
    
    path = []
    curr = B
    while curr != -1:
        path.append(curr)
        curr = parent[curr]
        
    if D % 2 == 0:
        C = path[D // 2]
        target_depth = D // 2
        
        dist = [-1] * (n + 1)
        branch = [-1] * (n + 1)
        
        q = [C]
        dist[C] = 0
        
        for neighbor in adj[C]:
            dist[neighbor] = 1
            branch[neighbor] = neighbor
            q.append(neighbor)
            
        head = 1
        counts_dict = {}
        
        while head < len(q):
            u = q[head]
            head += 1
            
            if dist[u] == target_depth:
                b = branch[u]
                counts_dict[b] = counts_dict.get(b, 0) + 1
            elif dist[u] < target_depth:
                for v in adj[u]:
                    if dist[v] == -1:
                        dist[v] = dist[u] + 1
                        branch[v] = branch[u]
                        q.append(v)
                        
        counts = list(counts_dict.values())
        
        total_pairs = 0
        sum_counts = sum(counts)
        for c in counts:
            total_pairs += c * (sum_counts - c)
        total_pairs //= 2
        
        print(D + 1)
        print(total_pairs)
        
    else:
        C1 = path[D // 2]
        C2 = path[D // 2 + 1]
        target_depth = D // 2
        
        def get_count(start, ignore, target):
            q = [start]
            dist = [-1] * (n + 1)
            dist[start] = 0
            dist[ignore] = -2
            
            cnt = 0
            head = 0
            while head < len(q):
                u = q[head]
                head += 1
                
                if dist[u] == target:
                    cnt += 1
                elif dist[u] < target:
                    for v in adj[u]:
                        if dist[v] == -1:
                            dist[v] = dist[u] + 1
                            q.append(v)
            return cnt
            
        cnt1 = get_count(C1, C2, target_depth)
        cnt2 = get_count(C2, C1, target_depth)
        
        print(D + 1)
        print(cnt1 * cnt2)

if __name__ == '__main__':
    solve()
