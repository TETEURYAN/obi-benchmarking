import sys

def solve():
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
            
        adj = {i: [] for i in range(1, E + 1)}
        for _ in range(L):
            u = int(input_data[idx])
            v = int(input_data[idx+1])
            idx += 2
            adj[u].append(v)
            adj[v].append(u)
            
        visited = set()
        stack = [1]
        visited.add(1)
        
        while stack:
            node = stack.pop()
            for neighbor in adj[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    stack.append(neighbor)
                    
        print(f"Teste {test_case}")
        if len(visited) == E:
            print("normal")
        else:
            print("falha")
        print()
        
        test_case += 1

if __name__ == '__main__':
    solve()