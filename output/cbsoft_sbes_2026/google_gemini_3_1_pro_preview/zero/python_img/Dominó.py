
import sys

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
        
        degree = [0] * 7
        adj = {i: [] for i in range(7)}
        
        for _ in range(n):
            u = int(input_data[idx])
            v = int(input_data[idx+1])
            idx += 2
            
            degree[u] += 1
            degree[v] += 1
            adj[u].append(v)
            adj[v].append(u)
            
        odd_count = sum(1 for i in range(7) if degree[i] % 2 != 0)
        
        possible = True
        if odd_count != 0 and odd_count != 2:
            possible = False
        else:
            start_node = -1
            for i in range(7):
                if degree[i] > 0:
                    start_node = i
                    break
            
            if start_node != -1:
                visited = [False] * 7
                queue = [start_node]
                visited[start_node] = True
                
                while queue:
                    curr = queue.pop(0)
                    for neighbor in adj[curr]:
                        if not visited[neighbor]:
                            visited[neighbor] = True
                            queue.append(neighbor)
                
                for i in range(7):
                    if degree[i] > 0 and not visited[i]:
                        possible = False
                        break
        
        print(f"Teste {test_case}")
        if possible:
            print("sim")
        else:
            print("nao")
        print()
        
        test_case += 1

if __name__ == '__main__':
    solve()
