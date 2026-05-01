import sys

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    idx = 0
    teste = 1
    while idx < len(input_data):
        n = int(input_data[idx])
        idx += 1
        if n == 0:
            break
        
        adj = [[] for _ in range(7)]
        degree = [0] * 7
        
        for _ in range(n):
            u = int(input_data[idx])
            v = int(input_data[idx+1])
            idx += 2
            adj[u].append(v)
            adj[v].append(u)
            degree[u] += 1
            degree[v] += 1
            
        odd_count = sum(1 for d in degree if d % 2 != 0)
        
        ans = "sim"
        if odd_count != 0 and odd_count != 2:
            ans = "nao"
        else:
            visited = [False] * 7
            start_node = -1
            for i in range(7):
                if degree[i] > 0:
                    start_node = i
                    break
            
            if start_node != -1:
                stack = [start_node]
                visited[start_node] = True
                while stack:
                    curr = stack.pop()
                    for neighbor in adj[curr]:
                        if not visited[neighbor]:
                            visited[neighbor] = True
                            stack.append(neighbor)
                
                for i in range(7):
                    if degree[i] > 0 and not visited[i]:
                        ans = "nao"
                        break
        
        print(f"Teste {teste}")
        print(ans)
        print()
        teste += 1

if __name__ == '__main__':
    main()