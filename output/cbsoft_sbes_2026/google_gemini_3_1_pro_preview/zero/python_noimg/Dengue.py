import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    iterator = iter(input_data)
    
    test_case = 1
    while True:
        try:
            n_str = next(iterator)
        except StopIteration:
            break
        n = int(n_str)
        if n == 0:
            break
        
        adj = {i: [] for i in range(1, n + 1)}
        for _ in range(n - 1):
            u = int(next(iterator))
            v = int(next(iterator))
            adj[u].append(v)
            adj[v].append(u)
        
        min_max_dist = float('inf')
        best_node = -1
        
        for i in range(1, n + 1):
            q = [i]
            dist = {i: 0}
            max_dist = 0
            
            head = 0
            while head < len(q):
                curr = q[head]
                head += 1
                
                for neighbor in adj[curr]:
                    if neighbor not in dist:
                        dist[neighbor] = dist[curr] + 1
                        if dist[neighbor] > max_dist:
                            max_dist = dist[neighbor]
                        q.append(neighbor)
            
            if max_dist < min_max_dist:
                min_max_dist = max_dist
                best_node = i
                
        print(f"Teste {test_case}")
        print(best_node)
        print()
        
        test_case += 1

if __name__ == '__main__':
    solve()