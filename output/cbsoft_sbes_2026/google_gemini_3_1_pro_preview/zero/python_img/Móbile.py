
import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    N = int(input_data[0])
    
    tree = [[] for _ in range(N + 1)]
    
    idx = 1
    for _ in range(N):
        i = int(input_data[idx])
        j = int(input_data[idx+1])
        tree[j].append(i)
        idx += 2
        
    stack = [tree[0][0]]
    post_order = []
    
    while stack:
        u = stack.pop()
        post_order.append(u)
        for v in tree[u]:
            stack.append(v)
            
    sizes = [1] * (N + 1)
    is_balanced = True
    
    for u in reversed(post_order):
        if not tree[u]:
            sizes[u] = 1
            continue
            
        first_child_size = sizes[tree[u][0]]
        total = 1
        for v in tree[u]:
            if sizes[v] != first_child_size:
                is_balanced = False
                break
            total += sizes[v]
            
        if not is_balanced:
            break
        sizes[u] = total
        
    if is_balanced:
        print("bem")
    else:
        print("mal")

if __name__ == '__main__':
    solve()
