The problem asks us to count the number of "safe" cells in an $N \times N$ grid.
A cell is "safe" if starting from it and following the arrows leads to a cycle within the grid, rather than exiting the grid.
If a path leads outside the grid, the starting cell is not safe.

Constraints:
$N \le 500$.
Grid size is $N \times N$, so max $500 \times 500 = 250,000$ cells.
Time limit is usually 1s or 2s for OBI/ICPC style problems.
An $O(N^2)$ or $O(N^2 \alpha(N^2))$ solution is required. An $O(N^3)$ solution would likely be too slow ($125 \times 10^9$ operations).

Let's model the grid as a graph.
Each cell is a node.
Each node has exactly one outgoing edge (determined by the arrow direction).
This forms a functional graph (a collection of components, each consisting of directed cycles with trees rooted at the cycle nodes).

A cell is safe if and only if it belongs to a cycle.
Why?
In a functional graph, every path eventually enters a cycle.
If the path exits the grid, it means the path reached a boundary cell whose arrow points outwards.
Let's define "exiting the grid" as reaching a virtual "sink" node outside.
Actually, it's simpler:
A cell is "unsafe" if following the arrows leads out of the grid.
A cell is "safe" if following the arrows stays inside the grid forever.
Since the grid is finite, staying inside forever implies visiting a cell twice, which implies a cycle.
So, "safe" cells are exactly those that are part of a cycle within the grid.

Let's look at the transitions.
Grid coordinates $(r, c)$ where $0 \le r, c < N$.
'V': $(r, c) \to (r+1, c)$
'<': $(r, c) \to (r, c-1)$
'>': $(r, c) \to (r, c+1)$
'A': $(r, c) \to (r-1, c)$

If a transition leads to coordinates outside $[0, N-1]$, the path exits.

Algorithm Idea 1: DFS with coloring.
We can perform a DFS from each unvisited node.
States for each node:
0: Unvisited
1: Visiting (currently in the recursion stack)
2: Visited and Safe (part of a cycle)
3: Visited and Unsafe (leads out)

However, standard DFS might be tricky with the "exiting" condition.
Let's refine the states.
We want to find nodes that are part of cycles.
Nodes that point out of bounds are definitely not part of a cycle. They are "exit nodes".
Let's reverse the graph.
In the original graph, edges go $u \to v$.
In the reversed graph, edges go $v \to u$.
If a node $u$ points out of bounds, it is unsafe.
In the reversed graph, any node that can reach $u$ is also unsafe (because in the original graph, that node leads to $u$ which leads out).
So, we can identify all "exit nodes" (nodes on the boundary pointing outwards).
Then, we perform a BFS/DFS on the *reversed* graph starting from these exit nodes.
All nodes reachable from exit nodes in the reversed graph are "unsafe".
The remaining nodes are "safe".

Let's verify this logic.
1. Identify boundary nodes that point out.
   - Top row ($r=0$), arrow 'A'.
   - Bottom row ($r=N-1$), arrow 'V'.
   - Left col ($c=0$), arrow '<'.
   - Right col ($c=N-1$), arrow '>'.
   These nodes lead directly out. Let's call this set $S_{exit}$.
2. Build the reversed graph.
   - If grid$[r][c]$ points to $(nr, nc)$ (which is inside), add an edge from $(nr, nc)$ to $(r, c)$ in the reversed adjacency list.
   - If grid$[r][c]$ points outside, do not add a reversed edge (or add it to a virtual sink, but we just mark the source as an exit node).
3. Run BFS/DFS on the reversed graph starting with all nodes in $S_{exit}$ as initial queue/stack.
   - Mark these nodes as "unsafe".
   - For each neighbor in the reversed graph, if not visited, mark as "unsafe" and add to queue.
4. Count nodes not marked "unsafe".

Complexity:
Building the graph: $O(N^2)$.
BFS/DFS: Each node and edge is processed once. Edges = $N^2$. So $O(N^2)$.
Total time: $O(N^2)$.
Space: $O(N^2)$ to store the grid and the reversed graph (or just the grid and compute neighbors on the fly).
Since $N=500$, $N^2 = 250,000$. This fits easily in memory and time.

