import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    N = int(input_data[0])
    P = int(input_data[1])
    Q = int(input_data[2])
    
    if Q < 0:
        P = -P
        Q = -Q
        
    it = iter(input_data[3:])
    mapped = map(int, it)
    pts = sorted(zip(mapped, mapped), key=lambda p: p[0])
    
    W = [Q * y - P * x for x, y in pts]
    
    unique_W = sorted(set(W))
    rank = {val: i + 1 for i, val in enumerate(unique_W)}
    
    tree = [0] * (len(unique_W) + 1)
    tree_len = len(tree)
    
    ans = 0
    for w in W:
        r = rank[w]
        
        s = 0
        i = r
        while i > 0:
            s += tree[i]
            i -= i & (-i)
        ans += s
        
        i = r
        while i < tree_len:
            tree[i] += 1
            i += i & (-i)
            
    print(ans)

solve()