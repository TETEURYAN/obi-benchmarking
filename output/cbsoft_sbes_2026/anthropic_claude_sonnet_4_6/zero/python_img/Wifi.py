Looking at this problem, I need to understand the wifi signal behavior:
- Signal passes through walls from inside to outside, but NOT from outside to inside
- So an antenna placed in a room covers that room AND all rooms that contain it (ancestors in the nesting hierarchy)
- But it does NOT cover rooms nested inside it (children)

The key insight: Each room needs to be covered by an antenna. An antenna placed in room R covers R and all its ancestors. So we need to cover all rooms, and the optimal strategy is to place antennas in the "leaf" rooms (rooms with no children inside them) - but wait, that's not quite right either.

Let me think again. The nesting structure forms a tree. An antenna in node R covers R and all ancestors of R. We want minimum number of antennas to cover all nodes.

This is equivalent to: minimum number of nodes such that every node is either selected or is an ancestor of a selected node. This means we need to cover all nodes, and selecting a node covers it and all its ancestors.

So we need every node to be covered. A node v is covered if v itself is selected, or some descendant of v is selected (since selecting a descendant covers v as ancestor).

Wait - selecting node R covers R and all ancestors. So node v is covered if v is selected OR some descendant of v is selected.

The uncovered nodes would be leaves that aren't selected. So we must select all leaves! But that's the maximum...

Actually: we need every node covered. Node v is covered iff v is selected OR some node in subtree(v) \ {v} is selected (a descendant). So leaves MUST be selected (they have no descendants). And if a leaf is selected, all its ancestors are automatically covered.

So the answer = number of leaf nodes in the nesting tree!

Let me verify with examples:
- Test 1: 4 rooms. The outermost contains others. Room `0 20 20 0` is root. Inside it: `5 15 15 5` and `5 19 8 17`. Inside `5 15 15 5`: `8 10 10 8`. Leaves are: `5 19 8 17` and `8 10 10 8`. Answer = 2. ✓
- Test 2: 1 room, it's a leaf. Answer = 1. ✓
- Test 3: Need to build tree and count leaves = 3. ✓

Now I need to build the nesting tree efficiently. For N up to 10^5, I need an efficient containment algorithm.

To find the direct parent of each rectangle: sort rectangles by area (descending), then for each rectangle find the smallest rectangle that contains it.

I'll use coordinate compression and sweep line, or simply: sort by area descending, and for each rect find its parent = the smallest rect containing it.

A simple approach: sort by area. For each rect (smallest first), find the smallest containing rect. Use the fact that if rect A contains rect B, then A.x1 < B.x1 (since no intersections).

I'll sort by x1 ascending (which correlates with containment - larger rects have smaller x1). Actually let me sort by area descending and use a stack-based approach on x-coordinates.

Since rectangles don't intersect and are nested, I can sort by x1 and use interval nesting logic.

```python
import sys
from sys import stdin

def solve():
    input_data = stdin.read().split()
    idx = 0
    N = int(input_data[idx]); idx += 1
    rects = []
    for i in range(N):
        x1, y1, x2, y2 = int(input_data[idx]), int(input_data[idx+1]), int(input_data[idx+2]), int(input_data[idx+3])
        idx += 4
        rects.append((x1, y1, x2, y2))
    
    # Sort by x1 ascending, then by x2 descending (larger rects first when same x1)
    rects.sort(key=lambda r: (r[0], -r[2]))
    
    # For each rect find parent: smallest rect containing it
    # Use stack: maintain stack of rects by nesting
    children_count = [0] * N
    stack = []  # stack of indices into sorted rects
    
    for i in range(N):
        x1, y1, x2, y2 = rects[i]
        # Pop stack elements that don't contain current rect
        while stack and rects[stack[-1]][2] < x2:
            stack.pop()
        if stack:
            parent = stack[-1]
            children_count[parent] += 1
        stack.append(i)
    
    leaves = sum(1 for i in range(N) if children_count[i] == 0)
    print(leaves)

solve()
```