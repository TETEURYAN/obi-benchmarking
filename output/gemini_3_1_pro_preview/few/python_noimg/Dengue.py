import sys

sys.setrecursionlimit(200000)

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    idx = 0
    test_case = 1
    while idx < len(input_data):
        n = int(input_data[idx])
        idx += 1
        if n == 0:
            break
        
        adj = [[] for _ in range(n + 1)]
        for _ in range(n - 1):
            u = int(input_data[idx])
            v = int(input_data[idx+1])
            adj[u].append(v)
            adj[v].append(u)
            idx += 2
            
        min_max_dist = float('inf')
        best_node = -1
        
        for i in range(1, n + 1):
            dist = [-1] * (n + 1)
            dist[i] = 0
            q = [i]
            max_d = 0
            for curr in q:
                for nxt in adj[curr]:
                    if dist[nxt] == -1:
                        dist[nxt] = dist[curr] + 1
                        if dist[nxt] > max_d:
                            max_d = dist[nxt]
                        q.append(nxt)
            
            if max_d < min_max_dist:
                min_max_dist = max_d
                best_node = i
                
        print(f"Teste {test_case}")
        print(best_node)
        print()
        
        test_case += 1

if __name__ == '__main__':
    solve()