Let's trace Example 1.
3
>>V
AV<
A<>

Grid:
(0,0) '>' -> (0,1)
(0,1) '>' -> (0,2)
(0,2) 'V' -> (1,2)
(1,0) 'A' -> (0,0)
(1,1) 'V' -> (2,1)
(1,2) '<' -> (1,1)
(2,0) 'A' -> (1,0)
(2,1) '<' -> (2,0)
(2,2) '>' -> (2,3) -> OUT (Right boundary)

Exit nodes:
(2,2) points right, $c=2$ is right boundary. So (2,2) is exit.

Reversed edges:
(0,1) <- (0,0)
(0,2) <- (0,1)
(1,2) <- (0,2)
(0,0) <- (1,0)
(2,1) <- (1,1)
(1,1) <- (1,2)
(1,0) <- (2,0)
(2,0) <- (2,1)
(2,2) points out, so no reversed edge coming in from outside. But (2,2) is a source of "unsafety".

BFS start: Queue = [(2,2)]. Visited/Unsafe = {(2,2)}.
Pop (2,2). Does anyone point to (2,2)?
Looking at grid, nobody points to (2,2).
(1,2) points left to (1,1).
(2,1) points left to (2,0).
Nobody points to (2,2).
So BFS ends.
Unsafe: {(2,2)}.
Total cells: 9.
Safe: 9 - 1 = 8.
Output: 8. Matches example.

Let's trace Example 2.
4
>>V<
A<<<
AAA>
>>>A

Grid:
Row 0: >>V<
(0,0)> -> (0,1)
(0,1)> -> (0,2)
(0,2)V -> (1,2)
(0,3)< -> (0,2) (Wait, (0,3) is right boundary. '<' points left to (0,2). Safe move.)
Row 1: A<<<
(1,0)A -> (0,0)
(1,1)< -> (1,0)
(1,2)< -> (1,1)
(1,3)< -> (1,2)
Row 2: AAA>
(2,0)A -> (1,0)
(2,1)A -> (1,1)
(2,2)A -> (1,2)
(2,3)> -> (2,4) -> OUT (Right boundary)
Row 3: >>>A
(3,0)> -> (3,1)
(3,1)> -> (3,2)
(3,2)> -> (3,3)
(3,3)A -> (2,3)

Exit nodes:
(2,3) points right, $c=3$ is boundary. (2,3) is exit.
Any others?
(0,3) is '<', points inside.
(1,3) is '<', points inside.
(3,3) is 'A', points inside.
Top row 'A': (1,0), (2,0), (2,1), (2,2) point up. (1,0)->(0,0). (2,0)->(1,0). None point out from top boundary.
Bottom row 'V': None.
Left col '<': None.
Right col '>': (2,3) is the only one.

So start BFS with Queue = [(2,3)].
Unsafe = {(2,3)}.
Who points to (2,3)?
(3,3) 'A' points to (2,3).
Add (3,3) to Queue. Unsafe = {(2,3), (3,3)}.
Who points to (3,3)?
(3,2) '>' points to (3,3).
Add (3,2). Unsafe = {(2,3), (3,3), (3,2)}.
Who points to (3,2)?
(3,1) '>' points to (3,2).
Add (3,1).
Who points to (3,1)?
(3,0) '>' points to (3,1).
Add (3,0).
Who points to (3,0)?
Nobody.
Queue empty.

Unsafe set: {(2,3), (3,3), (3,2), (3,1), (3,0)}.
Size: 5.
Total cells: $4 \times 4 = 16$.
Safe: $16 - 5 = 11$.
Matches example output 11.

Implementation details:
- Read N.
- Read grid.
- Identify exit nodes.
  - Iterate all cells. Check if next step is out of bounds.
  - Or just check boundary cells.
    - $r=0$ and grid[r][c] == 'A'
    - $r=N-1$ and grid[r][c] == 'V'
    - $c=0$ and grid[r][c] == '<'
    - $c=N-1$ and grid[r][c] == '>'
