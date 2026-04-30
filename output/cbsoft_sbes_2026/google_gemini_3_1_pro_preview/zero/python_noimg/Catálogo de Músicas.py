
import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    N = int(input_data[0])
    paths = input_data[1:N+1]
    
    # tree[node_id] = [name_len, count, {child_name: child_node_id}]
    tree = [[0, 0, {}]]
    
    initial_cost = 0
    
    for path in paths:
        initial_cost += len(path)
        parts = path.split('/')
        
        curr = 0
        tree[curr][1] += 1
        
        for i in range(len(parts) - 1):
            part = parts[i]
            if part not in tree[curr][2]:
                new_id = len(tree)
                tree.append([len(part), 0, {}])
                tree[curr][2][part] = new_id
            curr = tree[curr][2][part]
            tree[curr][1] += 1

    min_cost = initial_cost
    
    stack = [(0, initial_cost)]
    
    while stack:
        curr, current_cost = stack.pop()
        if current_cost < min_cost:
            min_cost = current_cost
            
        for child_name, child_id in tree[curr][2].items():
            child_len, child_count, _ = tree[child_id]
            # Calculate the cost if we move the reference directory to this child
            child_cost = current_cost + 3 * N - child_count * (child_len + 4)
            stack.append((child_id, child_cost))
            
    print(min_cost)

if __name__ == '__main__':
    solve()
