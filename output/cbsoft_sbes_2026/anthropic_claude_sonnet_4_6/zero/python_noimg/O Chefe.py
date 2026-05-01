import sys
from sys import stdin

def main():
    input = stdin.read().split()
    idx = 0
    
    N = int(input[idx]); idx+=1
    M = int(input[idx]); idx+=1
    I = int(input[idx]); idx+=1
    
    ages = [0] * (N+1)
    for i in range(1, N+1):
        ages[i] = int(input[idx]); idx+=1
    
    # managers[i] = set of direct managers of i
    # subordinates[i] = set of direct subordinates of i
    managers = [set() for _ in range(N+1)]
    subordinates = [set() for _ in range(N+1)]
    
    for _ in range(M):
        x = int(input[idx]); idx+=1
        y = int(input[idx]); idx+=1
        managers[y].add(x)
        subordinates[x].add(y)
    
    results = []
    
    for _ in range(I):
        cmd = input[idx]; idx+=1
        
        if cmd == 'P':
            e = int(input[idx]); idx+=1
            # Find all direct and indirect managers of e
            # BFS/DFS upward
            visited = set()
            stack = list(managers[e])
            for m in stack:
                visited.add(m)
            
            while stack:
                node = stack.pop()
                for m in managers[node]:
                    if m not in visited:
                        visited.add(m)
                        stack.append(m)
            
            if not visited:
                results.append('*')
            else:
                min_age = min(ages[m] for m in visited)
                results.append(str(min_age))
        
        else:  # T
            a = int(input[idx]); idx+=1
            b = int(input[idx]); idx+=1
            
            # Swap positions of a and b in the chain of command
            # This means: a takes b's position and b takes a's position
            # We need to swap their edges
            
            # Get managers and subordinates of a and b
            managers_a = set(managers[a])
            managers_b = set(managers[b])
            subordinates_a = set(subordinates[a])
            subordinates_b = set(subordinates[b])
            
            # Remove a from its managers' subordinates and subordinates' managers
            for m in managers_a:
                subordinates[m].discard(a)
            for s in subordinates_a:
                managers[s].discard(a)
            
            # Remove b from its managers' subordinates and subordinates' managers
            for m in managers_b:
                subordinates[m].discard(b)
            for s in subordinates_b:
                managers[s].discard(b)
            
            # Handle the case where a manages b or b manages a
            # If a is in managers_b, then after swap b should be in managers_a's position
            # We need to handle cross-references
            
            # Replace a with b in b's old connections, and b with a in a's old connections
            # But we need to handle if a was manager of b or b was manager of a
            
            new_managers_a = set()
            for m in managers_b:
                if m == a:
                    new_managers_a.add(b)
                else:
                    new_managers_a.add(m)
            
            new_managers_b = set()
            for m in managers_a:
                if m == b:
                    new_managers_b.add(a)
                else:
                    new_managers_b.add(m)
            
            new_subordinates_a = set()
            for s in subordinates_b:
                if s == a:
                    new_subordinates_a.add(b)
                else:
                    new_subordinates_a.add(s)
            
            new_subordinates_b = set()
            for s in subordinates_a:
                if s == b:
                    new_subordinates_b.add(a)
                else:
                    new_subordinates_b.add(s)
            
            managers[a] = new_managers_a
            managers[b] = new_managers_b
            subordinates[a] = new_subordinates_a
            subordinates[b] = new_subordinates_b
            
            # Update neighbors
            for m in managers[a]:
                subordinates[m].add(a)
            for s in subordinates[a]:
                managers[s].add(a)
            
            for m in managers[b]:
                subordinates[m].add(b)
            for s in subordinates[b]:
                managers[s].add(b)
    
    print('\n'.join(results))

main()