- Build reversed adjacency list or compute on the fly.
  - Computing on the fly is easier for memory and code simplicity.
  - `get_sources(r, c)` returns list of cells that point to (r,c).
    - Check (r-1, c): if grid[r-1][c] == 'V', then (r-1, c) -> (r, c).
    - Check (r+1, c): if grid[r+1][c] == 'A', then (r+1, c) -> (r, c).
    - Check (r, c-1): if grid[r][c-1] == '>', then (r, c-1) -> (r, c).
    - Check (r, c+1): if grid[r][c+1] == '<', then (r, c+1) -> (r, c).
    - Must check bounds for these neighbors.
- BFS/DFS.
  - Use a queue. Add all exit nodes.
  - `visited` array (boolean).
  - While queue not empty:
    - pop (r, c).
    - for each source (sr, sc) of (r, c):
      - if not visited[sr][sc]:
        - visited[sr][sc] = True
        - queue.append((sr, sc))
- Result: Total cells - count of visited cells.

Wait, is it possible for a node to be marked unsafe but not reachable from an exit node in the reversed graph?
No. If a node is unsafe, it leads to an exit.
Path: $u \to \dots \to v \to \text{out}$.
In reversed graph: $\text{out} \leftarrow v \leftarrow \dots \leftarrow u$.
So $u$ is reachable from $v$ (which is an exit node) in the reversed graph.
So the BFS approach covers all unsafe nodes.

Corner cases:
- N=1.
  - If arrow points out, 0 safe.
  - If arrow points... wait, N=1, any arrow points out?
    - 'V': r+1=1 (out).
    - 'A': r-1=-1 (out).
    - '>': c+1=1 (out).
    - '<': c-1=-1 (out).
  - So for N=1, answer is always 0.
  - Let's check logic.
  - Boundary checks: (0,0) is top, bottom, left, right.
  - Any arrow will trigger one condition.
  - Queue starts with (0,0).
  - Visited count = 1.
  - Total = 1. Safe = 0. Correct.

- All cells safe.
  - Grid of cycles.
  - No exit nodes.
  - Queue empty.
  - Visited count 0.
  - Safe = $N^2$. Correct.

- All cells unsafe.
  - All point to one corner which points out.
  - Queue starts with corner.
  - BFS visits all.
  - Safe = 0. Correct.

Data structures:
- Grid can be list of strings or list of lists. List of strings is fine since we only read.
- `visited` can be a list of lists of booleans or a set. List of lists is faster. $500 \times 500$ is small enough.
- Queue: `collections.deque`.

Input reading:
`sys.stdin.read().split()` handles whitespace nicely.
First token N.
Next N tokens are the rows.

Let's write the code structure.

