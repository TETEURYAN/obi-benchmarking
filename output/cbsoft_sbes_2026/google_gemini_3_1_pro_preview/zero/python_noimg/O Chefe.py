
import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    idx = 0
    n_tokens = len(input_data)
    
    out = []
    
    while idx < n_tokens:
        N = int(input_data[idx])
        M = int(input_data[idx+1])
        I = int(input_data[idx+2])
        idx += 3
        
        age = [0] * (N + 1)
        for i in range(1, N + 1):
            age[i] = int(input_data[idx])
            idx += 1
            
        rev_adj = [[] for _ in range(N + 1)]
        for _ in range(M):
            u = int(input_data[idx])
            v = int(input_data[idx+1])
            idx += 2
            rev_adj[v].append(u)
            
        pos = list(range(N + 1))
        emp = list(range(N + 1))
        reachable = [None] * (N + 1)
        
        for _ in range(I):
            type = input_data[idx]
            idx += 1
            if type == 'T':
                A = int(input_data[idx])
                B = int(input_data[idx+1])
                idx += 2
                
                u = pos[A]
                v = pos[B]
                emp[u], emp[v] = emp[v], emp[u]
                pos[A] = v
                pos[B] = u
            else:
                E = int(input_data[idx])
                idx += 1
                
                u = pos[E]
                if reachable[u] is None:
                    visited = [False] * (N + 1)
                    stack = [u]
                    visited[u] = True
                    reach = []
                    while stack:
                        curr = stack.pop()
                        for neighbor in rev_adj[curr]:
                            if not visited[neighbor]:
                                visited[neighbor] = True
                                stack.append(neighbor)
                                reach.append(neighbor)
                    reachable[u] = reach
                    
                reach = reachable[u]
                if not reach:
                    out.append("*")
                else:
                    min_a = 1000
                    for node in reach:
                        a = age[emp[node]]
                        if a < min_a:
                            min_a = a
                    out.append(str(min_a))
                    
    if out:
        sys.stdout.write('\n'.join(out) + '\n')

if __name__ == '__main__':
    solve()
