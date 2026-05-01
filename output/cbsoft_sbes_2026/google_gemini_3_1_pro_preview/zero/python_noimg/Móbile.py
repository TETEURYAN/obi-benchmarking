import sys

sys.setrecursionlimit(100000)

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    N = int(input_data[0])
    
    adj = [[] for _ in range(N + 1)]
    root = 0
    
    idx = 1
    for _ in range(N):
        I = int(input_data[idx])
        J = int(input_data[idx+1])
        idx += 2
        if J == 0:
            root = I
        else:
            adj[J].append(I)
            
    balanced = True
    
    def dfs(u):
        nonlocal balanced
        if not balanced:
            return 0
        
        child_size = -1
        total_size = 1
        
        for v in adj[u]:
            sz = dfs(v)
            if child_size == -1:
                child_size = sz
            elif child_size != sz:
                balanced = False
            total_size += sz
            
        return total_size

    dfs(root)
    
    if balanced:
        print("bem")
    else:
        print("mal")

if __name__ == '__main__':
    solve()