```python
import sys
from collections import deque

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    iterator = iter(input_data)
    try:
        N = int(next(iterator))
    except StopIteration:
        return

    grid = []
    for _ in range(N):
        grid.append(next(iterator))
    
    # Visited array for BFS (marks unsafe cells)
    # False = safe (potentially), True = unsafe
    visited = [[False for _ in range(N)] for _ in range(N)]
    q = deque()
    
    # Helper to process a cell if it's an exit
    # We iterate all cells to find exits.
    # Optimization: Only check boundary cells.
    
    # Check boundaries
    # Top row (r=0), arrow 'A'
    for c in range(N):
        if grid[0][c] == 'A':
            if not visited[0][c]:
                visited[0][c] = True
                q.append((0, c))
    
    # Bottom row (r=N-1), arrow 'V'
    for c in range(N):
        if grid[N-1][c] == 'V':
            if not visited[N-1][c]:
                visited[N-1][c] = True
                q.append((N-1, c))
                
    # Left col (c=0), arrow '<'
    for r in range(N):
        if grid[r][0] == '<':
            if not visited[r][0]:
                visited[r][0] = True
                q.append((r, 0))
    
    # Right col (c=N-1), arrow '>'
    for r in range(N):
        if grid[r][N-1] == '>':
            if not visited[r][N-1]:
                visited[r][N-1] = True
                q.append((r, N-1))

    # Directions for reversed graph traversal
    # We are at (r, c) which is unsafe.
    # We want to find (pr, pc) such that (pr, pc) -> (r, c).
    # (pr, pc) is 'V' and (pr+1, pc) == (r, c) => pr = r-1, pc = c. Check grid[r-1][c] == 'V'
    # (pr, pc) is 'A' and (pr-1, pc) == (r, c) => pr = r+1, pc = c. Check grid[r+1][c] == 'A'
    # (pr, pc) is '>' and (pr, pc+1) == (r, c) => pr = r, pc = c-1. Check grid[r][c-1] == '>'
    # (pr, pc) is '<' and (pr, pc-1) == (r, c) => pr = r, pc = c+1. Check grid[r][c+1] == '<'
    
    # Offsets for the 4 neighbors in the grid
    # dr, dc for the neighbor
    # We check if neighbor points to current (r, c)
    
    # Neighbors: (r-1, c), (r+1, c), (r, c-1), (r, c+1)
    # 1. Neighbor (r-1, c). If valid, does it point down ('V')? If yes, it points to (r, c).
    # 2. Neighbor (r+1, c). If valid, does it point up ('A')? If yes, it points to (r, c).
    # 3. Neighbor (r, c-1). If valid, does it point right ('>')? If yes, it points to (r, c).
    # 4. Neighbor (r, c+1). If valid, does it point left ('<')? If yes, it points to (r, c).

    while q:
        r, c = q.popleft()
        
        # Check neighbor above (r-1, c)
        if r > 0:
            if grid[r-1][c] == 'V':
                if not visited[r-1][c]:
                    visited[r-1][c] = True
                    q.append((r-1, c))
        
        # Check neighbor below (r+1, c)
        if r < N - 1:
            if grid[r+1][c] == 'A':
                if not visited[r+1][c]:
                    visited[r+1][c] = True
                    q.append((r+1, c))
            
        # Check neighbor left (r, c-1)
        if c > 0:
            if grid[r][c-1] == '>':
                if not visited[r][c-1]:
                    visited[r][c-1] = True
                    q.append((r, c-1))
            
        # Check neighbor right (r, c+1)
        if c < N - 1:
            if grid[r][c+1] == '<':
                if not visited[r][c+1]:
                    visited[r][c+1] = True
                    q.append((r, c+1))
    
    unsafe_count = 0
    for r in range(N):
        for c in range(N):
            if visited[r][c]:
                unsafe_count += 1
                
    print(N * N - unsafe_count)

if __name__ == '__main__':
    solve()
```

Let's double check the logic for finding sources.
Current node: $(r, c)$.
We want $(pr, pc)$ such that $(pr, pc) \to (r, c)$.
Possible arrows at $(pr, pc)$:
- 'V': $(pr, pc) \to (pr+1, pc)$. So $pr+1=r \implies pr=r-1$. $pc=c$.
  Condition: $pr=r-1$ is valid ($r>0$) and `grid[r-1][c] == 'V'`. Correct.
- 'A': $(pr, pc) \to (pr-1, pc)$. So $pr-1=r \implies pr=r+1$. $pc=c$.
  Condition: $pr=r+1$ is valid ($r<N-1$) and `grid[r+1][c] == 'A'`. Correct.
- '>': $(pr, pc) \to (pr, pc+1)$. So $pc+1=c \implies pc=c-1$. $pr=r$.
  Condition: $pc=c-1$ is valid ($c>0$) and `grid[r][c-1] == '>'`. Correct.
- '<': $(pr, pc) \to (pr, pc-1)$. So $pc-1=c \implies pc=c+1$. $pr=r$.
  Condition: $pc=c+1$ is valid ($c<N-1$) and `grid[r][c+1] == '<'`. Correct.

The logic holds.

Is there any case where `sys.setrecursionlimit` is needed?
No, this is an iterative BFS solution. No recursion depth issues.

