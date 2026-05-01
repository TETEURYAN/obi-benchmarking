import sys
from sys import stdin

def solve():
    input = stdin.read().split()
    idx = 0
    N = int(input[idx]); idx += 1
    
    rects = []
    for i in range(N):
        x1 = int(input[idx]); idx += 1
        y1 = int(input[idx]); idx += 1
        x2 = int(input[idx]); idx += 1
        y2 = int(input[idx]); idx += 1
        rects.append((x1, y1, x2, y2))
    
    # We need to find the nesting structure of rectangles
    # Rectangle A contains rectangle B if A's bounds contain B's bounds
    # The signal goes from inside to outside, so an antenna inside room B
    # covers B and all rooms that contain B (ancestors)
    # But signal doesn't go from outside to inside
    
    # So each room needs to be covered by an antenna that is either:
    # - inside that room (directly), or
    # - inside a room that is nested inside that room (descendant)
    
    # An antenna placed at depth d covers all rooms at depth <= d that contain it
    # i.e., it covers its room and all ancestor rooms
    
    # We need minimum number of antennas to cover all rooms
    # A room is "covered" if there's an antenna in it or in any of its descendants
    
    # This is equivalent to: we need to cover all LEAF nodes in the nesting tree
    # Because if all leaves are covered, their ancestors are also covered
    # (since signal goes from inside to outside)
    
    # Wait, but a leaf room has no descendants, so we need an antenna inside it
    # A non-leaf room is covered if any descendant has an antenna
    
    # So minimum antennas = number of leaf rooms in the containment tree
    
    # Build containment tree
    # For each rectangle, find its direct parent (smallest rectangle that contains it)
    
    # Sort rectangles by area (descending) - larger rectangles are potential parents
    # For each rectangle, find the smallest rectangle that strictly contains it
    
    # With N up to 1e5, we need an efficient approach
    # 
    # Key insight: sort by x1 (left boundary). Use a stack-based approach.
    # Actually, since rectangles don't intersect and are nested like boxes,
    # we can sort by area and use containment checks.
    
    # Sort by area descending (larger first = potential ancestors)
    def area(r):
        return (r[2] - r[0]) * (r[1] - r[3])
    
    rects_sorted = sorted(range(N), key=lambda i: -area(rects[i]))
    
    # For each rect, find parent = smallest containing rect
    # Use sorted order: for rect i (in sorted order), its parent is the most recently
    # seen rect that contains it
    
    # Build parent array using a stack
    # Sort by x1, then for same x1 by x2 descending (larger first)
    # Actually let's sort by x1 asc, y1 desc (top-left corner)
    
    # Simpler: sort by area desc, then for each rect find parent using a stack
    # Since rects are non-intersecting and nested, we can use coordinate sorting
    
    children_count = [0] * N
    
    # Sort indices by area descending
    order = sorted(range(N), key=lambda i: -area(rects[i]))
    
    # Use a stack to find parent
    # Stack contains indices in order of nesting
    stack = []
    parent = [-1] * N
    
    for idx_i in order:
        x1, y1, x2, y2 = rects[idx_i]
        # Pop stack elements that don't contain current rect
        while stack:
            top = stack[-1]
            tx1, ty1, tx2, ty2 = rects[top]
            if tx1 <= x1 and ty1 >= y1 and tx2 >= x2 and ty2 <= y2:
                # top contains current
                parent[idx_i] = top
                children_count[top] += 1
                break
            else:
                stack.pop()
        stack.append(idx_i)
    
    # Count leaves (nodes with no children)
    leaves = sum(1 for i in range(N) if children_count[i] == 0)
    
    print(leaves)

solve()