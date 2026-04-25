import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    
    parent = list(range(n + 1))
    size = [1] * (n + 1)
    
    def find(i):
        root = i
        while parent[root] != root:
            root = parent[root]
        curr = i
        while curr != root:
            nxt = parent[curr]
            parent[curr] = root
            curr = nxt
        return root

    def union(i, j):
        root_i = find(i)
        root_j = find(j)
        if root_i != root_j:
            if size[root_i] < size[root_j]:
                root_i, root_j = root_j, root_i
            parent[root_j] = root_i
            size[root_i] += size[root_j]

    idx = 1
    for _ in range(n - 1):
        u = int(input_data[idx])
        v = int(input_data[idx+1])
        c = int(input_data[idx+2])
        idx += 3
        
        if c == 0:
            union(u, v)
            
    ans = n * (n - 1) // 2
    for i in range(1, n + 1):
        if parent[i] == i:
            s = size[i]
            ans -= s * (s - 1) // 2
            
    print(ans)

if __name__ == '__main__':
    solve()