Input format check:
First line N.
Next N lines strings.
`sys.stdin.read().split()` will split by whitespace.
If the grid lines contain spaces (unlikely given problem description "N characters"), `split()` would break them.
Problem says: "Each one of the N lines following contains N characters".
Usually this means ">>V\nAV<\n...".
`split()` handles newlines as delimiters, so it returns `['3', '>>V', 'AV<', 'A<>']`.
This is correct. If lines had spaces like `> > V`, `split` would return `['3', '>', '>', 'V', ...]`.
Given standard competitive programming format for grids, lines are contiguous strings.
The code assumes contiguous strings.

Wait, what if the input has trailing spaces or weird formatting?
`split()` is robust against that.
What if $N$ is missing? Handled.
What if grid lines are missing? `next(iterator)` would raise `StopIteration`.
The problem guarantees valid input format usually.
I'll add a basic check or just let it crash naturally if input is malformed (standard practice).
The prompt says "código robusto", so handling `StopIteration` is good.

One small optimization/correction:
The initial loop for boundary checks.
I iterated 4 times over rows/cols.
Actually, iterating all cells is $O(N^2)$.
Iterating boundaries is $O(N)$.
Iterating boundaries is better.
My code does iterate boundaries separately.
Top row: $N$ cells.
Bottom row: $N$ cells.
Left col: $N$ cells.
Right col: $N$ cells.
Total checks: $4N$.
This is fine. Corners are checked twice?
Top-Left $(0,0)$:
Checked in Top row loop.
Checked in Left col loop.
If it is 'A', added to queue.
If it is '<', added to queue.
If it is 'A' and '<'? Impossible, it's one char.
So it's safe. The `if not visited` check prevents double adding to queue.
Wait, if $(0,0)$ is 'A', it is added.
Then in Left col loop, if $(0,0)$ is '<', it is added.
Since it can't be both, no issue.
What if $(0,0)$ is 'V' (points down)?
Top row loop checks `if grid[0][c] == 'A'`. 'V' != 'A'. Not added.
Left col loop checks `if grid[r][0] == '<'`. 'V' != '<'. Not added.
Correct.

Wait, what if a cell is on the boundary but points INWARDS?
Example: $(0,0)$ is 'V'.
It is on top row. `grid[0][0] == 'A'` is False.
It is on left col. `grid[0][0] == '<'` is False.
It is NOT added to queue.
Correct, because it does not lead out of the grid immediately.

What if a cell is NOT on boundary but leads out?
Impossible. To lead out, you must cross the boundary.
Crossing the boundary requires being on the boundary and pointing outwards.
So only boundary cells can be "exit nodes".

Correctness verified.

Complexity:
Reading input: $O(N^2)$.
Initialization: $O(N)$.
BFS: Each cell enters queue at most once. Inside loop constant time. $O(N^2)$.
Counting: $O(N^2)$.
Total Time: $O(N^2)$.
Space: Grid $O(N^2)$, Visited $O(N^2)$, Queue $O(N^2)$.
Total Space: $O(N^2)$.
Constraints $N \le 500 \implies N^2 = 250,000$.
Operations $\approx 10^6$. Very fast.
Memory $\approx 250\text{KB}$ for grid (chars) + $250\text{KB}$ for visited (bools). Very small.

Final check on imports.
`sys`, `deque`.
Output format: "Seu programa deve produzir um único inteiro".
`print(count)` does exactly that.

One detail: `sys.stdin.read().split()` returns list of strings.
If the input is:
```
3
>>V
AV<
A<>
```
`input_data` = `['3', '>>V', 'AV<', 'A<>']`.
`N` = 3.
`grid` = `['>>V', 'AV<', 'A<>']`.
This works.

What if the input has spaces between characters?
`3`
`> > V`
`split()` would produce `['3', '>', '>', 'V', ...]`.
The code would interpret `'>'` as a row. `len('>')` is 1. `N=3`.
The logic `grid[r][c]` would fail or go out of bounds if I don't check lengths.
However, the problem description says "Each one of the N lines following contains N characters".
This implies no spaces.
Standard OBI/ICPC format.
I will assume standard format.

