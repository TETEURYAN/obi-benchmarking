import sys

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    idx = 0
    test_case = 1
    
    while idx < len(input_data):
        E = int(input_data[idx])
        L = int(input_data[idx+1])
        idx += 2
        
        if E == 0 and L == 0:
            break
            
        adj = [[] for _ in range(E + 1)]
        
        for _ in range(L):
            u = int(input_data[idx])
            v = int(input_data[idx+1])
            idx += 2
            adj[u].append(v)
            adj[v].append(u)
            
        visited = [False] * (E + 1)
        stack = [1]
        visited[1] = True
        count = 1
        
        while stack:
            node = stack.pop()
            for neighbor in adj[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    count += 1
                    stack.append(neighbor)
                    
        print(f"Teste {test_case}")
        if count == E:
            print("normal")
        else:
            print("falha")
        print()
        
        test_case += 1

if __name__ == '__main__':
    main()