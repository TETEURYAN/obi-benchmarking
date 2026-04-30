Looking at this problem, I need to find the minimum number of tapes to cover all land cells (#) where:
- Green tapes are horizontal
- Yellow tapes are vertical
- A cell covered by yellow tape cannot be adjacent (horizontally/vertically) to a cell covered by green tape

This means the land cells must be partitioned into two groups: those covered by green (horizontal) tapes and those covered by yellow (vertical) tapes, such that no green cell is adjacent to a yellow cell.

This is essentially a 2-coloring problem on the land cells where adjacent land cells must have the same color (both green or both yellow). So connected components of land cells (using 4-connectivity) must all be the same color.

Wait, actually adjacent land cells don't HAVE to be the same color - they just can't be different colors (green adjacent to yellow is forbidden). So adjacent land cells must be the same color. This means each connected component of land cells must be entirely green or entirely yellow.

For each connected component, we choose either green or yellow:
- If green: count the number of maximal horizontal runs of consecutive # in that component
- If yellow: count the number of maximal vertical runs of consecutive # in that component

We want to minimize the total count.

Let me verify with test 3: A 4x4 block of # (rows 2-5, cols 3-5). 
- Green: 4 rows × 1 run each = 4 tapes
- Yellow: 3 cols × 4 runs each... wait, 3 columns × 4 consecutive = 3 tapes
- Answer is 3. ✓

For each connected component, compute min(horizontal_runs, vertical_runs).

Let me implement this:

1. Find connected components using BFS/DFS
2. For each component, count horizontal runs and vertical runs
3. Sum up the minimums

```python
import sys
from collections import deque

def solve():
    input_data = sys.stdin.buffer.read().split()
    idx = 0
    N = int(input_data[idx]); idx+=1
    M = int(input_data[idx]); idx+=1
    grid = []
    for i in range(N):
        grid.append(input_data[idx].decode()); idx+=1
    
    visited = [[False]*M for _ in range(N)]
    
    total = 0
    
    for si in range(N):
        for sj in range(M):
            if grid[si][sj] == '#' and not visited[si][sj]:
                # BFS to find component
                component = []
                q = deque()
                q.append((si, sj))
                visited[si][sj] = True
                while q:
                    r, c = q.popleft()
                    component.append((r, c))
                    for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
                        nr, nc = r+dr, c+dc
                        if 0<=nr<N and 0<=nc<M and not visited[nr][nc] and grid[nr][nc]=='#':
                            visited[nr][nc] = True
                            q.append((nr, nc))
                
                # Count horizontal runs
                cells_set = set(component)
                h_runs = 0
                for (r, c) in component:
                    # start of horizontal run if left neighbor not in component
                    if (r, c-1) not in cells_set:
                        h_runs += 1
                
                # Count vertical runs
                v_runs = 0
                for (r, c) in component:
                    # start of vertical run if top neighbor not in component
                    if (r-1, c) not in cells_set:
                        v_runs += 1
                
                total += min(h_runs, v_runs)
    
    print(total)

solve()
```

Let me verify with test 1 (answer 8) and test 5 (answer 18).

Test 2: `...####.#` - two components: `####` (h=1, v=4, min=1) and `#` (h=1, v=1, min=1). Total=2. ✓

Test 3: One component, h=4, v=3, min=3. ✓

The solution looks correct.

```python
import sys
from collections import deque

def solve():
    input_data = sys.stdin.buffer.read().split()
    idx = 0
    N = int(input_data[idx]); idx+=1
    M = int(input_data[idx]); idx+=1
    grid = []
    for i in range(N):
        grid.append(input_data[idx].decode()); idx+=1
    
    visited = [[False]*M for _ in range(N)]
    total = 0
    
    for si in range(N):
        for sj in range(M):
            if grid[si][sj] == '#' and not visited[si][sj]:
                component = []
                q = deque()
                q.append((si, sj))
                visited[si][sj] = True
                while q:
                    r, c = q.popleft()
                    component.append((r, c))
                    for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
                        nr, nc = r+dr, c+dc
                        if 0<=nr<N and 0<=nc<M and not visited[nr][nc] and grid[nr][nc]=='#':
                            visited[nr][nc] = True
                            q.append((nr, nc))
                
                cells_set = set(component)
                h_runs = 0
                for (r, c) in component:
                    if (r, c-1) not in cells_set:
                        h_runs += 1
                
                v_runs = 0
                for (r, c) in component:
                    if (r-1, c) not in cells_set:
                        v_runs += 1
                
                total += min(h_runs, v_runs)
    
    print(total)

solve()
```