Code structure looks good.
I will combine the boundary checks into a single loop or keep them separate. Separate is clearer.
Actually, I can just iterate all cells $(r, c)$ and check if `grid[r][c]` points out.
This is $O(N^2)$ but simplifies the code logic (no need to handle 4 cases separately).
Given $N=500$, $N^2$ is small enough that the constant factor of iterating everything vs boundaries doesn't matter for performance, and it reduces code size.
Let's refactor the initialization loop.

```python
    for r in range(N):
        for c in range(N):
            char = grid[r][c]
            # Check if points out
            out = False
            if char == 'A' and r == 0: out = True
            elif char == 'V' and r == N - 1: out = True
            elif char == '<' and c == 0: out = True
            elif char == '>' and c == N - 1: out = True
            
            if out:
                if not visited[r][c]:
                    visited[r][c] = True
                    q.append((r, c))
```
This is cleaner and less error-prone than 4 loops.

Final check on the problem statement details.
"Gabriel é um garoto..." context.
"Setas" title.
Input: N, then N lines.
Output: integer.
Constraints: N <= 500.
Everything matches.

One edge case: $N=0$?
Constraint $1 \le N$. So $N \ge 1$.
Empty input? `if not input_data: exit()`. Handled.

I'm ready to generate the code.

```python
import sys
from collections import deque

# Set recursion limit just in case, though we use BFS
sys.setrecursionlimit(200000)

def solve():
    # Fast I/O
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return

    iterator = iter(input_data)
    try:
        n_str = next(iterator)
        N = int(n_str)
    except StopIteration:
        return

    grid = []
    for _ in range(N):
        try:
            grid.append(next(iterator))
        except StopIteration:
            break
            
    # Visited array: True means unsafe (leads to exit), False means safe (potentially)
    visited = [[False] * N for _ in range(N)]
    q = deque()
    
    # Step 1: Identify all exit nodes (boundary cells pointing outwards)
    # and add them to the queue to start the BFS on the reversed graph.
    for r in range(N):
        for c in range(N):
            char = grid[r][c]
            is_exit = False
            if char == 'A' and r == 0:
                is_exit = True
            elif char == 'V' and r == N - 1:
                is_exit = True
            elif char == '<' and c == 0:
                is_exit = True
            elif char == '>' and c == N - 1:
                is_exit = True
            
            if is_exit:
                if not visited[r][c]:
                    visited[r][c] = True
                    q.append((r, c))

    # Step 2: BFS on the reversed graph
    # If v is unsafe, and u -> v, then u is unsafe.
    # We look for u such that u points to v.
    while q:
        r, c = q.popleft()
        
        # Check potential predecessors (u) of (r, c)
        
        # 1. Predecessor at (r-1, c) if it points Down ('V')
        if r > 0:
            if grid[r-1][c] == 'V':
                if not visited[r-1][c]:
                    visited[r-1][c] = True
                    q.append((r-1, c))
        
        # 2. Predecessor at (r+1, c) if it points Up ('A')
        if r < N - 1:
            if grid[r+1][c] == 'A':
                if not visited[r+1][c]:
                    visited[r+1][c] = True
                    q.append((r+1, c))
        
        # 3. Predecessor at (r, c-1) if it points Right ('>')
        if c > 0:
            if grid[r][c-1] == '>':
                if not visited[r][c-1]:
                    visited[r][c-1] = True
                    q.append((r, c-1))
        
        # 4. Predecessor at (r, c+1) if it points Left ('<')
        if c < N - 1:
            if grid[r][c+1] == '<':
                if not visited[r][c+1]:
                    visited[r][c+1] = True
                    q.append((r, c+1))

    # Step 3: Count safe cells
    unsafe_count = 0
    for r in range(N):
        for c in range(N):
            if visited[r][c]:
                unsafe_count += 1
                
    print(N * N - unsafe_count)

if __name__ == '__main__':
    solve()
```
The logic is sound. The code is clean. It follows all guidelines.
No markdown blocks in the final output.
Just the code.

