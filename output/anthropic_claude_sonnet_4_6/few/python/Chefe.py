import sys

def main():
    data = sys.stdin.read().split()
    idx = 0
    
    N = int(data[idx]); idx+=1
    M = int(data[idx]); idx+=1
    I = int(data[idx]); idx+=1
    
    ages = [0] * (N+1)
    for i in range(1, N+1):
        ages[i] = int(data[idx]); idx+=1
    
    # managers[v] = set of direct managers of v
    # subordinates[v] = set of direct subordinates of v
    managers = [set() for _ in range(N+1)]
    subordinates = [set() for _ in range(N+1)]
    
    for _ in range(M):
        x = int(data[idx]); idx+=1
        y = int(data[idx]); idx+=1
        managers[y].add(x)
        subordinates[x].add(y)
    
    def get_all_managers(e):
        # BFS/DFS upward to find all managers
        visited = set()
        stack = list(managers[e])
        while stack:
            node = stack.pop()
            if node not in visited:
                visited.add(node)
                for m in managers[node]:
                    if m not in visited:
                        stack.append(m)
        return visited
    
    output = []
    
    for _ in range(I):
        cmd = data[idx]; idx+=1
        if cmd == 'P':
            e = int(data[idx]); idx+=1
            all_mgrs = get_all_managers(e)
            if not all_mgrs:
                output.append('*')
            else:
                min_age = min(ages[m] for m in all_mgrs)
                output.append(str(min_age))
        else:  # T
            a = int(data[idx]); idx+=1
            b = int(data[idx]); idx+=1
            # Swap positions of a and b in the chain of command
            # This means: a takes b's position and b takes a's position
            # We need to swap their edges
            
            # Get current edges for a and b
            mgrs_a = set(managers[a])
            mgrs_b = set(managers[b])
            subs_a = set(subordinates[a])
            subs_b = set(subordinates[b])
            
            # Remove all edges involving a and b
            for m in mgrs_a:
                subordinates[m].discard(a)
            for s in subs_a:
                managers[s].discard(a)
            for m in mgrs_b:
                subordinates[m].discard(b)
            for s in subs_b:
                managers[s].discard(b)
            
            managers[a] = set()
            managers[b] = set()
            subordinates[a] = set()
            subordinates[b] = set()
            
            # Now assign b's old edges to a and a's old edges to b
            # But we need to handle the case where a was manager of b or b was manager of a
            # Replace a with b and b with a in the edge sets
            
            new_mgrs_a = set()
            for m in mgrs_b:
                if m == a:
                    new_mgrs_a.add(b)
                else:
                    new_mgrs_a.add(m)
            
            new_mgrs_b = set()
            for m in mgrs_a:
                if m == b:
                    new_mgrs_b.add(a)
                else:
                    new_mgrs_b.add(m)
            
            new_subs_a = set()
            for s in subs_b:
                if s == a:
                    new_subs_a.add(b)
                else:
                    new_subs_a.add(s)
            
            new_subs_b = set()
            for s in subs_a:
                if s == b:
                    new_subs_b.add(a)
                else:
                    new_subs_b.add(s)
            
            managers[a] = new_mgrs_a
            managers[b] = new_mgrs_b
            subordinates[a] = new_subs_a
            subordinates[b] = new_subs_b
            
            # Rebuild reverse edges
            for m in managers[a]:
                subordinates[m].add(a)
            for s in subordinates[a]:
                managers[s].add(a)
            for m in managers[b]:
                subordinates[m].add(b)
            for s in subordinates[b]:
                managers[s].add(b)
    
    print('\n'.join(output))

main()