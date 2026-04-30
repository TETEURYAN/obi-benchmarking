
import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    N = int(input_data[0])
    paths = input_data[1:]
    
    children = {}
    adj = [[]]
    count = [0]
    name_len = [0]
    num_nodes = 1
    
    cost_root = 0
    
    for path in paths:
        cost_root += len(path)
        parts = path.split('/')
        curr = 0
        count[0] += 1
        for i in range(len(parts) - 1):
            part = parts[i]
            key = (curr, part)
            if key not in children:
                children[key] = num_nodes
                adj[curr].append(num_nodes)
                adj.append([])
                count.append(0)
                name_len.append(len(part))
                num_nodes += 1
            curr = children[key]
            count[curr] += 1
            
    min_cost = cost_root
    stack = [(0, cost_root)]
    
    while stack:
        u, cost_u = stack.pop()
        if cost_u < min_cost:
            min_cost = cost_u
            
        for v in adj[u]:
            cost_v = cost_u + 3 * N - count[v] * (name_len[v] + 4)
            stack.append((v, cost_v))
            
    print(min_cost)

if __name__ == '__main__':
    solve()