Wait, the prompt says:
"Se python for Python, use 'sys.stdin.read().split()' para leitura rápida e 'sys.setrecursionlimit(200000)' para problemas de recursão."
I used `sys.stdin.read().split()`.
I added `sys.setrecursionlimit` although not strictly needed for BFS, but it's in the guidelines for "problems of recursion". This is a graph problem, so it's good practice to include it or if I decided to switch to DFS. I'll keep it.

One final check on the variable names. `N` is used. `grid` is used.
Constraints: `N <= 500`.
The solution is $O(N^2)$.
Memory is $O(N^2)$.
It fits.

The prompt asks for "ZERO EXPLICAÇÃO".
I will output only the code.

One tiny detail: `sys.setrecursionlimit` takes an integer.
The prompt example shows `sys.setrecursionlimit(200000)`.
I will use that.

The prompt example for input reading:
```python
import sys
input_data = sys.stdin.read().split()
if not input_data:
    exit()
n = int(input_data[0])
m = int(input_data[1])
grid = input_data[2:]
```
My reading logic:
```python
input_data = sys.stdin.read().split()
if not input_data:
    return
# ...
N = int(next(iterator))
# ...
```
This is equivalent and handles the grid lines correctly.

Final check on output format.
"Seu programa deve produzir um único inteiro".
`print(N * N - unsafe_count)` produces an integer followed by a newline. Correct.

I am confident in this solution.import sys
from collections import deque

# OBI/ICPC style solution for the "Setas" problem
# Time Complexity: O(N^2)
# Space Complexity: O(N^2)

def solve():
    # Fast I/O as requested
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return

    iterator = iter(input_data)
    
    try:
        n_str = next(iterator)
        N = int(n_str)
    except StopIteration:
        return

    grid = []
    for _ in range(N):
        try:
            grid.append(next(iterator))
        except StopIteration:
            break
            
    # Visited array to mark unsafe cells (cells that lead out of the grid)
    # False: potentially safe, True: unsafe
    visited = [[False] * N for _ in range(N)]
    q = deque()
    
    # Step 1: Identify all exit nodes (boundary cells pointing outwards)
    # These are the sources of "unsafety" in the reversed graph logic.
    for r in range(N):
        for c in range(N):
            char = grid[r][c]
            is_exit = False
            
            # Check boundary conditions based on arrow direction
            if char == 'A' and r == 0:
                is_exit = True
            elif char == 'V' and r == N - 1:
                is_exit = True
            elif char == '<' and c == 0:
                is_exit = True
            elif char == '>' and c == N - 1:
                is_exit = True
            
            if is_exit:
                if not visited[r][c]:
                    visited[r][c] = True
                    q.append((r, c))

    # Step 2: BFS on the reversed graph
    # If a cell leads to an unsafe cell, it is also unsafe.
    # We traverse backwards from the exit nodes.
    while q:
        r, c = q.popleft()
        
        # Check potential predecessors (cells that point to the current unsafe cell)
        
        # 1. Cell above (r-1, c) points Down ('V') -> leads to (r, c)
        if r > 0:
            if grid[r-1][c] == 'V':
                if not visited[r-1][c]:
                    visited[r-1][c] = True
                    q.append((r-1, c))
        
        # 2. Cell below (r+1, c) points Up ('A') -> leads to (r, c)
        if r < N - 1:
            if grid[r+1][c] == 'A':
                if not visited[r+1][c]:
                    visited[r+1][c] = True
                    q.append((r+1, c))
        
        # 3. Cell to the left (r, c-1) points Right ('>') -> leads to (r, c)
        if c > 0:
            if grid[r][c-1] == '>':
                if not visited[r][c-1]:
                    visited[r][c-1] = True
                    q.append((r, c-1))
        
        # 4. Cell to the right (r, c+1) points Left ('<') -> leads to (r, c)
        if c < N - 1:
            if grid[r][c+1] == '<':
                if not visited[r][c+1]:
                    visited[r][c+1] = True
                    q.append((r, c+1))

    # Step 3: Count safe cells
    unsafe_count = 0
    for r in range(N):
        for c in range(N):
            if visited[r][c]:
                unsafe_count += 1
                
    print(N * N - unsafe_count)

if __name__ == '__main__':
    solve()