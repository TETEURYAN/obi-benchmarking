import sys
input = sys.stdin.readline

def main():
    data = sys.stdin.read().split()
    idx = 0
    N = int(data[idx]); idx+=1
    M = int(data[idx]); idx+=1
    I = int(data[idx]); idx+=1
    
    ages = [0] * (N+1)
    for i in range(1, N+1):
        ages[i] = int(data[idx]); idx+=1
    
    # managers[x] = set of direct managers of x
    # subordinates[x] = set of direct subordinates of x
    managers = [set() for _ in range(N+1)]
    subordinates = [set() for _ in range(N+1)]
    
    for _ in range(M):
        x = int(data[idx]); idx+=1
        y = int(data[idx]); idx+=1
        managers[y].add(x)
        subordinates[x].add(y)
    
    def get_all_managers(e):
        # BFS/DFS to get all managers (direct and indirect)
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
    
    def swap(a, b):
        # Swap positions of a and b in the chain of command
        # a's managers become b's managers and vice versa
        # a's subordinates become b's subordinates and vice versa
        # But we need to be careful if a is a manager of b or b is a manager of a
        
        managers_a = set(managers[a])
        managers_b = set(managers[b])
        subs_a = set(subordinates[a])
        subs_b = set(subordinates[b])
        
        # Remove a from its managers' subordinates and its subordinates' managers
        for m in managers_a:
            subordinates[m].discard(a)
        for s in subs_a:
            managers[s].discard(a)
        
        # Remove b from its managers' subordinates and its subordinates' managers
        for m in managers_b:
            subordinates[m].discard(b)
        for s in subs_b:
            managers[s].discard(b)
        
        # Now assign b's old position to a and a's old position to b
        # But replace a with b and b with a in the sets
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
        
        managers[a] = new_managers_a
        managers[b] = new_managers_b
        subordinates[a] = new_subs_a
        subordinates[b] = new_subs_b
        
        # Update references
        for m in managers[a]:
            subordinates[m].add(a)
        for s in subordinates[a]:
            managers[s].add(a)
        
        for m in managers[b]:
            subordinates[m].add(b)
        for s in subordinates[b]:
            managers[s].add(b)
    
    results = []
    
    for _ in range(I):
        cmd = data[idx]; idx+=1
        if cmd == 'P':
            e = int(data[idx]); idx+=1
            all_mgrs = get_all_managers(e)
            if not all_mgrs:
                results.append('*')
            else:
                min_age = min(ages[m] for m in all_mgrs)
                results.append(str(min_age))
        else:  # T
            a = int(data[idx]); idx+=1
            b = int(data[idx]); idx+=1
            swap(a, b)
    
    print('\n'.join(results))

main()