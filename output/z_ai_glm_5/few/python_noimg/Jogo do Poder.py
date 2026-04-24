import sys

# Increase recursion depth just in case, though DSU is iterative
sys.setrecursionlimit(200000)

def solve():
    # Read all input at once
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return

    iterator = iter(input_data)
    
    try:
        N = int(next(iterator))
        M = int(next(iterator))
    except StopIteration:
        return

    # Total number of cells
    V = N * M
    
    # Arrays for grid values and coordinates
    # Using lists of appropriate size
    powers = [0] * V
    coords = [] # Will store (power, index)
    
    # Reading the grid
    # We flatten the grid to a 1D array for easier processing
    # Index mapping: row * M + col
    for r in range(N):
        for c in range(M):
            val = int(next(iterator))
            idx = r * M + c
            powers[idx] = val
            coords.append((val, idx))
            
    # Sort cells by power
    coords.sort()
    
    # DSU structures
    parent = list(range(V))
    size = [1] * V # Not strictly needed for size, but good for DSU rank heuristic if used
    component_sum = [0] * V # Total power of the component
    max_ans = [0] * V # Max power achievable from this component (if it were isolated)
    
    # For managing the 'alive' nodes in a component
    # alive_head[u] points to the first node in the circular linked list of alive nodes in u's component
    # next_alive[u] points to the next node in the list
    alive_head = list(range(V))
    next_alive = list(range(V)) # Initially each points to itself? Or -1?
    # Let's use a simple linked list: head -> node1 -> node2 -> ... -> None
    # Initially: head[i] = i, next[i] = -1
    
    # Re-initializing for simple linked list logic
    for i in range(V):
        alive_head[i] = i
        next_alive[i] = -1
        
    # Final answers array
    ans = [0] * V
    
    # Active status of a cell (processed or not)
    active = [False] * V
    
    # Helper to find root
    def find(i):
        path = []
        while parent[i] != i:
            path.append(i)
            i = parent[i]
        for node in path:
            parent[node] = i
        return i

    # Process nodes in increasing order of power
    for p_val, u in coords:
        # Initialize component for the current node
        # It starts as active with its own power
        active[u] = True
        component_sum[u] = p_val
        # max_ans for a single node is its own power
        # alive_head[u] is already u, next_alive[u] is -1
        
        # Store neighbors' roots
        neighbor_roots = set()
        
        # Check 4 neighbors
        r, c = divmod(u, M)
        if r > 0: neighbor_roots.add((u - M))
        if r < N - 1: neighbor_roots.add((u + M))
        if c > 0: neighbor_roots.add((u - 1))
        if c < M - 1: neighbor_roots.add((u + 1))
        
        # We collect unique roots of active neighbors
        active_neighbor_roots = []
        for v_flat in neighbor_roots:
            if active[v_flat]:
                root_v = find(v_flat)
                # Check if this root is already added (since multiple neighbors can belong to same component)
                # We use a local visited marker or just check if root_v is in a temporary set
                # Since we process roots, we can just use a set
                # But to keep it efficient, we can mark them. 
                # However, simple set addition is fine given constraints.
                if root_v not in neighbor_roots: # reusing set is not good, make new set
                    pass
        
        # Correct neighbor collection logic
        unique_roots = set()
        if r > 0:
            v = u - M
            if active[v]: unique_roots.add(find(v))
        if r < N - 1:
            v = u + M
            if active[v]: unique_roots.add(find(v))
        if c > 0:
            v = u - 1
            if active[v]: unique_roots.add(find(v))
        if c < M - 1:
            v = u + 1
            if active[v]: unique_roots.add(find(v))
            
        # List of components to merge
        # We need to decide which components survive (can be absorbed by u)
        # and which die (cannot be absorbed, but u absorbs them)
        
        # Calculate total potential sum
        total_sum = p_val
        for root in unique_roots:
            total_sum += component_sum[root]
            
        # We will merge all of them into u.
        # u becomes the new root.
        # We must determine which 'alive' lists survive.
        
        # If a component root has max_ans[root] < p_val, it means the nodes in that component
        # cannot absorb u. So they 'die'. We finalize their answers.
        # Otherwise, they survive and are linked to u's alive list.
        
        # Prepare for merging
        # u is the new root
        parent[u] = u # redundant but safe
        component_sum[u] = total_sum
        
        # Construct new alive list for u
        # Start with u itself
        current_alive_head = u
        current_alive_tail = u
        next_alive[u] = -1
        
        for root in unique_roots:
            # Merge DSU
            parent[root] = u
            
            # Check survival condition
            # The condition for a component to be able to absorb u is:
            # max_ans[root] >= p_val
            # Note: max_ans[root] is the sum of that component.
            
            if max_ans[root] >= p_val:
                # This component survives!
                # Link its alive list to u's list
                # We append it to the end of our current list
                next_alive[current_alive_tail] = alive_head[root]
                current_alive_tail = root # The root stores the tail pointer? 
                # No, we need to find tail. 
                # Optimization: We can just prepend. Order doesn't matter.
                # Prepend:
                # next_alive[root's tail] = current_alive_head
                # current_alive_head = alive_head[root]
                # But finding tail is O(size).
                # Better: We can just link head to head.
                # next_alive[u] = alive_head[root]?
                # This creates a list: u -> root's list.
                # But we have multiple roots.
                # u -> root1 -> root2?
                # Let's just iterate and link.
                # To avoid O(N^2) with finding tails, we can link head to tail.
                # Since we iterate unique_roots, let's just link head-to-head.
                
                # New list: u -> root's list
                # But we need to preserve u's list too.
                # next_alive[u] should point to the head of the merged list.
                # Wait, if we do:
                # temp = next_alive[u]
                # next_alive[u] = alive_head[root]
                # last_of_root = ...
                # last_of_root.next = temp
                # This requires finding last of root.
                
                # Efficient linking:
                # Since we only need to iterate the list at the end (or when it dies), 
                # and total iterations are bounded by N, we can just link head to head?
                # No, that breaks the list structure (two heads pointing to same next).
                
                # Correct efficient linking:
                # Link tail of new component to head of old accumulator.
                # We need to find tail of 'root'.
                # Since we iterate 'root's list to set answers when it dies, 
                # finding tail here adds to complexity.
                # BUT, we only find tail if it survives.
                # And we only iterate list if it dies.
                # So we can afford to find tail here?
                # Sum of lengths found = N.
                # Sum of iterations to find tail = N.
                # So it is O(N) total.
                
                # Find tail of root's alive list
                curr = alive_head[root]
                if curr != -1:
                    # Append current_accumulator to end of root's list
                    # Find tail
                    tail = curr
                    while next_alive[tail] != -1:
                        tail = next_alive[tail]
                    
                    # Link: root's list -> current_accumulator
                    next_alive[tail] = current_alive_head
                    current_alive_head = alive_head[root]

            else:
                # Component dies
                # Finalize answers for all in alive_head[root]
                curr = alive_head[root]
                while curr != -1:
                    ans[curr] = max_ans[root]
                    curr = next_alive[curr]
        
        # Update u's component info
        alive_head[u] = current_alive_head
        max_ans[u] = total_sum
        
    # After processing all nodes, any remaining alive nodes have the max possible answer
    # which is the sum of their final component.
    # We iterate over all nodes. If ans[i] is 0, it might be part of an alive component.
    # But 0 is a valid power? No, powers >= 1.
    # However, a node might have ans 0 if it was never processed?
    # All nodes are processed.
    # We just need to process the final alive lists.
    
    # We can iterate all roots.
    for i in range(V):
        if parent[i] == i: # Is a root
            # If it's a root, it might still have alive nodes
            # Actually, only the final roots of each connected component will be roots.
            # And only those that were never killed.
            # But wait, if a component was killed, its nodes have ans set.
            # We just need to check if the root's alive list is valid.
            # But we don't have a 'dead' marker for the head.
            # We can rely on ans array. If ans[i] == 0, it's alive.
            # But we need to update everyone in the list.
            
            # Let's just traverse alive_head[i] for all roots i.
            # If a node was killed, it is NOT in the alive_head of its parent anymore.
            # It was removed.
            # So any node in alive_head[i] is alive and needs ans = max_ans[i].
            
            curr = alive_head[i]
            while curr != -1:
                ans[curr] = max_ans[i]
                curr = next_alive[curr]

    # Print output
    # Format: N lines, M integers each
    output_buffer = []
    for r in range(N):
        row_vals = ans[r*M : (r+1)*M]
        output_buffer.append(" ".join(map(str, row_vals)))
    
    sys.stdout.write("\n".join(output_buffer) + "\n")

if __name__ == '__main__':
    solve()