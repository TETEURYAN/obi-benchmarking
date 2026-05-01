Looking at this problem, I need to find the minimum number of tapes (green horizontal, yellow vertical) to cover all land cells, where:
- All land cells must be covered
- All sea cells must be uncovered
- Green tapes are horizontal, yellow tapes are vertical
- A yellow-covered cell cannot be adjacent (horizontally/vertically) to a green-covered cell

This means the green region and yellow region must be separated - no green cell can be adjacent to a yellow cell. So the land cells must be partitioned into two sets: G (green) and Y (yellow), where no cell in G is adjacent to a cell in Y.

This means G and Y form independent components with no adjacency between them. In other words, each connected component of land cells must be entirely green or entirely yellow.

Wait, but within a connected component, if some cells are green and some yellow, they'd be adjacent. So each connected component must be monochromatic.

For a connected component colored green: minimum tapes = number of maximal horizontal runs of land cells within that component.
For a connected component colored yellow: minimum tapes = number of maximal vertical runs of land cells within that component.

We want to minimize total tapes, so for each connected component, we choose min(horizontal_runs, vertical_runs).

Let me verify with test cases:

Test 3: 4x3 block of '#' at rows 1-4, cols 2-4 (0-indexed).
- Horizontal runs: 4 rows × 1 run each = 4
- Vertical runs: 3 cols × 1 run each = 3
- Min = 3 ✓

Test 2: `...####.#` - two components: `####` and `#`
- `####`: horiz=1, vert=4, min=1
- `#`: horiz=1, vert=1, min=1
- Total=2 ✓

Test 1: Need to check connected components and their runs.

Let me implement this:

```python
import sys
from collections import deque

def solve():
    input_data = sys.stdin.read().split()
    idx = 0
    N = int(input_data[idx]); idx+=1
    M = int(input_data[idx]); idx+=1
    grid = []
    for i in range(N):
        grid.append(input_data[idx]); idx+=1
    
    visited = [[False]*M for _ in range(N)]
    total = 0
    
    for si in range(N):
        for sj in range(M):
            if grid[si][sj] == '#' and not visited[si][sj]:
                # BFS to find component
                cells = []
                q = deque()
                q.append((si, sj))
                visited[si][sj] = True
                while q:
                    r, c = q.popleft()
                    cells.append((r, c))
                    for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
                        nr, nc = r+dr, c+dc
                        if 0<=nr<N and 0<=nc<M and not visited[nr][nc] and grid[nr][nc]=='#':
                            visited[nr][nc] = True
                            q.append((nr, nc))
                
                cell_set = set(cells)
                
                # Count horizontal runs
                # Group by row
                from collections import defaultdict
                rows = defaultdict(list)
                cols = defaultdict(list)
                for r, c in cells:
                    rows[r].append(c)
                    cols[c].append(r)
                
                h_runs = 0
                for r, cs in rows.items():
                    cs_sorted = sorted(cs)
                    runs = 1
                    for k in range(1, len(cs_sorted)):
                        if cs_sorted[k] != cs_sorted[k-1]+1:
                            runs += 1
                    h_runs += runs
                
                v_runs = 0
                for c, rs in cols.items():
                    rs_sorted = sorted(rs)
                    runs = 1
                    for k in range(1, len(rs_sorted)):
                        if rs_sorted[k] != rs_sorted[k-1]+1:
                            runs += 1
                    v_runs += runs
                
                total += min(h_runs, v_runs)
    
    print(total)

solve()
```

Let me verify test 5 mentally... it should give 18. The logic seems correct. Let me finalize:

import sys
from collections import deque, defaultdict

def solve():
    data = sys.stdin.buffer.read().split()
    idx = 0
    N = int(data[idx]); idx+=1
    M = int(data[idx]); idx+=1
    grid = []
    for i in range(N):
        grid.append(data[idx].decode()); idx+=1
    
    visited = [[False]*M for _ in range(N)]
    total = 0
    
    for si in range(N):
        for sj in range(M):
            if grid[si][sj] == '#' and not visited[si][sj]:
                cells = []
                q = deque([(si, sj)])
                visited[si][sj] = True
                while q:
                    r, c = q.popleft()
                    cells.append((r, c))
                    for dr, dc in ((-1,0),(1,0),(0,-1),(0,1)):
                        nr, nc = r+dr, c+dc
                        if 0<=nr<N and 0<=nc<M and not visited[nr][nc] and grid[nr][nc]=='#':
                            visited[nr][nc] = True
                            q.append((nr, nc))
                rows = defaultdict(list)
                cols = defaultdict(list)
                for r, c in cells:
                    rows[r].append(c)
                    cols[c].append(r)
                h_runs = 0
                for r, cs in rows.items():
                    cs.sort()
                    runs = 1
                    for k in range(1, len(cs)):
                        if cs[k] != cs[k-1]+1:
                            runs += 1
                    h_runs += runs
                v_runs = 0
                for c, rs in cols.items():
                    rs.sort()
                    runs = 1
                    for k in range(1, len(rs)):
                        if rs[k] != rs[k-1]+1:
                            runs += 1
                    v_runs += runs
                total += min(h_runs, v_runs)
    print(total)

solve()