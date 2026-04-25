Looking at this problem, I need to understand the structure:

1. Rooms are nested rectangles (like boxes within boxes)
2. WiFi signal passes from inside to outside but NOT from outside to inside
3. An antenna placed in a room covers that room AND all rooms containing it (outward), but NOT rooms inside it
4. I need minimum number of antennas to cover all rooms

Key insight: The rooms form a tree structure based on containment. The outermost rectangle is the root. Each room's parent is the smallest room that directly contains it.

An antenna placed in room R covers R and all ancestors of R (rooms containing R). So an antenna covers the path from R to the root.

This is equivalent to: given a tree, find the minimum number of root-to-node paths that cover all nodes. This is the number of leaves in the tree!

Wait, let me think again. An antenna in room R covers R and all rooms that contain R (ancestors). So it covers the path from R up to the root.

To cover all nodes with minimum number of such root-to-leaf paths, the answer is the number of leaves in the containment tree.

Let me verify with test cases:
- Test 1: 4 rooms. The outermost is `0 20 20 0`. Inside it: `5 15 15 5` and `5 19 8 17`. Inside `5 15 15 5`: `8 10 10 8`. Tree: root has 2 children (the two medium rooms), one of which has a child. Leaves are `5 19 8 17` and `8 10 10 8`. That's 2 leaves → answer 2. ✓
- Test 2: 1 room, it's both root and leaf → 1. ✓
- Test 3: Need to figure out containment. Answer is 3 leaves.

So the algorithm is:
1. Build containment tree
2. Count leaves

To build the containment tree efficiently with N up to 10^5:
- Sort rectangles by area (descending) or by x1 ascending, then find parent as the smallest containing rectangle.
- Use a sweep line or sorting approach.

A rectangle A contains rectangle B if A.x1 < B.x1 and A.x2 > B.x2 and A.y1 > B.y1 and A.y2 < B.y2 (given y1 > y2).

To find the parent of each rectangle (smallest containing rectangle), I can sort by area descending and use a stack-based approach, or sort by x1 and use interval nesting.

Since rectangles don't intersect and are properly nested, I can sort by x1 ascending (and for ties by x2 descending). Then use a stack to find the direct parent.

```python
import sys

def solve():
    data = sys.stdin.read().split()
    idx = 0
    n = int(data[idx]); idx += 1
    rects = []
    for i in range(n):
        x1, y1, x2, y2 = int(data[idx]), int(data[idx+1]), int(data[idx+2]), int(data[idx+3])
        idx += 4
        rects.append((x1, y1, x2, y2, i))
    
    # Sort by x1 ascending, then x2 descending (wider first = outer first)
    rects.sort(key=lambda r: (r[0], -r[2]))
    
    children_count = [0] * n
    parent = [-1] * n
    
    # Stack holds indices into rects array; use x2 to check containment
    stack = []
    
    for i, (x1, y1, x2, y2, orig) in enumerate(rects):
        # Pop stack elements that don't contain current rect
        while stack and rects[stack[-1]][2] < x2:
            stack.pop()
        if stack:
            par = rects[stack[-1]][4]
            parent[orig] = par
            children_count[par] += 1
        stack.append(i)
    
    # Count leaves: nodes with 0 children
    leaves = sum(1 for i in range(n) if children_count[i] == 0)
    print(leaves)

solve()
```

Let me verify test 3 gives 3 leaves with this logic, then finalize.

import sys

def solve():
    data = sys.stdin.read().split()
    idx = 0
    n = int(data[idx]); idx += 1
    rects = []
    for i in range(n):
        x1, y1, x2, y2 = int(data[idx]), int(data[idx+1]), int(data[idx+2]), int(data[idx+3])
        idx += 4
        rects.append((x1, y1, x2, y2, i))
    
    rects.sort(key=lambda r: (r[0], -r[2]))
    
    children_count = [0] * n
    
    stack = []
    
    for i, (x1, y1, x2, y2, orig) in enumerate(rects):
        while stack and rects[stack[-1]][2] < x2:
            stack.pop()
        if stack:
            par = rects[stack[-1]][4]
            children_count[par] += 1
        stack.append(i)
    
    leaves = sum(1 for i in range(n) if children_count[i] == 0)
    print(leaves)

solve()