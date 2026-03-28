import sys

def main():
    # Read all input at once for efficiency
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return

    iterator = iter(input_data)
    test_case_num = 1
    output_buffer = []

    while True:
        try:
            n_str = next(iterator)
            n = int(n_str)
        except StopIteration:
            break
        
        if n == 0:
            break
        
        # Build graph (adjacency list) and calculate initial degrees
        adj = [[] for _ in range(n + 1)]
        degree = [0] * (n + 1)
        
        # Read N-1 edges
        for _ in range(n - 1):
            u = int(next(iterator))
            v = int(next(iterator))
            adj[u].append(v)
            adj[v].append(u)
            degree[u] += 1
            degree[v] += 1
        
        # Find the center of the tree using the "peeling onion" method (topological sort)
        # The center(s) will be the last node(s) remaining
        
        # Queue for current leaves (nodes with degree 1)
        # Using a list and an index pointer for efficiency (simulating a queue)
        leaves = []
        for i in range(1, n + 1):
            if degree[i] == 1:
                leaves.append(i)
        
        # Track the number of remaining nodes
        remaining_nodes = n
        # Track processed nodes
        processed = [False] * (n + 1)
        
        queue_head = 0
        
        # While there are more than 2 nodes remaining
        while remaining_nodes > 2:
            # Process current layer of leaves
            # We identify the size of the current layer to process them all at once
            # though processing one-by-one also works for correctness.
            # We must ensure we don't process nodes added in this same iteration.
            
            current_layer_size = len(leaves) - queue_head
            
            for _ in range(current_layer_size):
                if queue_head >= len(leaves):
                    break
                
                u = leaves[queue_head]
                queue_head += 1
                
                processed[u] = True
                remaining_nodes -= 1
                
                for v in adj[u]:
                    if not processed[v]:
                        degree[v] -= 1
                        if degree[v] == 1:
                            leaves.append(v)
        
        # Find the nodes that were not processed (the center(s))
        center = -1
        for i in range(1, n + 1):
            if not processed[i]:
                center = i
                break # The problem accepts any valid center, so we can pick the first one found
        
        # If N=1, the loop doesn't run, processed is all False, center is 1. Correct.
        # If N=2, loop condition (2 > 2) is false, processed is all False, center is 1. Correct.
        
        output_buffer.append(f"Teste {test_case_num}")
        output_buffer.append(str(center))
        output_buffer.append("") # Blank line required by problem
        
        test_case_num += 1

    # Print all output at once
    sys.stdout.write("\n".join(output_buffer))

if __name__ == "__main__":
    main()