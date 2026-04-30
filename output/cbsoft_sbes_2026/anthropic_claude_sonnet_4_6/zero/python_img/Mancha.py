Looking at this problem, I need to determine if a "mancha" (stain) is regular, meaning for every pair of pixels P and Q in the stain, d(P,Q) = dmanhattan(P,Q).

Key insight: d(P,Q) = dmanhattan(P,Q) means the shortest path within the stain equals the Manhattan distance. This means there's always a "monotone" path between any two pixels - you never need to go "backwards" in either dimension.

This is equivalent to saying: the stain has no "holes" or "detours" - specifically, for any two pixels P and Q, there exists a path that only moves in the directions that reduce Manhattan distance (i.e., moves that go toward Q).

A cleaner characterization: The stain is regular if and only if it is "HV-convex" and "orthoconvex" - meaning:
1. Every row segment is contiguous (no gaps in any row)
2. Every column segment is contiguous (no gaps in any column)
3. The stain is "connected" in a way that allows monotone paths

Actually, the condition d(P,Q) = dmanhattan(P,Q) for all pairs is equivalent to: the stain is an **HV-convex polyomino** that is also **connected** (which it is by assumption). HV-convex means each row and each column intersection with the stain is a contiguous segment (possibly empty).

Wait, but that's not sufficient. We also need "orthoconvex" - that the stain is connected via monotone paths. The correct characterization is: the stain is regular iff it is HV-convex (rows and columns are contiguous intervals).

Let me verify with the examples:
- Left figure (regular): rows and columns should be contiguous
- Middle figure (irregular): has gaps
- Right figure (irregular): has a hole

So the condition is: for every row, the '*' pixels form a contiguous segment; and for every column, the '*' pixels form a contiguous segment.

Let me verify with test 3: `.*` and `**` - row 0: col 1; row 1: cols 0,1. Column 0: row 1; column 1: rows 0,1. All contiguous. Output S. ✓

But wait - is HV-convexity sufficient? Consider an HV-convex shape that looks like a "Z" - rows are contiguous, columns are contiguous, but you might need detours. Actually for HV-convex connected polyominoes, it's been shown that monotone paths always exist between any two cells if the shape is also "row-convex" and "column-convex" AND connected. But connectivity + HV-convex might not be enough...

Actually thinking more carefully: if rows and columns are all contiguous intervals, then for any P=(r1,c1) and Q=(r2,c2), we can try to go row by row. The key property needed is that consecutive rows' intervals overlap, ensuring we can move between them. But even if they don't overlap horizontally, we might need detours.

Let me just implement the HV-convex check and see if it passes the test cases. If the stain is HV-convex (each row and column has contiguous pixels), then d(P,Q) = dmanhattan(P,Q).

```python
import sys
from collections import deque

def solve():
    input_data = sys.stdin.read().split()
    n = int(input_data[0])
    grid = []
    for i in range(1, n+1):
        grid.append(input_data[i])
    
    # Check HV-convexity: each row and column has contiguous '*' pixels
    for i in range(n):
        row = grid[i]
        first = -1
        last = -1
        for j in range(n):
            if row[j] == '*':
                if first == -1:
                    first = j
                last = j
        if first != -1:
            for j in range(first, last+1):
                if row[j] != '*':
                    print("N")
                    return
    
    for j in range(n):
        first = -1
        last = -1
        for i in range(n):
            if grid[i][j] == '*':
                if first == -1:
                    first = i
                last = i
        if first != -1:
            for i in range(first, last+1):
                if grid[i][j] != '*':
                    print("N")
                    return
    
    print("S")

solve()
```