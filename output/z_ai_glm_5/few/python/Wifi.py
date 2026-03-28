import sys

# Increase recursion depth just in case, though we use iterative/segment tree approaches
sys.setrecursionlimit(200000)

def solve():
    # Read all input at once
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    iterator = iter(input_data)
    try:
        N = int(next(iterator))
    except StopIteration:
        return

    rects = []
    events = []
    y_coords = set()

    # Read rectangles
    for i in range(N):
        x1 = int(next(iterator))
        y1 = int(next(iterator))
        x2 = int(next(iterator))
        y2 = int(next(iterator))
        
        # Store original index, coordinates
        # Note: y1 is top (larger), y2 is bottom (smaller)
        rects.append((x1, y1, x2, y2, i))
        
        # Collect y coordinates for compression
        y_coords.add(y1)
        y_coords.add(y2)
        
        # Create events: (x_coord, type, x2, y1, y2, original_index)
        # Type 0: Start (x1), Type 1: End (x2)
        # We process Start events before End events if x1 == x2 (though problem implies strict containment/non-intersection)
        # For Start events, we sort by x2 descending to ensure parents are processed before children
        events.append((x1, 0, x2, y1, y2, i))
        events.append((x2, 1, x2, y1, y2, i))

    # Coordinate Compression for Y
    sorted_y = sorted(list(y_coords))
    y_map = {val: i for i, val in enumerate(sorted_y)}
    M = len(sorted_y)

    # Sort events
    # Primary: x coordinate
    # Secondary: type (0 comes before 1)
    # Tertiary (for type 0): x2 descending (wider rectangles first -> parents first)
    events.sort(key=lambda e: (e[0], e[1], -e[2] if e[1] == 0 else e[2]))

    # Segment Tree for Y-interval management
    # Each node stores a stack of indices (representing rectangles covering that segment)
    # and the minimum value in that segment's subtree considering the stack tops.
    tree_stacks = [[] for _ in range(4 * M)]
    tree_min_sub = [0] * (4 * M) # min_sub value for the subtree

    # Helper to get top of stack
    def get_top(node):
        if not tree_stacks[node]:
            return 0
        return tree_stacks[node][-1]

    # Helper to update a node's min_sub value based on children and own stack
    def update_node(node, l_child, r_child):
        top_val = get_top(node)
        # The value at any point in this node's range is max(top_val, value_from_child)
        # We want the minimum of these values in the range.
        # min_sub[node] = min( max(top, min_sub[left]), max(top, min_sub[right]) )
        # Since we push in increasing order of index, top_val is always >= children's values?
        # Actually, indices are assigned arbitrarily, but we push parents (larger area) first.
        # Wait, the indices are just identifiers. The 'depth' in the tree matters.
        # But for the query logic to work (finding the deepest container), we just need the indices.
        # The Segment Tree logic relies on the fact that if a node has a value v on stack,
        # it covers the whole segment. The children might have more specific (larger index) values.
        # Since we process parents first, parents have smaller indices? No, indices are 0..N-1.
        # We need to ensure that the 'value' we store represents the 'depth' or a comparable metric.
        # Actually, the problem reduces to finding the parent. The parent is the one on top of the stack.
        # The 'min' query logic works if the value represents the index.
        # Let's stick to storing the index.
        
        # Logic verification:
        # If node has top v, children have top u (u > v, processed later).
        # In child range, value is u. In rest of node range, value is v.
        # min is min(u, v) = v.
        # Formula: min(max(v, min_sub[L]), max(v, min_sub[R]))
        # If min_sub[L] = u, max(v, u) = u.
        # If min_sub[R] = v (no child overlap), max(v, v) = v.
        # Result min(u, v) = v. Correct.
        
        tree_min_sub[node] = min(max(top_val, tree_min_sub[l_child]), max(top_val, tree_min_sub[r_child]))

    # Update range: push or pop value
    def update(node, start, end, l, r, val, is_push):
        if l > end or r < start:
            return
        
        if l <= start and end <= r:
            if is_push:
                tree_stacks[node].append(val)
            else:
                if tree_stacks[node]:
                    tree_stacks[node].pop()
            
            # Update min_sub for this node.
            # If leaf, min_sub is just the top.
            if start == end:
                tree_min_sub[node] = get_top(node)
            else:
                # We need children's min_sub. Since we are at a fully covered node,
                # we don't recurse. Children retain their old state.
                # We just recompute this node's min_sub.
                mid = (start + end) // 2
                left_child = 2 * node
                right_child = 2 * node + 1
                update_node(node, left_child, right_child)
            return

        mid = (start + end) // 2
        update(2 * node, start, mid, l, r, val, is_push)
        update(2 * node + 1, mid + 1, end, l, r, val, is_push)
        
        # After children are updated, update current node
        update_node(node, 2 * node, 2 * node + 1)

    # Query range: find minimum value in [l, r]
    # We pass down the max value from ancestors (ancestor_max)
    def query(node, start, end, l, r, ancestor_max):
        if l > end or r < start:
            return float('inf')
        
        current_top = get_top(node)
        current_max = max(ancestor_max, current_top)
        
        if l <= start and end <= r:
            # The minimum in this segment is max(current_max, min_sub[node])
            # because min_sub[node] stores the min of values in subtree (relative to node's stack)
            # Wait, min_sub[node] is calculated assuming node's stack top is the 'base' for children.
            # The actual value at a point is max(ancestor_max, top_on_path).
            # min_sub[node] = min_{y in node} ( max(top(node), val(y in children)) )
            # So min_{y in node} ( max(ancestor_max, top(node), val(y in children)) )
            # = max(ancestor_max, min_{y in node} ( max(top(node), val(y in children)) ))
            # = max(ancestor_max, tree_min_sub[node])
            return max(current_max, tree_min_sub[node])

        mid = (start + end) // 2
        res_left = query(2 * node, start, mid, l, r, current_max)
        res_right = query(2 * node + 1, mid + 1, end, l, r, current_max)
        
        return min(res_left, res_right)

    # Parent array
    parent = [-1] * N
    
    # Process events
    for event in events:
        x, typ, x2, y1, y2, idx = event
        
        l = y_map[y2] # bottom (smaller y value, smaller index after sorting)
        r = y_map[y1] # top (larger y value, larger index)
        
        if typ == 0: # Start event
            # Query for parent
            # The query returns the index of the rectangle that contains this one
            # (specifically the one with smallest index? No, the one that is 'active' and covers the range)
            # Since we push parents first, and parents have smaller indices?
            # Indices are 0..N-1. We need to ensure the logic holds.
            # The query returns the 'top' value. The 'top' is the last pushed rectangle covering the point.
            # Since we process Start events sorted by x2 descending (parent first), 
            # the parent is pushed first. Then children are pushed.
            # So children will be on top of parents.
            # The query returns the minimum value in the range.
            # If a child covers the whole range, its value is returned.
            # If a child covers part, and parent covers rest, min is parent.
            # This correctly identifies the immediate parent (the one that covers the whole range and is 'highest' in stack).
            # But wait, if child covers part, min is parent. This means parent is the container.
            # Is it possible that a sibling covers part? Siblings are disjoint.
            # If a sibling covers part of the Y-range, they are disjoint in Y.
            # So for the current rect to be contained, it must be fully inside the parent.
            # If it overlaps a sibling in Y, they are disjoint, so current rect cannot be inside sibling.
            # So the query correctly finds the parent.
            
            p_idx = query(1, 0, M - 1, l, r, 0)
            
            if p_idx > 0:
                # Indices in input are 0 to N-1. We used 0 for "empty".
                # We stored idx+1 in the segment tree? No, we stored idx.
                # We need to handle the 0 case (root).
                # Let's store idx + 1 in the segment tree to distinguish from 0.
                pass
        
        # Re-running logic with idx+1 storage to avoid 0 conflict
        # Adjusting the update calls:
        pass

    # Re-implementing the loop with idx+1 adjustment
    for event in events:
        x, typ, x2, y1, y2, idx = event
        l = y_map[y2]
        r = y_map[y1]
        
        if typ == 0: # Start
            # Query
            # We pass 0 as ancestor_max. The query returns max(0, min_sub).
            # If empty, returns 0.
            best = query(1, 0, M - 1, l, r, 0)
            if best == 0:
                parent[idx] = -1 # Root
            else:
                parent[idx] = best - 1 # Convert back to 0-based index
            
            # Push current rectangle (idx + 1)
            update(1, 0, M - 1, l, r, idx + 1, True)
        else: # End
            # Pop (idx + 1)
            update(1, 0, M - 1, l, r, idx + 1, False)

    # Build tree structure to count leaves
    children_count = [0] * N
    for i in range(N):
        if parent[i] != -1:
            children_count[parent[i]] += 1
            
    leaves = 0
    for i in range(N):
        if children_count[i] == 0:
            leaves += 1
            
    print(leaves)

# The logic inside the loop was slightly pseudo-code, integrating it properly in the final code block.
# One detail: `tree_min_sub` needs to be initialized correctly. 0 is correct (empty).
# `update_node` logic handles leaves.
# `query` logic handles range.

if __name__ == '__main__':
    solve()