 sys
from collections import defaultdict

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    
    n = int(data[0])
    graph = defaultdict(list)
    for i in range(1, n+1):
        u = int(data[2*i-1])
        v = int(data[2*i])
        graph[v].append(u)
    
    balanced = True
    def dfs(node):
        nonlocal balanced
        if not graph[node]:
            return 1
        
        sizes = []
        for child in graph[node]:
            sizes.append(dfs(child))
        
        if len(set(sizes)) != 1:
            balanced = False
        
        return 1 + sum(sizes)
    
    dfs(0)
    print('bem' if balanced else 'mal')

if __name__ == '__main__':
    main()
