import sys
from collections import defaultdict

def main():
    input_data = sys.stdin.buffer.read().split()
    idx = 0
    N = int(input_data[idx]); idx += 1
    M = int(input_data[idx]); idx += 1
    
    edges = set()
    adj = defaultdict(list)
    
    for _ in range(M):
        x = int(input_data[idx]); idx += 1
        y = int(input_data[idx]); idx += 1
        adj[x].append(y)
        adj[y].append(x)
        if x > y:
            x, y = y, x
        edges.add((x, y))
    
    # Find connected components using BFS
    component = [-1] * (N + 1)
    comp_id = 0
    
    for start in range(1, N + 1):
        if component[start] == -1:
            # BFS
            queue = [start]
            component[start] = comp_id
            head = 0
            while head < len(queue):
                node = queue[head]
                head += 1
                for neighbor in adj[node]:
                    if component[neighbor] == -1:
                        component[neighbor] = comp_id
                        queue.append(neighbor)
            comp_id += 1
    
    # Group nodes by component
    comp_nodes = defaultdict(list)
    for node in range(1, N + 1):
        comp_nodes[component[node]].append(node)
    
    # The connectivity value = sum of C(size, 2) for each component
    # Adding edge (A, B) is redundant (connectivity stays same) if A and B are already in the same component
    # AND there's no existing edge between A and B
    
    # So we need to find two nodes in the same component with no direct edge between them
    # If any component has size >= 3, or size >= 2 and not fully connected (complete graph)
    
    # For each component, check if it's a complete graph
    # A complete graph on k nodes has k*(k-1)/2 edges
    # Count edges within each component
    
    comp_edge_count = defaultdict(int)
    for (x, y) in edges:
        # x < y
        comp_edge_count[component[x]] += 1
    
    for cid, nodes in comp_nodes.items():
        k = len(nodes)
        max_edges = k * (k - 1) // 2
        actual_edges = comp_edge_count[cid]
        
        if actual_edges < max_edges:
            # There exists a pair in this component with no direct edge
            # Find such a pair
            # For efficiency, iterate over nodes and check adjacency
            node_set = set(nodes)
            adj_set = defaultdict(set)
            for node in nodes:
                for neighbor in adj[node]:
                    if neighbor in node_set:
                        adj_set[node].add(neighbor)
            
            # Find pair not connected
            found = False
            for i in range(len(nodes)):
                if found:
                    break
                u = nodes[i]
                for j in range(i + 1, len(nodes)):
                    v = nodes[j]
                    if v not in adj_set[u]:
                        print(u, v)
                        found = True
                        break
            if found:
                return
    
    print(-1)

main()