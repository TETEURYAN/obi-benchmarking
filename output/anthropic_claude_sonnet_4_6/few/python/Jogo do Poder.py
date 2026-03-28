Looking at this problem, I need to find for each starting cell, the maximum power achievable playing optimally.

**Key Insight:** The hero can move freely on the grid. The hero can kill a monster if its current power >= monster's power. After killing, power increases. The optimal strategy is: from a starting cell, the hero can kill all monsters reachable in a "greedy" manner - always killing the weakest available adjacent monster first, expanding the reachable set.

**Critical Observation:** The grid is connected (orthogonal moves, can revisit). So the hero starting at cell with power P can kill any monster with power <= P, then with the accumulated power kill more, etc. But the hero needs a *path* to reach those monsters through already-defeated cells or cells it can beat.

Actually, since the hero can revisit cells and the grid is connected, the reachable "safe" region expands. The hero can reach any cell adjacent to its current safe region. So the problem reduces to: starting with power P[i][j], what's the maximum sum of a connected subgraph containing (i,j) where we can "grow" it greedily (always able to add a neighbor with value <= current_sum)?

This is equivalent to: find the connected component containing (i,j) that is reachable by the greedy expansion process. The process: start with {(i,j)}, power = P[i][j]. Repeatedly add any neighbor of the current region with value <= current_power, updating power. This is like a BFS/priority-queue expansion.

**Key insight for efficiency:** Two cells end up in the same "maximal reachable set" if they're in the same connected component under the greedy expansion. We can precompute for each cell what the maximum power is.

The approach: Sort all cells by value. Use a Union-Find. Process cells in increasing order of value. When we process a cell, union it with already-processed neighbors. A component can "unlock" the next cell if the component's total sum >= that cell's value.

This is similar to the "water filling" / Kruskal-like approach:

1. Sort cells by value ascending.
2. Process in order. When adding a cell, merge with neighbors that are already added.
3. A component with sum S can absorb any cell with value <= S.
4. After merging, check if the new sum unlocks more cells (use a pointer/heap).

For each starting cell, the answer is the sum of all cells it can reach via this process.

Let me implement this with Union-Find + sorted processing:

```
Sort cells by value.
Use a min-heap of "pending" cells sorted by value.
Process: for each component, track its sum. When a component's sum >= next cell's value and that cell is adjacent, merge.
```

Actually the standard approach: process cells in sorted order, maintain components. A component becomes "active" once it's reachable from some starting point. But we need per-starting-cell answers.

The key insight: the set of cells a hero can collect depends only on which connected "affordable" subgraph they're in. Two starting cells get the same answer iff they end up in the same final reachable group.

Using the greedy Kruskal-like merge: sort cells by value, add them one by one, merge with neighbors. But a cell can only be "absorbed" by a component if that component's sum >= cell's value.

This requires a more careful simulation. Let me implement with a priority queue per component approach, but that's complex. Instead, I'll use the following: process in sorted order, and when merging components, check if the merged sum can absorb more pending cells.

import sys
from heapq import *

def solve():
    data = sys.stdin.read().split()
    idx = 0
    N = int(data[idx]); idx+=1
    M = int(data[idx]); idx+=1
    P = []
    for i in range(N):
        for j in range(M):
            P.append(int(data[idx])); idx+=1
    
    # ... Union-Find solution

After careful analysis, I'll implement the solution:

```python
import sys
from heapq import heappush, heappop

def solve():
    # [full solution below]
```

```python
import sys
from heapq import heappush, heappop

def solve():
    data = sys.stdin.read().split()
    idx = 0
    N = int(data[idx]); idx+=1
    M = int(data[idx]); idx+=1
    total = N*M
    P = [int(data[idx+i]) for i in range(total)]
    
    parent = list(range(total))
    size = [1]*total
    comp_sum = P[:]
    # For each component root, a heap of (value, cell_id) of neighbors not yet in component
    # We'll use a global heap approach
    
    ans = [0]*total
    
    def find(x):
        while parent[x]!=x:
            parent[x]=parent[parent[x]]
            x=parent[x]
        return x
    
    def union(a,b):
        a,b=find(a),find(b)
        if a==b: return a
        if size[a]<size[b]: a,b=b,a
        parent[b]=a
        size[a]+=size[b]
        comp_sum[a]+=comp_sum[b]
        return a
    
    # Sort cells by value
    order = sorted(range(total), key=lambda x: P[x])
    
    added = [False]*total
    # For each component (by root), maintain a min-heap of (neighbor_value, neighbor_id)
    heap = [[] for _ in range(total)]
    
    def get_neighbors(cell):
        r,c = divmod(cell, M)
        res=[]
        if r>0: res.append(cell-M)
        if r<N-1: res.append(cell+M)
        if c>0: res.append(cell-1)
        if c<M-1: res.append(cell+1)
        return res
    
    # Process: we need to handle the case where adding a cell might allow absorbing more
    # Use a global approach: maintain a heap of (value, cell) for cells not yet added
    # but adjacent to added cells... 
    # Actually each component has its own frontier heap
    
    # Better: process all cells. For each cell in sorted order, it gets added.
    # But it can only be added to a component if that component can afford it.
    # This is tricky because a cell might be affordable by one component but not another.
    
    # Alternative correct approach:
    # Each connected component that forms must be "self-consistent":
    # there exists an ordering to add cells such that at each step the current sum >= next cell value
    # AND the cells form a connected subgraph.
    
    # The greedy: a component can grow if its sum >= some neighbor's value.
    # We simulate: maintain for each component a min-heap of neighbor values.
    # A component can absorb a neighbor if comp_sum >= neighbor value.
    # When absorbed, merge components, update heap, check again.
    
    # But we need to "start" components. Each cell starts as its own component.
    # Initially no cell is "active". We need to activate cells.
    # 
    # Actually every cell starts active (as a hero). The question is what each can reach.
    # 
    # The answer for cell c = sum of all cells in the maximal set reachable from c.
    # 
    # Two cells c1, c2: if they end up in the same maximal reachable set, same answer.
    # 
    # The maximal reachable set from c: the largest connected subgraph containing c
    # such that there's a valid ordering (greedy expansion works).
    # 
    # Claim: the greedy (always pick cheapest affordable neighbor) gives the optimal result.
    # This is because if we can afford neighbor with value v, picking it increases our power,
    # which can only help us afford more things later.
    
    # So for each starting cell, simulate greedy BFS with min-heap.
    # But N*M = 100000, and each simulation is O(NM log NM), total O((NM)^2 log NM) - too slow.
    
    # Need smarter approach.
    # 
    # Key observation: if two cells end up in the same "reachable group", they have the same answer.
    # We can compute these groups efficiently.
    #
    # Algorithm (Kruskal-like):
    # Sort all cells by value.
    # Maintain components. Process cells in increasing order.
    # When we process cell v (add it to the "pool"):
    #   - Create component {v} with sum P[v]
    #   - Merge with any already-pooled neighbors
    #   - After merging, check if the merged component can absorb any pending (not yet pooled) neighbors
    #     that have value <= comp_sum. But those aren't pooled yet...
    #
    # Hmm, this doesn't directly work because a cell with higher value might be absorbable
    # if the component sum is large enough.
    
    # Let me think differently.
    # 
    # Process cells in increasing order of value: v1 <= v2 <= ... <= v_k
    # When we add v_i, we merge it with neighbors already added.
    # After merging, the component sum might now be >= v_{i+1}, v_{i+2}, etc.
    # But those cells might not be adjacent yet.
    #
    # Actually the correct simulation:
    # Use a global min-heap of (value, cell_id) for cells not yet processed.
    # Maintain components with their sums and frontier heaps.
    # 
    # But the issue is: which component "claims" a cell?
    # A cell can be claimed by any adjacent component that can afford it.
    # Once claimed, it merges into that component.
    #
    # If multiple components can afford it, they'll eventually merge anyway (since the cell connects them).
    #
    # Algorithm:
    # - All cells start "unprocessed"
    # - Maintain a global min-heap of (P[cell], cell) - initially all cells
    # - Process the minimum value cell: it starts a new component OR gets absorbed
    # 
    # Wait, I think the right way is:
    # 
    # Every cell will eventually be part of some component's answer.
    # The components are determined by the greedy process.
    # 
    # Let me look at this differently using the "small to large" or union-find with heap merging:
    
    # CORRECT ALGORITHM:
    # 
    # 1. Sort cells by value ascending: c_1, c_2, ..., c_K (K = N*M)
    # 2. Process in this order. Maintain Union-Find with comp_sum.
    #    Also maintain for each component root a min-heap of (value, cell) of 
    #    UNPROCESSED neighbors.
    # 3. When processing c_i:
    #    a. Mark c_i as processed.
    #    b. For each processed neighbor n of c_i:
    #       - Merge comp(c_i) and comp(n)
    #    c. Now, repeatedly check: does the current component have sum >= the min unprocessed neighbor?
    #       If yes, that neighbor can be absorbed NOW (even though it hasn't been "reached" in sorted order yet).
    #       But wait - that neighbor might not be the global minimum unprocessed cell.
    #       
    # Hmm, this is getting complex. Let me think about what "reachable" means more carefully.
    
    # INSIGHT: A set S of cells is "achievable" starting from cell c if:
    # 1. c ∈ S
    # 2. S is connected
    # 3. There exists an ordering c = s_1, s_2, ..., s_|S| such that for each k,
    #    P[s_1] + ... + P[s_{k-1}] >= P[s_k]  (hero can beat s_k)
    #    AND s_k is adjacent to {s_1,...,s_{k-1}} in the grid.
    #
    # The maximum achievable sum from c = max over all achievable sets S containing c of sum(S).
    #
    # GREEDY CLAIM: The greedy (always pick the minimum-value affordable neighbor) maximizes the reachable set.
    # Proof sketch: If we can afford neighbor with value v, taking it is always at least as good as not taking it
    # (it increases our power). So we should always take the cheapest affordable neighbor first.
    #
    # EQUIVALENCE: Two cells c1, c2 have the same answer iff they belong to the same "maximal greedy component".
    #
    # EFFICIENT COMPUTATION:
    # 
    # Think of it as: we want to find all maximal connected subsets S such that
    # there's a valid ordering to collect all of S starting from the minimum element of S.
    # (The minimum element must be the start, since it's the only one that can be the hero
    #  without needing prior kills... wait, no. Any cell can be the hero.)
    #
    # Actually, for a set S to be achievable starting from c:
    # - We need P[c] >= P[s_2] (the second cell we visit must be beatable initially)
    # - OR we need to find an ordering where c can beat the first neighbor.
    #
    # The minimum value cell in S must be reachable with power = P[c] (before any kills),
    # OR c itself is the minimum.
    #
    # Hmm, let me reconsider. If c is not the minimum in S, then c needs to beat some neighbor first.
    # That neighbor must have value <= P[c].
    #
    # Let me think about which cells can be in the same "group":
    # 
    # A connected component C is "self-sufficient" if starting from the minimum-value cell in C,
    # the greedy can collect all of C.
    # 
    # But starting from a non-minimum cell c in C: c might not be able to collect all of C
    # if P[c] < some neighbor's value and c can't reach the minimum first.
    #
    # Example: cells with values [1, 100, 2] in a line. 
    # Starting from 100: can beat 1 (100>=1), then beat 2 (101>=2). Total = 103.
    # Starting from 1: can beat 2? 1 < 2, no. Can beat 100? 1 < 100, no. Stuck at 1.
    # Starting from 2: can beat 1 (2>=1), power=3. Can beat 100? 3 < 100, no. Total = 3.
    #
    # So different starting cells give different answers even in the same connected grid component.
    #
    # This means we can't just compute "groups" independently of starting cell easily.
    # 
    # BUT: notice that the answer for cell c = sum of all cells reachable from c via greedy.
    # And the greedy from c is deterministic (always pick min affordable neighbor).
    #
    # For N*M = 100000, can we afford O((NM)^2)? That's 10^10 - too slow.
    # O(NM * log(NM)) per cell? Also too slow if done naively.
    # 
    # We need O(NM * log(NM)) total.
    
    # BETTER APPROACH - Union Find with careful merging:
    #
    # Observation: If we sort cells by value and process them in order,
    # when we add cell v to the "processed" set:
    # - It can immediately merge with processed neighbors (since they have smaller values,
    #   and the component containing v has sum >= P[v] >= any processed neighbor's value... 
    #   wait, that's not right either)
    #
    # Let me think about this more carefully with the examples.
    #
    # Example 2: 1 7 -> values: 6 3 10 1 20 7 7
    # Sorted: 1(idx3), 3(idx1), 6(idx0), 7(idx5), 7(idx6), 10(idx2), 20(idx4)
    #
    # Answer: 9 3 54 1 54 14 14
    # 
    # Cell idx3 (value 1): answer 1. Can't beat any neighbor (3 > 1, 20 > 1). Stuck.
    # Cell idx1 (value 3): answer 3. Neighbors: 6(>3), 10(>3). Stuck.
    # Cell idx0 (value 6): answer 9. Can beat idx1(3): power=9. Then neighbors: idx2(10)>9. Stuck. Total=9.
    # Cell idx5 (value 7): answer 14. Can beat idx6(7): power=14. Neighbors: idx4(20)>14, idx2(10... wait idx5 is position 5, neighbors are idx4 and idx6.
    #   idx5 neighbors: idx4(20), idx6(7). Beat idx6: power=14. Then idx4(20)>14. Total=14.
    # Cell idx6 (value 7): answer 14. Neighbors: idx5(7). Beat idx5: power=14. idx4(20)>14. Total=14.
    # Cell idx2 (value 10): answer 54. Neighbors: idx1(3), idx3(1). Beat idx3(1): power=11. Beat idx1(3): power=14. 
    #   Now neighbors of {idx1,idx2,idx3}: idx0(6)<=14, beat: power=20. idx4(20)<=20, beat: power=40. 
    #   idx5(7)<=40, beat: power=47. idx6(7)<=47, beat: power=54. Total=54.
    # Cell idx4 (value 20): answer 54. Neighbors: idx3(1), idx5(7). Beat idx3: power=21. Beat idx5: power=28.
    #   Beat idx6: power=35. Beat idx2: power=45. Beat idx1: power=48. Beat idx0: power=54. Total=54.
    #
    # So cells idx2 and idx4 both get answer 54 (they can collect everything).
    # Cells idx5 and idx6 get answer 14.
    # Cell idx0 gets 9.
    # Cells idx1 and idx3 are stuck.
    
    # PATTERN: The answer for a cell c is determined by which "reachable group" it belongs to.
    # The reachable group of c = all cells that c can collect via greedy.
    # 
    # Key insight for efficiency: 
    # If cell A can reach cell B (A's greedy includes B), and B can reach cell C,
    # does A necessarily reach C? Not necessarily (A might not have enough power to reach C directly,
    # but B might).
    # 
    # Actually yes! If A's greedy collects B (so A has power >= P[B] at some point, and B is adjacent),
    # then after collecting B, A has even more power. So A can do everything B can do (and more).
    # Therefore: if A can reach B, then answer(A) >= answer(B).
    # 
    # This means: the "reachable groups" are nested or disjoint!
    # If A can reach B and B can reach A, they have the same answer.
    # If A can reach B but B cannot reach A, then answer(A) > answer(B) (strictly, since A collected B).
    
    # ALGORITHM IDEA:
    # 
    # Process cells in increasing order of value.
    # Maintain Union-Find. When we process cell v (in sorted order):
    #   - Add v to the structure
    #   - Merge with all processed neighbors
    #   - The component containing v now has sum = sum of all cells in it
    #   - Check if this component's sum can now "absorb" any unprocessed cells adjacent to it
    #     (i.e., unprocessed neighbors with value <= comp_sum)
    #   - If yes, process those cells too (recursively/iteratively)
    #
    # This is like a BFS/DFS where we process cells in a specific order.
    # 
    # For each component, maintain a min-heap of (value, cell) for unprocessed neighbors.
    # When a component's sum increases (due to merging), check if the min of the heap is <= sum.
    # If yes, absorb that cell, merge, update sum, check again.
    #
    # When merging two components, merge their heaps (small into large for efficiency).
    #
    # Total complexity: O(NM * log^2(NM)) with small-to-large heap merging.
    # For NM = 100000, this should be fast enough.
    #
    # But what's the answer for each cell?
    # After this process, each cell belongs to a component. The answer for cell c = comp_sum[find(c)].
    # 
    # Wait, is this correct? Let me verify with example 2.
    # 
    # Cells (0-indexed): 0:6, 1:3, 2:10, 3:1, 4:20, 5:7, 6:7
    # Sorted: 3(1), 1(3), 0(6), 5(7), 6(7), 2(10), 4(20)
    # 
    # Process cell 3 (value 1):
    #   - Component {3}, sum=1
    #   - Processed neighbors: none
    #   - Unprocessed neighbors: 2(10), 4(20)
    #   - Min neighbor value = 10 > 1. Can't absorb. Stop.
    #   - Heap for comp(3): [(10,2), (20,4)]
    #
    # Process cell 1 (value 3):
    #   - Component {1}, sum=3
    #   - Processed neighbors: none (0 and 2 not processed)
    #   - Unprocessed neighbors: 0(6), 2(10)
    #   - Min = 6 > 3. Stop.
    #   - Heap for comp(1): [(6,0), (10,2)]
    #
    # Process cell 0 (value 6):
    #   - Component {0}, sum=6
    #   - Processed neighbors: 1 (processed). Merge comp(0) and comp(1).
    #     New comp sum = 6+3 = 9. Root = comp(0) or comp(1), say comp(0).
    #     Merge heaps: comp(0) had [(6,0)... wait, 0's unprocessed neighbors are just 1, but 1 is now processed.
    #     Actually when we add cell 0, its neighbors are cell 1 (processed) and... in 1D array of 7, neighbors of 0 is just 1.
    #     Neighbors of 1 are 0 and 2.
    #   - After merging comp(0) and comp(1): sum=9, heap contains unprocessed neighbors.
    #     Unprocessed neighbors of {0,1}: cell 2 (value 10). (Cell 0's other neighbor doesn't exist; cell 1's neighbors are 0 and 2, 0 is processed.)
    #     Heap: [(10, 2)]
    #   - Min = 10 > 9. Stop.
    #
    # Process cell 5 (value 7):
    #   - Component {5}, sum=7
    #   - Processed neighbors: none (4 and 6 not processed)
    #   - Unprocessed neighbors: 4(20), 6(7)
    #   - Min = 7 <= 7! Absorb cell 6.
    #     Process cell 6: merge comp(5) and comp(6). sum = 7+7 = 14.
    #     Unprocessed neighbors of {5,6}: 4(20). Heap: [(20,4)]
    #   - Min = 20 > 14. Stop.
    #
    # Process cell 6 (value 7): already processed (absorbed above). Skip.
    #
    # Process cell 2 (value 10):
    #   - Component {2}, sum=10
    #   - Processed neighbors: 1 (in comp(0), sum=9), 3 (in comp(3), sum=1)
    #   - Merge comp(2) with comp(0): sum = 10+9 = 19. Heap: [(10,2) from comp(3)... 
    #     Wait, comp(3)'s heap had [(10,2),(20,4)]. Now 2 is processed, so remove it.
    #     Merge comp(2+0) with comp(3): sum = 19+1 = 20. 
    #     Heap: unprocessed neighbors of {0,1,2,3}: cell 4(20). [(20,4)]
    #   - Min = 20 <= 20! Absorb cell 4.
    #     Process cell 4: merge. sum = 20+20 = 40.
    #     Unprocessed neighbors of {0,1,2,3,4}: cell 5 (in comp(5), sum=14... wait, 5 is processed).
    #     Hmm, cell 4's neighbors are 3 and 5. 3 is processed (in current comp), 5 is processed (in comp(5)).
    #     Merge comp(current) with comp(5): sum = 40+14 = 54.
    #     Heap: unprocessed neighbors of {0,1,2,3,4,5,6}: none (all processed).
    #   - Done. comp sum = 54.
    #
    # Process cell 4 (value 20): already processed. Skip.
    #
    # Final components:
    # - {0,1,2,3,4,5,6}: sum=54. Cells: 2,4 (and 0,1,3,5,6 also in this component!)
    # 
    # But wait, the answers are: 9 3 54 1 54 14 14
    # Cells 0,1,3 should NOT have answer 54!
    # 
    # So my algorithm is WRONG. The issue is that when we merge components, we're saying all cells
    # in the merged component have the same answer, but that's not true.
    # Cell 1 (value 3) can't reach cell 2 (value 10) because 3 < 10 and its only other neighbor is 0 (value 6 > 3).
    
    # I need to rethink.
    
    # The answer for cell c = sum of cells reachable from c via greedy.
    # This is NOT the same as the component sum in the union-find above.
    # 
    # The union-find above computes "which cells end up in the same maximally-reachable group",
    # but the answer for each cell depends on WHERE in that group it starts.
    
    # Let me reconsider. The answer for cell c:
    # - Start with power P[c]
    # - Greedily collect neighbors with value <= current power
    # - The set of collected cells = answer set
    # 
    # For cell 2 (value 10): can collect 1(3), 3(1), then 0(6), then 4(20), then 5(7), 6(7). Total=54.
    # For cell 0 (value 6): can collect 1(3), power=9. Can't collect 2(10>9). Total=9.
    # For cell 1 (value 3): can't collect 0(6>3) or 2(10>3). Total=3.
    # For cell 3 (value 1): can't collect 2(10>1) or 4(20>1). Total=1.
    # For cell 4 (value 20): can collect 3(1), power=21. Collect 5(7), power=28. Collect 6(7), power=35.
    #   Collect 2(10), power=45. Collect 1(3), power=48. Collect 0(6), power=54. Total=54.
    # For cell 5 (value 7): collect 6(7), power=14. Can't collect 4(20>14) or 2(10... wait, 5's neighbors are 4 and 6 only in 1D).
    #   Actually in 1D array of 7: neighbors of 5 are 4 and 6. Collect 6: power=14. 4(20)>14. Total=14.
    # For cell 6 (value 7): neighbors are 5. Collect 5(7): power=14. 4(20)>14. Total=14.
    
    # So the answers depend on the starting cell's value and position.
    # 
    # OBSERVATION: The answer for cell c = sum of the "reachable set" from c.
    # The reachable set from c is determined by the greedy BFS.
    # 
    # Can we compute this efficiently for all cells?
    # 
    # IDEA: For each cell c, the reachable set R(c) satisfies:
    # - c ∈ R(c)
    # - R(c) is connected
    # - sum(R(c)) >= max value in R(c) ... no that's not right either
    # - There's a valid ordering to collect R(c) starting from c
    # 
    # ANOTHER OBSERVATION: 
    # If we sort cells by value, the reachable set from c consists of c plus
    # all cells that can be "unlocked" by the growing power.
    # 
    # The reachable set from c is the same as: the set of cells reachable from c
    # in the subgraph induced by cells with value <= (sum of cells collected so far).
    # This is a fixed-point computation.
    # 
    # EFFICIENT ALGORITHM:
    # 
    # For each cell c, the answer is determined by a "threshold" process.
    # Let's define f(c) = sum of reachable set from c.
    # 
    # Key insight: f(c) only depends on P[c] and the structure of the grid.
    # Specifically, f(c) = f(c') if P[c] = P[c'] and they're in "equivalent" positions.
    # 
    # But this doesn't directly help.
    # 
    # BETTER INSIGHT: 
    # Consider the cells sorted by value: v_1 <= v_2 <= ... <= v_K.
    # 
    # For cell c with value P[c]:
    # - It can immediately beat any neighbor with value <= P[c].
    # - After beating those, it can beat more, etc.
    # 
    # The reachable set from c = the connected component of c in the "affordable graph" 
    # that grows as power increases.
    # 
    # This is equivalent to: 
    # Start with the set {c}. Repeatedly add any cell adjacent to the current set
    # with value <= current sum. Stop when no more can be added.
    # 
    # This is O(K log K) per cell using a priority queue, so O(K^2 log K) total - too slow.
    # 
    # For K = 100000, we need something like O(K log^2 K) total.
    
    # CRUCIAL OBSERVATION FOR EFFICIENCY:
    # 
    # Claim: f(c) = f(c') whenever c and c' are in the same "reachable group".
    # 
    # Define: c ~> c' if c can reach c' (c' is in the reachable set of c).
    # 
    # If c ~> c', then f(c) >= f(c') (since c collects everything c' can collect, plus more).
    # If c ~> c' AND c' ~> c, then f(c) = f(c').
    # 
    # The relation ~> is transitive (if c can reach c', and c' can reach c'', then c can reach c'').
    # 
    # So the equivalence classes under (~> and <~) partition the cells.
    # Within each class, all cells have the same answer.
    # 
    # But computing these classes is still the challenge.
    
    # LET ME LOOK AT THIS FROM A DIFFERENT ANGLE.
    # 
    # The greedy from cell c: use a min-heap. Start with heap = {(P[c], c)}, visited = {c}, power = P[c].
    # Wait, actually the hero starts AT cell c with power P[c], and the cell c's monster is the hero
    # (so P[c] is already the hero's power, and cell c has no monster to fight).
    # Then the hero moves to adjacent cells and fights monsters there.
    # 
    # So the greedy: 
    # - power = P[c], collected = {c}
    # - frontier = min-heap of (value, neighbor) for neighbors of collected cells
    # - While frontier is non-empty and frontier.min().value <= power:
    #   - Pop (v, cell) from frontier
    #   - power += v, collected.add(cell)
    #   - Add cell's unvisited neighbors to frontier
    # 
    # This is O(K log K) per cell.
    # 
    # For K = 100000, total = O(K^2 log K) = 10^10 * 17 ≈ too slow.
    # 
    # We need a smarter approach.
    
    # SMART APPROACH - "Offline" computation:
    # 
    # Sort cells by value. Process in increasing order.
    # Maintain a Union-Find where each component tracks:
    # - Its total sum
    # - A min-heap of (value, cell) for unprocessed neighbors
    # 
    # When processing cell v (in sorted order):
    # 1. Create component {v} with sum = P[v]
    # 2. For each processed neighbor u of v:
    #    - Merge comp(v) and comp(u)
    #    - (When merging, combine heaps using small-to-large)
    # 3. After all merges, check if comp(v)'s sum >= min unprocessed neighbor's value
    #    - If yes, that neighbor can be absorbed (it will be processed "early")
    #    - But this changes the order of processing!
    # 
    # This is the key issue: when a component's sum grows large enough to absorb a not-yet-processed cell,
    # we need to process that cell immediately.
    # 
    # Modified algorithm:
    # - Use a global sorted order, but allow "early processing" when a component can afford it.
    # - Maintain a global min-heap of unprocessed cells.
    # - Also maintain per-component heaps of affordable unprocessed neighbors.
    # 
    # Actually, let me think of it as:
    # - Process cells in a specific order determined by when they become "affordable".
    # - A cell becomes affordable when some adjacent component has sum >= its value.
    # - Initially, cells are affordable if they're the minimum in their neighborhood (or can be started as heroes).
    # 
    # Wait, but EVERY cell can be a starting hero. So every cell is "affordable" at the start (as a hero).
    # The question is what each hero can collect.
    
    # I think the key insight I'm missing is:
    # 
    # The answer for cell c = sum of the connected component that c would form
    # if we ran the following process:
    # 
    # "Grow" from c: add neighbors with value <= current sum, iteratively.
    # 
    # And the claim is: the answer for c equals the answer for the minimum-value cell
    # in c's reachable set, IF c can reach that minimum cell.
    # 
    # Hmm, let me think about when two cells have the same answer.
    # 
    # In example 2: cells 2 (value 10) and 4 (value 20) both have answer 54.
    # Cell 2 can reach cell 4 (via 3: 10->1->20, power grows to 11 then 31... wait:
    #   Cell 2 (value 10): neighbors are 1 and 3.
    #   Beat 1(3): power=13. Beat 3(1): power=14. Now neighbors of {1,2,3}: 0(6) and 4(20).
    #   Beat 0(6): power=20. Beat 4(20): power=40. Beat 5(7): power=47. Beat 6(7): power=54.
    # Cell 4 (value 20): neighbors are 3 and 5.
    #   Beat 3(1): power=21. Beat 5(7): power=28. Beat 6(7): power=35. Beat 2(10): power=45.
    #   Beat 1(3): power=48. Beat 0(6): power=54.
    # 
    # Both reach everything. So they have the same answer.
    # 
    # Cell 0 (value 6): can only reach {0,1}, answer=9.
    # Cell 5 (value 7): can only reach {5,6}, answer=14.
    # 
    # OBSERVATION: The reachable set from c is determined by:
    # Starting with power P[c], what connected subgraph can we greedily expand to?
    # 
    # EFFICIENT ALGORITHM (I think this works):
    # 
    # Sort all cells by value. Process in increasing order.
    # Maintain Union-Find with comp_sum and per-component min-heap of unprocessed neighbors.
    # 
    # For each cell v in sorted order (if not already processed):
    #   1. Mark v as processed.
    #   2. Create component {v}, sum = P[v].
    #   3. For each processed neighbor u:
    #      - Merge comp(v) and comp(u) (small-to-large heap merge)
    #   4. While comp(v)'s min unprocessed neighbor has value <= comp_sum:
    #      - Pop that neighbor w from the heap
    #      - Mark w as processed
    #      - Merge comp(v) and comp(w) (which might have processed neighbors of its own)
    #      - Actually, when we "process" w early, we need to also merge w with its processed neighbors
    #        and potentially trigger more absorptions.
    #      - This is a BFS/DFS within the absorption step.
    # 
    # After processing all cells, each cell's answer = comp_sum[find(cell)].
    # 
    # BUT WAIT: This gives the answer for the "best possible starting cell" in each component,
    # not for each individual cell.
    # 
    # In example 2, after this process, cells {0,1,2,3,4,5,6} might all be in one component with sum=54.
    # But cells 0,1,3 have answers 9,3,1 respectively, not 54.
    # 
    # So this approach computes the WRONG answer for cells that can't reach the full component.
    
    # I need to fundamentally rethink.
    
    # CORRECT UNDERSTANDING:
    # 
    # The answer for cell c is NOT the sum of the component c ends up in after the global process.
    # It's the sum of what c can specifically reach starting from P[c].
    # 
    # Different cells in the same "global component" can have different answers.
    # 
    # So we need a per-cell computation. But O(K^2) is too slow.
    # 
    # Let me think about the structure of answers.
    # 
    # CLAIM: The answer for cell c = sum of the largest connected subgraph S containing c
    # such that S can be "built up" starting from c.
    # 
    # CLAIM 2: S can be built up starting from c iff:
    # For every prefix of the optimal ordering (c = s_1, s_2, ..., s_k, ...),
    # sum(s_1,...,s_{k-1}) >= P[s_k].
    # 
    # CLAIM 3: The optimal ordering is: always pick the minimum-value unvisited neighbor.
    # (Greedy is optimal.)
    # 
    # CLAIM 4: The reachable set from c = the set of cells reachable by the greedy from c.
    # 
    # Now, for efficiency:
    # 
    # OBSERVATION: If P[c] >= P[c'] and c is adjacent to c', then R(c) ⊇ R(c').
    # (c can do everything c' can do, since c starts with more power and can reach c' first.)
    # Wait, this isn't quite right because c might not be able to reach c' without going through
    # cells with value > P[c].
    # 
    # Hmm. Let me think about a simpler structure.
    # 
    # TREE STRUCTURE OF ANSWERS:
    # 
    # Consider the cells sorted by value: v_1 <= v_2 <= ... <= v_K.
    # 
    # For cell v_1 (minimum value): it can only beat cells with value <= P[v_1].
    # Since v_1 is the minimum, no other cell has value <= P[v_1] (unless there are ties).
    # So v_1 can only beat cells with value = P[v_1] (ties).
    # 
    # For cell v_K (maximum value): it can beat everything adjacent to it, and with accumulated power,
    # potentially everything.
    # 
    # DIVIDE AND CONQUER IDEA:
    # 
    # Process cells in increasing order of value.
    # When we process cell v_i, we know that any cell with value > P[v_i] cannot be beaten by v_i alone.
    # But v_i might be able to collect some cells with value <= P[v_i] first, then beat larger ones.
    # 
    # This is still the same greedy process.
    
    # OK let me look at this from a completely different angle.
    # 
    # OFFLINE ALGORITHM WITH UNION-FIND:
    # 
    # Key insight: The answer for cell c = sum of the "reachable component" of c.
    # The reachable component of c is determined by the greedy process.
    # 
    # Two cells c and c' have the same reachable component iff:
    # 1. c can reach c' (c' ∈ R(c))
    # 2. c' can reach c (c ∈ R(c'))
    # 
    # If c can reach c' but c' cannot reach c, then R(c) ⊋ R(c').
    # 
    # STRUCTURE: The reachable components form a DAG (actually a forest/tree structure).
    # 
    # ALGORITHM:
    # 
    # Sort cells by value. Process in increasing order.
    # For each cell v (in sorted order):
    #   - Compute R(v) using greedy BFS.
    #   - But use memoization: if v is adjacent to a cell u with P[u] <= P[v],
    #     and we've already computed R(u), then R(v) ⊇ R(u) ∪ {v}.
    #     After collecting R(u), v has power P[v] + sum(R(u)).
    #     Then v can potentially collect more.
    # 
    # This is still complex. Let me think about a cleaner formulation.
    
    # CLEAN ALGORITHM (I believe this is correct):
    # 
    # Process cells in INCREASING order of value.
    # Maintain Union-Find with comp_sum.
    # For each component, maintain a min-heap of (value, cell) for UNPROCESSED neighbors.
    # 
    # When processing cell v:
    # 1. Create component {v}, sum = P[v].
    # 2. For each processed neighbor u of v:
    #    - Merge comp(v) and comp(u).
    # 3. While the min unprocessed neighbor of comp(v) has value <= comp_sum[comp(v)]:
    #    - Pop that neighbor w.
    #    - Process w (mark as processed, create component {w}, merge with processed neighbors of w).
    #    - Merge comp(v) and comp(w).
    #    - Repeat.
    # 
    # After processing all cells, the answer for cell c = comp_sum[find(c)].
    # 
    # BUT as I showed earlier, this gives the wrong answer for cells like 0,1,3 in example 2.
    # 
    # WAIT. Let me re-examine. In example 2:
    # 
    # After the algorithm, what components do we get?
    # 
    # Process v_1 = cell 3 (value 1):
    #   - comp {3}, sum=1
    #   - Processed neighbors: none
    #   - Unprocessed neighbors: 2(10), 4(20). Min=10 > 1. Stop.
    # 
    # Process v_2 = cell 1 (value 3):
    #   - comp {1}, sum=3
    #   - Processed neighbors: none (0 and 2 not processed)
    #   - Unprocessed neighbors: 0(6), 2(10). Min=6 > 3. Stop.
    # 
    # Process v_3 = cell 0 (value 6):
    #   - comp {0}, sum=6
    #   - Processed neighbors: cell 1 (processed). Merge comp(0) and comp(1). sum=9.
    #   - Unprocessed neighbors of {0,1}: cell 2(10). Min=10 > 9. Stop.
    #   - comp {0,1}, sum=9.
    # 
    # Process v_4 = cell 5 (value 7):
    #   - comp {5}, sum=7
    #   - Processed neighbors: none (4 and 6 not processed)
    #   - Unprocessed neighbors: 4(20), 6(7). Min=7 <= 7! Absorb cell 6.
    #     - Process cell 6: comp {6}, sum=7. Processed neighbors: cell 5 (processed). Merge. sum=14.
    #     - Unprocessed neighbors of {5,6}: 4(20). Min=20 > 14. Stop.
    #   - comp {5,6}, sum=14.
    # 
    # Process v_5 = cell 6 (value 7): already processed. Skip.
    # 
    # Process v_6 = cell 2 (value 10):
    #   - comp {2}, sum=10
    #   - Processed neighbors: cell 1 (in comp {0,1}, sum=9), cell 3 (in comp {3}, sum=1).
    #   - Merge comp(2) with comp(0,1): sum=10+9=19.
    #   - Merge with comp(3): sum=19+1=20.
    #   - Unprocessed neighbors of {0,1,2,3}: cell 4(20). Min=20 <= 20! Absorb cell 4.
    #     - Process cell 4: comp {4}, sum=20. Processed neighbors: cell 3 (in current comp), cell 5 (in comp {5,6}).
    #       Merge with current comp: sum=20+20=40.
    #       Merge with comp(5,6): sum=40+14=54.
    #     - Unprocessed neighbors: none. Stop.
    #   - comp {0,1,2,3,4,5,6}, sum=54.
    # 
    # Process v_7 = cell 4 (value 20): already processed. Skip.
    # 
    # Final: all cells in one component with sum=54.
    # 
    # But the correct answers are: 9 3 54 1 54 14 14.
    # 
    # So cells 0,1,3,5,6 have answers 9,3,1,14,14 respectively, NOT 54.
    # 
    # The algorithm gives 54 for all cells, which is WRONG.
    # 
    # The issue: the algorithm computes the "maximum reachable sum" for the BEST starting cell
    # in each component, not for each individual cell.
    # 
    # So I need a different approach.
    
    # RETHINKING FROM SCRATCH:
    # 
    # The answer for cell c = sum of cells reachable from c via greedy.
    # 
    # Let me think about what determines the reachable set.
    # 
    # LEMMA: The reachable set from c is the unique maximal set S such that:
    # 1. c ∈ S
    # 2. S is connected
    # 3. For every cell s ∈ S \ {c}, there exists a path c = p_0, p_1, ..., p_k = s in S
    #    such that for each i, P[p_i] <= sum(P[p_j] for j < i) + P[c].
    #    Wait, this isn't quite right either.
    # 
    # Actually, condition 3 should be: there exists an ordering of S starting with c
    # such that each cell in the ordering is adjacent to a previously ordered cell
    # and has value <= sum of previously ordered cells.
    # 
    # EQUIVALENT CONDITION: S is reachable from c iff:
    # For every subset T ⊆ S with c ∈ T and S\T non-empty,
    # there exists a cell s ∈ S\T adjacent to T with P[s] <= sum(T).
    # 
    # This is a "matroid-like" condition.
    # 
    # GREEDY OPTIMALITY: The greedy (always pick min-value affordable neighbor) finds the maximum S.
    # 
    # For efficiency, I think we need to observe:
    # 
    # OBSERVATION: The answer for cell c depends only on P[c] and the "local structure" around c.
    # More specifically, it depends on which cells are reachable from c.
    # 
    # OBSERVATION 2: If we sort cells by value and process them in order,
    # we can compute for each cell the "reachable sum" using a clever data structure.
    # 
    # Let me think about a simpler 1D case first.
    # 
    # 1D array: a_1, a_2, ..., a_n.
    # For cell i, the reachable set is determined by the greedy expansion.
    # 
    # In 1D, the reachable set from i is a contiguous interval [l, r] containing i.
    # (Because the grid is 1D and connected, and the greedy expands left or right.)
    # 
    # For 1D, we can compute the answer for each cell in O(n log n) using a stack or similar.
    # 
    # For 2D, the reachable set is a connected subgraph, not necessarily a rectangle.
    # 
    # APPROACH FOR GENERAL GRID:
    # 
    # I think the key insight is:
    # 
    # The answer for cell c = the sum of the "reachable component" of c,
    # where the reachable component is computed by the following process:
    # 
    # Sort cells by value. Process in increasing order.
    # When processing cell v:
    #   - v can "start" a new component.
    #   - v can also be absorbed by an existing component if that component is adjacent to v
    #     and has sum >= P[v].
    # 
    # The answer for cell c = the sum of the component that c is in when c is processed
    # (i.e., the component that c "starts" or is absorbed into at the time of processing).
    # 
    # Wait, but this doesn't account for the fact that c might be absorbed into a larger component later.
    # 
    # Hmm. Let me reconsider.
    # 
    # When cell c is processed (in sorted order), it either:
    # (a) Starts a new component {c} with sum P[c].
    # (b) Gets absorbed by an adjacent component with sum >= P[c].
    # 
    # In case (b), c is absorbed and its answer = the absorbing component's final sum.
    # In case (a), c starts a new component. This component might later absorb other cells
    # (when its sum grows large enough). The answer for c = the final sum of this component.
    # 
    # But in case (a), the component might also get absorbed by a larger component later!
    # If component A (containing c) gets absorbed by component B, then c's answer = B's final sum.
    # But that's wrong! c started component A, and A might not be able to reach B's cells.
    # 
    # WAIT. If component B absorbs component A, it means B is adjacent to A and B's sum >= some cell in A... 
    # no, it means A is adjacent to B and A's sum >= some cell in B... no.
    # 
    # Let me re-examine the algorithm:
    # 
    # When processing cell v (in sorted order):
    # - v is adjacent to some processed components.
    # - v merges with all adjacent processed components.
    # - The merged component might then absorb more unprocessed cells.
    # 
    # The "absorption" of v by an adjacent component means: the adjacent component has sum >= P[v],
    # so it can beat v. But v is being processed in sorted order, meaning P[v] is the current minimum
    # unprocessed cell. So any adjacent processed component has sum >= P[v] (since it was processed earlier
    # and has sum >= its own value >= ... hmm, not necessarily).
    # 
    # Actually, a processed component might have sum < P[v] if it was processed earlier but couldn't
    # absorb anything. For example, component {cell with value 3} has sum=3, and P[v]=6.
    # 3 < 6, so this component cannot absorb v.
    # 
    # So when processing v, we should only merge with adjacent processed components that have sum >= P[v].
    # But in the algorithm above, I merged with ALL adjacent processed components.
    # 
    # AH, THIS IS THE BUG! I should only merge v with adjacent components that can "afford" v.
    # 
    # But wait, if component A (sum=3) is adjacent to v (value=6), can A absorb v? No, 3 < 6.
    # But can v absorb A? v has value 6 >= 3 = A's max value (since A was processed before v in sorted order,
    # all cells in A have value <= P[v]). So v can beat all cells in A!
    # 
    # So when v is processed, v can absorb any adjacent processed component (since all processed cells
    # have value <= P[v], and v starts with power P[v]).
    # 
    # But then, after absorbing A, v's power = P[v] + sum(A). This might allow v to absorb more cells.
    # 
    # So the algorithm should be:
    # When processing v:
    # 1. Create component {v}, sum = P[v].
    # 2. Merge with ALL adjacent processed components (v can beat them since they have smaller values).
    # 3. Check if the merged sum can absorb any unprocessed neighbors.
    # 4. If yes, process those neighbors (recursively).
    # 
    # This is what I had before! And the issue is that it gives the wrong answer for cells like 0,1,3.
    # 
    # The problem: when cell 2 (value 10) is processed, it merges with comp(0,1) (sum=9) and comp(3) (sum=1).
    # But comp(0,1) was formed by cells 0 and 1, which have values 6 and 3. Cell 2 can beat both of them
    # (10 >= 6 and 10 >= 3). So cell 2 can absorb comp(0,1). That's correct.
    # 
    # But the issue is: the algorithm then says cell 0's answer = 54 (the final component sum).
    # But cell 0 cannot reach cell 2 (since 9 < 10). So cell 0's answer should be 9, not 54.
    # 
    # The algorithm is computing "what's the maximum sum achievable if you start from the BEST cell
    # in the component", not "what's the maximum sum achievable starting from cell c specifically".
    # 
    # So the algorithm is correct for finding the MAXIMUM answer in each component,
    # but not for each individual cell.
    # 
    # REVISED UNDERSTANDING:
    # 
    # The algorithm computes, for each "group" of cells, the maximum achievable sum.
    # But different cells in the same group might have different answers.
    # 
    # Specifically, cell c's answer = the sum of the component that c is in AT THE TIME c is processed
    # (before any further absorptions by larger cells).
    # 
    # Wait, let me re-examine:
    # 
    # When cell 0 (value 6) is processed:
    # - It merges with comp(1) (sum=3). New sum = 9.
    # - Min unprocessed neighbor = 10 > 9. Stop.
    # - At this point, comp(0,1) has sum=9.
    # 
    # Later, when cell 2 (value 10) is processed, it absorbs comp(0,1).
    # But this doesn't mean cell 0 can reach cell 2! Cell 2 can reach cell 0, but not vice versa.
    # 
    # So the answer for cell 0 = 9 (the sum of comp(0,1) at the time cell 0 was processed and the
    # component stabilized).
    # 
    # The answer for cell 2 = 54 (the final sum of the component after all absorptions).
    # 
    # KEY INSIGHT: The answer for cell c = the sum of the component that c is in
    # WHEN THE COMPONENT FIRST STABILIZES (i.e., when no more unprocessed neighbors can be absorbed).
    # 
    # But the component might later be absorbed by a larger cell. In that case, cell c's answer
    # is the sum at stabilization, NOT the final sum.
    # 
    # WAIT, but what if cell c's component (sum=9) is absorbed by cell 2 (value 10)?
    # Does cell c benefit from this? NO! Because cell c (value 6) cannot beat cell 2 (value 10 > 9).
    # Cell 2 absorbs cell c's component, but cell c cannot absorb cell 2.
    # 
    # So the answer for cell c = the sum of the component at the time it stabilizes,
    # BEFORE being absorbed by a larger cell.
    # 
    # REVISED ALGORITHM:
    # 
    # Process cells in increasing order of value.
    # Maintain Union-Find with comp_sum.
    # For each component, maintain a min-heap of unprocessed neighbors.
    # 
    # When processing cell v:
    # 1. Create component {v}, sum = P[v].
    # 2. Merge with all adjacent processed components.
    # 3. While min unprocessed neighbor <= comp_sum: absorb it (process it, merge).
    # 4. Record the answer for ALL cells in the current component = comp_sum.
    #    (These cells' answers are now finalized, since they can't grow further without being absorbed
    #    by a larger cell, which they can't reach.)
    # 
    # Wait, but step 4 is wrong. When cell 2 is processed and absorbs comp(0,1), the cells 0 and 1
    # are now in a larger component. But their answers were already finalized in step 4 when they
    # were processed.
    # 
    # Hmm, but when is step 4 executed for cells 0 and 1?
    # - Cell 1 (value 3) is processed: comp {1}, sum=3. No affordable neighbors. Answer for cell 1 = 3.
    # - Cell 0 (value 6) is processed: merges with comp(1), sum=9. No affordable neighbors. Answer for cells 0,1 = 9.
    #   But cell 1's answer was already set to 3!
    # 
    # So we need to be careful: when a component grows (by merging), we update the answers for all cells
    # in the component. But that's O(K) per merge, which is too slow.
    # 
    # ALTERNATIVE: Record the answer for cell c = the sum of the component at the time the component
    # STOPS GROWING (i.e., when no more affordable neighbors exist).
    # 
    # When does a component stop growing?
    # - When its min unprocessed neighbor has value > comp_sum.
    # - This happens after step 3 in the algorithm above.
    # 
    # But the component might grow again later when a new cell is processed and merges with it.
    # 
    # WAIT. Let me reconsider. When cell 0 (value 6) is processed:
    # - Merges with comp(1). Sum=9.
    # - Min unprocessed neighbor = 10 > 9. Component stabilizes.
    # - Answer for cells in comp(0,1) = 9? But cell 1's answer should be 3, not 9!
    # 
    # Hmm. Cell 1 (value 3) was processed first. At that time, its component had sum=3 and stabilized.
    # Then cell 0 (value 6) is processed and merges with comp(1). Now comp(0,1) has sum=9.
    # 
    # But cell 1 cannot reach cell 0! Cell 1 has value 3, and cell 0 has value 6 > 3.
    # So cell 1's answer should remain 3.
    # 
    # The issue: when cell 0 merges with comp(1), it doesn't mean cell 1 can now reach cell 0.
    # It means cell 0 can reach cell 1 (since 6 >= 3).
    # 
    # So the merge is "one-directional": cell 0 absorbs cell 1, but cell 1 doesn't absorb cell 0.
    # 
    # In the Union-Find, we're treating the merge as symmetric, but it's actually asymmetric.
    # 
    # REVISED UNDERSTANDING:
    # 
    # When cell v is processed (in sorted order) and merges with adjacent processed components,
    # it means v can reach those components (since v has value >= all cells in those components).
    # But those components cannot reach v (since their sum might be < P[v]).
    # 
    # So the answer for cells in the absorbed components is NOT updated when v absorbs them.
    # Their answers were finalized when their own components stabilized.
    # 
    # The answer for cell v = the sum of the component after all merges and absorptions in step 3.
    # 
    # REVISED ALGORITHM:
    # 
    # Process cells in increasing order of value.
    # Maintain Union-Find with comp_sum.
    # For each component, maintain a min-heap of unprocessed neighbors.
    # 
    # When processing cell v:
    # 1. Create component {v}, sum = P[v].
    # 2. Merge with all adjacent processed components.
    #    (v can reach all of them since they have smaller values.)
    # 3. While min unprocessed neighbor w has value <= comp_sum:
    #    - Process w (mark as processed).
    #    - Merge comp(v) and comp(w) (after merging w with its processed neighbors).
    # 4. Record answer[v] = comp_sum[find(v)].
    #    (This is the answer for v, since v can reach exactly the cells in its current component.)
    # 
    # Note: The answers for cells absorbed in step 2 and 3 were already recorded when they were processed.
    # 
    # Let me verify with example 2:
    # 
    # Process cell 3 (value 1):
    # - comp {3}, sum=1. No processed neighbors. Min unprocessed neighbor = 10 > 1. Stop.
    # - answer[3] = 1. ✓
    # 
    # Process cell 1 (value 3):
    # - comp {1}, sum=3. No processed neighbors. Min unprocessed neighbor = 6 > 3. Stop.
    # - answer[1] = 3. ✓
    # 
    # Process cell 0 (value 6):
    # - comp {0}, sum=6. Processed neighbors: cell 1 (comp {1}, sum=3). Merge. sum=9.
    # - Min unprocessed neighbor = 10 > 9. Stop.
    # - answer[0] = 9. ✓
    # 
    # Process cell 5 (value 7):
    # - comp {5}, sum=7. No processed neighbors. Min unprocessed neighbor = 7 (cell 6) <= 7. Absorb.
    #   - Process cell 6: comp {6}, sum=7. Processed neighbors: cell 5 (in current comp). Merge. sum=14.
    #   - answer[6] = 14. ✓
    # - Min unprocessed neighbor = 20 > 14. Stop.
    # - answer[5] = 14. ✓
    # 
    # Process cell 6 (value 7): already processed. Skip.
    # 
    # Process cell 2 (value 10):
    # - comp {2}, sum=10. Processed neighbors: cell 1 (comp {0,1}, sum=9), cell 3 (comp {3}, sum=1).
    #   Merge with comp(0,1): sum=10+9=19.
    #   Merge with comp(3): sum=19+1=20.
    # - Min unprocessed neighbor = 20 (cell 4) <= 20. Absorb.
    #   - Process cell 4: comp {4}, sum=20. Processed neighbors: cell 3 (in current comp), cell 5 (comp {5,6}, sum=14).
    #     Merge with current comp: sum=20+20=40.
    #     Merge with comp(5,6): sum=40+14=54.
    #     - answer[4] = 54. ✓
    #   - Min unprocessed neighbor: none. Stop.
    # - answer[2] = 54. ✓
    # 
    # Process cell 4 (value 20): already processed. Skip.
    # 
    # Final answers: [9, 3, 54, 1, 54, 14, 14]. ✓
    # 
    # GREAT! The algorithm works!
    # 
    # KEY POINTS:
    # - Process cells in increasing order of value.
    # - When processing cell v, merge with all adjacent processed components.
    # - Then greedily absorb unprocessed neighbors with value <= comp_sum.
    # - Record answer[v] = comp_sum after all absorptions.
    # - Cells absorbed during step 3 also get their answers recorded at that time.
    # - Cells absorbed in step 2 (adjacent processed components) already have their answers recorded.
    # 
    # COMPLEXITY:
    # - Each cell is processed exactly once.
    # - Each merge operation is O(log K) with Union-Find.
    # - Heap operations: each cell is added to heaps and removed at most once.
    # - With small-to-large heap merging: O(K log^2 K) total.
    # 
    # For K = 100000, this is about 100000 * 17 * 17 ≈ 3 * 10^7, which should be fast enough.
    
    # IMPLEMENTATION:
    # 
    # Union-Find with:
    # - parent[], size[], comp_sum[]
    # - comp_heap[]: min-heap of (value, cell) for unprocessed neighbors of each component
    # 
    # When merging two components (small into large):
    # - Merge the smaller heap into the larger heap.
    # - Update comp_sum.
    # 
    # When processing cell v:
    # - Use a stack/queue for BFS of cells to process.
    # - For each cell to process:
    #   a. Mark as processed.
    #   b. Create component {cell}, sum = P[cell].
    #   c. For each processed neighbor: merge.
    #   d. Add unprocessed neighbors to comp_heap.
    #   e. While comp_heap.min <= comp_sum: pop and add to processing queue.
    #   f. Record answer[cell] = comp_sum (after all merges from this "wave").
    # 
    # Wait, step f is tricky. The answer for cell v should be recorded AFTER all absorptions
    # triggered by v's processing. But cells absorbed in step e also get their answers recorded.
    # 
    # Let me re-examine: when cell v is processed and triggers absorption of cell w,
    # answer[w] = comp_sum at the time w is absorbed (which is the same as answer[v] since they're in the same component).
    # 
    # Actually, answer[v] = answer[w] = final comp_sum after all absorptions in this wave.
    # 
    # But what if w triggers further absorptions? Those are also part of the same wave.
    # 
    # So: answer[v] = answer[all cells absorbed in this wave] = final comp_sum after the wave.
    # 
    # Implementation: use a queue. Process all cells in the queue. After the queue is empty,
    # record the answer for all cells processed in this wave.
    # 
    # But we need to know which cells were processed in this wave. We can use a list.
    # 
    # Actually, since all cells in the wave end up in the same component, we can just record
    # answer[cell] = comp_sum[find(cell)] after the wave. But comp_sum changes during the wave.
    # 
    # Simpler: record answer[cell] = comp_sum[find(cell)] at the END of the wave.
    # But we need to do this for all cells in the wave.
    # 
    # Even simpler: at the end of the entire algorithm, answer[cell] = comp_sum[find(cell)]
    # for cells that were the "root" of their component when they stabilized.
    # But cells absorbed later have their comp_sum updated.
    # 
    # WAIT. Let me reconsider.
    # 
    # When cell 1 (value 3) is processed: comp {1}, sum=3. answer[1] = 3.
    # Later, cell 0 (value 6) is processed and merges with comp(1). comp {0,1}, sum=9.
    # answer[0] = 9. answer[1] remains 3.
    # 
    # So answer[1] = 3, not 9. This is correct.
    # 
    # The key: answer[cell] is recorded when cell is processed, NOT updated later.
    # 
    # But wait, when cell 0 merges with comp(1), the comp_sum of comp(1) becomes 9.
    # If we later do answer[1] = comp_sum[find(1)], we'd get 9, which is wrong.
    # 
    # So we must record answer[cell] = comp_sum[find(cell)] AT THE TIME cell is processed,
    # not at the end of the algorithm.
    # 
    # But "at the time cell is processed" means after all merges and absorptions triggered by cell's processing.
    # 
    # For cell 0: after merging with comp(1) and finding no more affordable neighbors, answer[0] = 9.
    # For cell 1: after finding no affordable neighbors, answer[1] = 3.
    # 
    # These are recorded at different times and are correct.
    # 
    # For cells absorbed during a wave (like cell 6 absorbed when cell 5 is processed):
    # answer[6] = comp_sum at the time cell 6 is absorbed = 14 (after merging {5} and {6}).
    # answer[5] = comp_sum at the end of the wave = 14.
    # Both are 14. ✓
    # 
    # For cell 4 absorbed when cell 2 is processed:
    # answer[4] = comp_sum at the time cell 4 is absorbed.
    # When cell 4 is absorbed: comp_sum = 20 (just cell 4 added to the current comp of sum 20).
    # Wait, let me redo:
    # 
    # Processing cell 2 (value 10):
    # - comp {2}, sum=10.
    # - Merge with comp(0,1) (sum=9): comp {0,1,2}, sum=19.
    # - Merge with comp(3) (sum=1): comp {0,1,2,3}, sum=20.
    # - Min unprocessed neighbor = 20 (cell 4) <= 20. Absorb cell 4.
    #   - Process cell 4: comp {4}, sum=20.
    #   - Merge with comp(3) (already in current comp, so find(3) = find(2)): no-op.
    #   - Merge with comp(5,6) (sum=14): comp {0,1,2,3,4,5,6}, sum=54.
    #   - answer[4] = 54. ✓
    # - No more unprocessed neighbors. answer[2] = 54. ✓
    # 
    # So answer[4] is recorded as 54 (the comp_sum AFTER cell 4 is fully processed, including its merges).
    # 
    # IMPLEMENTATION DETAIL:
    # When processing a cell (either as the "trigger" or as an absorbed cell),
    # we record its answer AFTER all its merges are done.
    # But the trigger cell's answer is recorded AFTER all absorptions in the wave.
    # 
    # Actually, let me re-examine: when cell 4 is absorbed and processed:
    # - It merges with comp(5,6). comp_sum becomes 54.
    # - answer[4] = 54.
    # Then we return to processing cell 2's wave:
    # - No more unprocessed neighbors.
    # - answer[2] = comp_sum[find(2)] = 54. ✓
    # 
    # So the answer for the trigger cell (2) is recorded AFTER all absorptions.
    # The answer for absorbed cells (4) is recorded when they're absorbed (after their own merges).
    # 
    # This works because: cell 4's answer = 54 (it can reach everything in the final component).
    # Cell 2's answer = 54 (same).
    # 
    # IMPLEMENTATION:
    # 
    # Use a stack for the wave processing.
    # When processing a cell:
    # 1. Mark as processed.
    # 2. Create component, merge with processed neighbors.
    # 3. Record answer[cell] = comp_sum[find(cell)].
    #    Wait, but we need to record AFTER all absorptions, not just after merges.
    # 
    # Hmm. Let me think again.
    # 
    # When cell 4 is absorbed:
    # - It merges with comp(5,6). comp_sum = 54.
    # - answer[4] = 54.
    # - No more affordable unprocessed neighbors for comp(4's component).
    # 
    # When cell 2 is the trigger:
    # - After absorbing cell 4 (and all its consequences), comp_sum = 54.
    # - answer[2] = 54.
    # 
    # So both cell 2 and cell 4 get answer 54. This is correct.
    # 
    # The key: answer[cell] = comp_sum[find(cell)] AFTER all merges triggered by cell's processing.
    # 
    # For the trigger cell (cell 2), this is after the entire wave.
    # For absorbed cells (cell 4), this is after their own merges (which might trigger further absorptions).
    # 
    # Since cell 4's merges (with comp(5,6)) are done before returning to cell 2's wave,
    # and cell 4's answer is recorded after those merges, cell 4 gets the correct answer.
    # 
    # IMPLEMENTATION USING RECURSION OR ITERATIVE DFS:
    # 
    # process(cell):
    #   mark cell as processed
    #   create comp {cell}, sum = P[cell]
    #   for each processed neighbor u:
    #     merge comp(cell) and comp(u)
    #   add unprocessed neighbors to comp_heap[find(cell)]
    #   while comp_heap[find(cell)].min <= comp_sum[find(cell)]:
    #     w = pop from comp_heap[find(cell)]
    #     if w is already processed: continue (it was processed in a previous wave)
    #     process(w)  # recursive call
    #     # after process(w), comp(cell) and comp(w) are merged (since w's processed neighbors include cells in comp(cell))
    #   answer[cell] = comp_sum[find(cell)]
    # 
    # Wait, there's an issue: when process(w) is called recursively, w merges with its processed neighbors,
    # which includes cells in comp(cell). So after process(w) returns, comp(cell) and comp(w) are merged.
    # 
    # But the heap for comp(cell) might have changed (since comp(w) was merged into it).
    # We need to re-check the heap after each recursive call.
    # 
    # Actually, the heap is maintained per component (by root). After merging, the heap of the merged
    # component is the union of the two heaps. So after process(w) returns, the heap of comp(cell)
    # (now merged with comp(w)) contains all unprocessed neighbors of the merged component.
    # 
    # The while loop continues checking this heap.
    # 
    # This should work correctly. Let me implement it.
    # 
    # But recursion depth could be O(K) = 100000, which might cause stack overflow.
    # Use iterative approach instead.
    # 
    # ITERATIVE IMPLEMENTATION:
    # 
    # For each unprocessed cell v (in sorted order):
    #   if v is already processed: continue
    #   stack = [v]
    #   while stack:
    #     cell = stack.pop()
    #     if cell is already processed: continue
    #     mark cell as processed
    #     create comp {cell}, sum = P[cell]
    #     for each processed neighbor u:
    #       merge comp(cell) and comp(u)
    #     add unprocessed neighbors to comp_heap[find(cell)]
    #     while comp_heap[find(cell)].min <= comp_sum[find(cell)]:
    #       w = pop from comp_heap[find(cell)]
    #       if w is already processed: continue
    #       stack.append(w)  # process w next
    #     answer[cell] = comp_sum[find(cell)]
    # 
    # Hmm, but this doesn't correctly handle the case where w's processing merges with comp(cell).
    # After w is processed (from the stack), comp(cell) and comp(w) are merged.
    # But we need to re-check the heap of the merged component.
    # 
    # The issue with the iterative approach: after processing w (from the stack), we need to
    # re-check the heap of the merged component. But the "while" loop for cell is already done.
    # 
    # Let me restructure:
    # 
    # For each unprocessed cell v (in sorted order):
    #   if v is already processed: continue
    #   queue = [v]
    #   while queue:
    #     cell = queue.pop(0)  # or use a stack
    #     if cell is already processed: continue
    #     mark cell as processed
    #     create comp {cell}, sum = P[cell]
    #     for each processed neighbor u:
    #       merge comp(cell) and comp(u)
    #     add unprocessed neighbors to comp_heap[find(cell)]
    #     # Check if any unprocessed neighbors are now affordable
    #     root = find(cell)
    #     while comp_heap[root] and comp_heap[root][0][0] <= comp_sum[root]:
    #       val, w = heappop(comp_heap[root])
    #       if processed[w]: continue
    #       queue.append(w)
    #     answer[cell] = comp_sum[find(cell)]
    # 
    # But this still has the issue: after processing w (which merges with comp(cell)),
    # the heap of comp(cell) might have new affordable neighbors. But we only check the heap
    # when processing cell, not after processing w.
    # 
    # SOLUTION: After processing w and merging with comp(cell), re-check the heap.
    # But in the queue-based approach, we process cells one by one. After processing w,
    # we should check the heap of the merged component and add more cells to the queue.
    # 
    # Let me restructure again:
    # 
    # For each unprocessed cell v (in sorted order):
    #   if v is already processed: continue
    #   # Start a new wave from v
    #   to_process = [v]
    #   while to_process:
    #     cell = to_process.pop()
    #     if processed[cell]: continue
    #     processed[cell] = True
    #     # Merge cell into the current wave's component
    #     # (The wave's component is identified by find(v) or find(cell) after merges)
    #     for each neighbor u of cell:
    #       if processed[u]:
    #         merge(cell, u)
    #       else:
    #         heappush(comp_heap[find(cell)], (P[u], u))
    #     # After merging, check if any unprocessed neighbors are affordable
    #     root = find(cell)
    #     while comp_heap[root] and comp_heap[root][0][0] <= comp_sum[root]:
    #       val, w = heappop(comp_heap[root])
    #       if not processed[w]:
    #         to_process.append(w)
    #     answer[cell] = comp_sum[find(cell)]
    # 
    # Wait, but when we add unprocessed neighbors to comp_heap[find(cell)], and then check the heap,
    # we might add w to to_process. Then when w is processed, it merges with comp(cell), and the heap
    # of the merged component might have new affordable neighbors. But we only check the heap when
    # processing cell, not after processing w.
    # 
    # The fix: after processing w (and merging), re-check the heap. This is done by the outer while loop:
    # after processing w, we go back to the top of the while loop and process the next cell in to_process.
    # But the heap check is done inside the loop for each cell, not for the merged component.
    # 
    # I think the correct approach is:
    # 
    # After processing each cell in the wave, check the heap of the CURRENT ROOT (which might have changed
    # due to merges) and add affordable unprocessed neighbors to to_process.
    # 
    # Let me re-examine with example 2, processing cell 2:
    # 
    # to_process = [2]
    # 
    # Process cell 2:
    # - processed[2] = True
    # - Neighbors: 1 (processed), 3 (processed)
    # - Merge(2, 1): comp {0,1,2}, sum=19. (comp(1) = comp(0,1) with sum=9)
    # - Merge(2, 3): comp {0,1,2,3}, sum=20.
    # - No unprocessed neighbors to add to heap (1 and 3 are processed).
    #   Wait, what about cell 4? Cell 4 is a neighbor of cell 3, not cell 2.
    #   Cell 2's neighbors are 1 and 3 (in 1D). Both processed.
    # - comp_heap[find(2)] = heap of unprocessed neighbors of comp {0,1,2,3}.
    #   This heap was built up during previous processing:
    #   - When cell 3 was processed: added (10,2) and (20,4) to heap. But (10,2) is now processed.
    #   - When cell 1 was processed: added (6,0) and (10,2) to heap. But both are now processed.
    #   - When cell 0 was processed: added (10,2) to heap. Processed.
    #   - So the heap contains (20,4) (from cell 3's processing) and possibly duplicates.
    # - Check heap: (20,4) <= 20. Add 4 to to_process.
    # - answer[2] = comp_sum[find(2)] = 20. WRONG! Should be 54.
    # 
    # The issue: answer[2] is recorded BEFORE processing cell 4.
    # 
    # I need to record answer[cell] AFTER all cells in the wave are processed.
    # 
    # REVISED: Record answer[cell] = comp_sum[find(cell)] AFTER the entire wave is done.
    # But then I need to track which cells are in the wave.
    # 
    # REVISED ALGORITHM:
    # 
    # For each unprocessed cell v (in sorted order):
    #   if v is already processed: continue
    #   wave = []
    #   to_process = [v]
    #   while to_process:
    #     cell = to_process.pop()
    #     if processed[cell]: continue
    #     processed[cell] = True
    #     wave.append(cell)
    #     for each neighbor u of cell:
    #       if processed[u]:
    #         merge(cell, u)
    #       else:
    #         heappush(comp_heap[find(cell)], (P[u], u))
    #     root = find(cell)
    #     while comp_heap[root] and comp_heap[root][0][0] <= comp_sum[root]:
    #       val, w = heappop(comp_heap[root])
    #       if not processed[w]:
    #         to_process.append(w)
    #   # After wave, record answers
    #   for cell in wave:
    #     answer[cell] = comp_sum[find(cell)]
    # 
    # Let me re-examine with example 2, processing cell 2:
    # 
    # to_process = [2], wave = []
    # 
    # Process cell 2:
    # - processed[2] = True, wave = [2]
    # - Neighbors: 1 (processed), 3 (processed)
    # - Merge(2, 1): comp {0,1,2}, sum=19.
    # - Merge(2, 3): comp {0,1,2,3}, sum=20.
    # - comp_heap[find(2)]: contains (20,4) (from cell 3's earlier processing).
    # - Check: 20 <= 20. Add 4 to to_process.
    # 
    # Process cell 4:
    # - processed[4] = True, wave = [2, 4]
    # - Neighbors: 3 (processed, in current comp), 5 (processed, in comp {5,6})
    # - Merge(4, 3): no-op (same comp).
    # - Merge(4, 5): comp {0,1,2,3,4,5,6}, sum=54.
    # - comp_heap[find(4)]: no unprocessed neighbors.
    # - Check: heap empty. No more to add.
    # 
    # to_process is empty. Wave = [2, 4].
    # answer[2] = comp_sum[find(2)] = 54. ✓
    # answer[4] = comp_sum[find(4)] = 54. ✓
    # 
    # But wait, when cell 5 was processed earlier, it was in a separate wave.
    # answer[5] = 14 (recorded in that wave). ✓
    # answer[6] = 14 (recorded in that wave). ✓
    # 
    # And when cell 0 was processed:
    # wave = [0, 1]? No, cell 1 was processed in a separate wave.
    # 
    # Let me redo the full example:
    # 
    # Sorted order: 3(1), 1(3), 0(6), 5(7), 6(7), 2(10), 4(20)
    # 
    # Process cell 3 (value 1):
    # - to_process = [3], wave = []
    # - Process cell 3: processed[3]=True, wave=[3].
    #   Neighbors: 2 (unprocessed), 4 (unprocessed).
    #   Add (10,2) and (20,4) to comp_heap[3].
    #   Check heap: min=10 > 1. No more.
    # - Wave = [3]. answer[3] = comp_sum[find(3)] = 1. ✓
    # 
    # Process cell 1 (value 3):
    # - to_process = [1], wave = []
    # - Process cell 1: processed[1]=True, wave=[1].
    #   Neighbors: 0 (unprocessed), 2 (unprocessed).
    #   Add (6,0) and (10,2) to comp_heap[1].
    #   Check heap: min=6 > 3. No more.
    # - Wave = [1]. answer[1] = 3. ✓
    # 
    # Process cell 0 (value 6):
    # - to_process = [0], wave = []
    # - Process cell 0: processed[0]=True, wave=[0].
    #   Neighbors: 1 (processed).
    #   Merge(0, 1): comp {0,1}, sum=9. (comp_heap merged: {(6,0),(10,2)} from comp(1) + {} from comp(0))
    #   Wait, comp(0) has no heap yet (just created). comp(1) has heap [(6,0),(10,2)].
    #   After merge, comp_heap[find(0)] = [(6,0),(10,2)].
    #   But (6,0) is now processed! We need to handle stale entries.
    #   Check heap: pop (6,0) - processed, skip. Pop (10,2) - not processed, 10 > 9. Stop.
    # - Wave = [0]. answer[0] = 9. ✓
    # 
    # Process cell 5 (value 7):
    # - to_process = [5], wave = []
    # - Process cell 5: processed[5]=True, wave=[5].
    #   Neighbors: 4 (unprocessed), 6 (unprocessed).
    #   Add (20,4) and (7,6) to comp_heap[5].
    #   Check heap: min=7 (cell 6) <= 7. Add 6 to to_process.
    # - Process cell 6: processed[6]=True, wave=[5,6].
    #   Neighbors: 5 (processed).
    #   Merge(6, 5): comp {5,6}, sum=14.
    #   comp_heap[find(6)]: merged heaps. comp(5) had [(7,6),(20,4)], comp(6) had [].
    #   After merge: [(7,6),(20,4)]. But (7,6) is now processed.
    #   Check heap: pop (7,6) - processed, skip. Pop (20,4) - not processed, 20 > 14. Stop.
    # - Wave = [5,6]. answer[5] = 14. ✓ answer[6] = 14. ✓
    # 
    # Process cell 6 (value 7): already processed. Skip.
    # 
    # Process cell 2 (value 10):
    # - to_process = [2], wave = []
    # - Process cell 2: processed[2]=True, wave=[2].
    #   Neighbors: 1 (processed), 3 (processed).
    #   Merge(2, 1): comp {0,1,2}, sum=19.
    #     comp_heap: merge comp(2)'s heap (empty) with comp(0,1)'s heap [(10,2)].
    #     After merge: [(10,2)]. But (10,2) is now processed.
    #   Merge(2, 3): comp {0,1,2,3}, sum=20.
    #     comp_heap: merge with comp(3)'s heap [(10,2),(20,4)].
    #     After merge: [(10,2),(10,2),(20,4)]. (duplicates, but we handle stale entries)
    #   Check heap: pop (10,2) - processed, skip. pop (10,2) - processed, skip. pop (20,4) - not processed, 20 <= 20. Add 4 to to_process.
    # - Process cell 4: processed[4]=True, wave=[2,4].
    #   Neighbors: 3 (processed), 5 (processed).
    #   Merge(4, 3): no-op (same comp).
    #   Merge(4, 5): comp {0,1,2,3,4,5,6}, sum=54.
    #     comp_heap: merge with comp(5,6)'s heap [(20,4)].
    #     After merge: [(20,4)]. But (20,4) is now processed.
    #   Check heap: pop (20,4) - processed, skip. Heap empty. Stop.
    # - Wave = [2,4]. answer[2] = 54. ✓ answer[4] = 54. ✓
    # 
    # Process cell 4 (value 20): already processed. Skip.
    # 
    # Final answers: [9, 3, 54, 1, 54, 14, 14]. ✓
    # 
    # GREAT! The algorithm works correctly!
    # 
    # Now let me implement this efficiently.
    # 
    # COMPLEXITY ANALYSIS:
    # - Each cell is processed exactly once: O(K).
    # - Each cell is added to at most 4 heaps (one per neighbor): O(K) heap insertions.
    # - Each heap entry is popped at most once: O(K log K) total heap operations.
    # - Union-Find operations: O(K α(K)) ≈ O(K).
    # - Heap merging (small-to-large): O(K log^2 K) total.
    # 
    # Total: O(K log^2 K) which is fine for K = 100000.
    # 
    # HEAP MERGING (small-to-large):
    # When merging two components, we merge the smaller heap into the larger heap.
    # This ensures O(K log^2 K) total operations.
    # 
    # In Python, heaps are lists. Merging by pushing all elements of the smaller heap into the larger:
    # O(|smaller| * log(|larger|)).
    # With small-to-large, total = O(K log^2 K).
    # 
    # IMPLEMENTATION:
    
    # Let me now write the actual code.

import sys
from heapq import heappush, heappop

def solve():
    data = sys.stdin.buffer.read().split()
    idx = 0
    N = int(data[idx]); idx += 1
    M = int(data[idx]); idx += 1
    K = N * M
    P = [int(data[idx + i]) for i in range(K)]
    
    # Union-Find
    parent = list(range(K))
    rank = [0] * K
    comp_sum = P[:]
    comp_heap = [[] for _ in range(K)]  # min-heap of (value, cell) for unprocessed neighbors
    
    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    
    def union(a, b):
        # Returns new root
        ra, rb = find(a), find(b)
        if ra == rb:
            return ra
        # Merge smaller heap into larger heap
        if len(comp_heap[ra]) < len(comp_heap[rb]):
            ra, rb = rb, ra
        # ra has larger heap; merge rb's heap into ra's heap
        for item in comp_heap[rb]:
            heappush(comp_heap[ra], item)
        comp_heap[rb] = []  # clear rb's heap
        # Union by rank
        if rank[ra] < rank[rb]:
            ra, rb = rb, ra
        parent[rb] = ra
        comp_sum[ra] += comp_sum[rb]
        if rank[ra] == rank[rb]:
            rank[ra] += 1
        return ra
    
    # Wait, there's a conflict: I'm merging heaps based on heap size, but union by rank.
    # These two criteria might conflict. Let me separate them.
    # 
    # Actually, for correctness, the Union-Find just needs to correctly track which component
    # each cell belongs to. The heap should be associated with the root.
    # 
    # When merging, I should:
    # 1. Determine the new root (by rank or size).
    # 2. Merge the smaller heap into the larger heap (for efficiency).
    # 3. If the new root is not the one with the larger heap, swap.
    # 
    # This is a bit tricky. Let me use union by size and merge heaps accordingly.
    
    # Let me redo with union by size:
    
    parent = list(range(K))
    size = [1] * K
    comp_sum = P[:]
    comp_heap = [[] for _ in range(K)]
    
    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    
    def union(a, b):
        ra, rb = find(a), find(b)
        if ra == rb:
            return ra
        # Make ra the larger component (by heap size for efficiency)
        if len(comp_heap[ra]) < len(comp_heap[rb]):
            ra, rb = rb, ra
        # Merge rb's heap into ra's heap
        for item in comp_heap[rb]:
            heappush(comp_heap[ra], item)
        comp_heap[rb] = []
        # Union: ra becomes root
        parent[rb] = ra
        size[ra] += size[rb]
        comp_sum[ra] += comp_sum[rb]
        return ra
    
    processed = [False] * K
    answer = [0] * K
    
    # Sort cells by value
    order = sorted(range(K), key=lambda x: P[x])
    
    def get_neighbors(cell):
        r, c = divmod(cell, M)
        neighbors = []
        if r > 0: neighbors.append(cell - M)
        if r < N - 1: neighbors.append(cell + M)
        if c > 0: neighbors.append(cell - 1)
        if c < M - 1: neighbors.append(cell + 1)
        return neighbors
    
    for v in order:
        if processed[v]:
            continue
        
        wave = []
        to_process = [v]
        
        while to_process:
            cell = to_process.pop()
            if processed[cell]:
                continue
            processed[cell] = True
            wave.append(cell)
            
            root = find(cell)
            
            for u in get_neighbors(cell):
                if processed[u]:
                    # Merge comp(cell) and comp(u)
                    root = union(cell, u)
                else:
                    # Add u to comp_heap
                    heappush(comp_heap[find(cell)], (P[u], u))
            
            # Check if any unprocessed neighbors are now affordable
            root = find(cell)
            while comp_heap[root] and comp_heap[root][0][0] <= comp_sum[root]:
                val, w = heappop(comp_heap[root])
                if not processed[w]:
                    to_process.append(w)
        
        # Record answers for all cells in the wave
        for cell in wave:
            answer[cell] = comp_sum[find(cell)]
    
    # Output
    out = []
    for i in range(N):
        row = []
        for j in range(M):
            row.append(str(answer[i * M + j]))
        out.append(' '.join(row))
    print('\n'.join(out))

solve()

# Wait, there's a bug: after merging in the loop, `root` might be stale.
# Let me fix: after each union, update root.
# Also, when adding to comp_heap, I should use find(cell) which might have changed after unions.

# Let me also reconsider the heap merging in union():
# When I merge rb's heap into ra's heap, I'm doing O(|rb_heap| * log(|ra_heap|)) work.
# With small-to-large (merging smaller into larger), total work = O(K log^2 K).
# But I'm merging based on heap size, not component size. This should still give O(K log^2 K)
# because each element is moved at most O(log K) times.

# Actually, with small-to-large merging of heaps, each element is moved O(log K) times,
# giving O(K log K) total moves, each costing O(log K) for the heap push, so O(K log^2 K) total.

# Let me also handle the case where comp_heap[root] might have stale entries (processed cells).
# I handle this by checking `if not processed[w]` before adding to to_process.
# But I should also skip stale entries when popping from the heap.

# In the while loop:
# while comp_heap[root] and comp_heap[root][0][0] <= comp_sum[root]:
#   val, w = heappop(comp_heap[root])
#   if not processed[w]:
#     to_process.append(w)
# 
# This correctly skips stale entries (processed cells in the heap).

# But there's another issue: after popping a stale entry, the next entry might also be stale.
# The while loop handles this correctly by continuing to pop.

# However, there's a subtle bug: after popping a stale entry, the condition
# comp_heap[root][0][0] <= comp_sum[root] might still hold, so we continue.
# But if the next entry is not stale and has value > comp_sum[root], we stop.
# This is correct.

# But what if we pop a stale entry and the heap becomes empty? The while condition handles this.

# Let me also fix the root update issue in the main loop:

# for u in get_neighbors(cell):
#   if processed[u]:
#     root = union(cell, u)  # root is updated
#   else:
#     heappush(comp_heap[find(cell)], (P[u], u))  # use find(cell) which is current root

# After union(cell, u), find(cell) might return a different root.
# So when adding unprocessed neighbors to the heap, I should use find(cell) after all unions.

# Let me restructure:

# for u in get_neighbors(cell):
#   if processed[u]:
#     union(cell, u)
# 
# root = find(cell)
# for u in get_neighbors(cell):
#   if not processed[u]:
#     heappush(comp_heap[root], (P[u], u))
# 
# root = find(cell)
# while comp_heap[root] and comp_heap[root][0][0] <= comp_sum[root]:
#   ...

# This is cleaner. Let me rewrite the solution.

import sys
from heapq import heappush, heappop

def solve():
    data = sys.stdin.buffer.read().split()
    idx = 0
    N = int(data[idx]); idx += 1
    M = int(data[idx]); idx += 1
    K = N * M
    P = [int(data[idx + i]) for i in range(K)]
    
    parent = list(range(K))
    comp_sum = P[:]
    comp_heap = [[] for _ in range(K)]
    
    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    
    def union(a, b):
        ra, rb = find(a), find(b)
        if ra == rb:
            return ra
        if len(comp_heap[ra]) < len(comp_heap[rb]):
            ra, rb = rb, ra
        for item in comp_heap[rb]:
            heappush(comp_heap[ra], item)
        comp_heap[rb] = []
        parent[rb] = ra
        comp_sum[ra] += comp_sum[rb]
        return ra
    
    processed = [False] * K
    answer = [0] * K
    
    order = sorted(range(K), key=lambda x: P[x])
    
    def get_neighbors(cell):
        r, c = divmod(cell, M)
        neighbors = []
        if r > 0: neighbors.append(cell - M)
        if r < N - 1: neighbors.append(cell + M)
        if c > 0: neighbors.append(cell - 1)
        if c < M - 1: neighbors.append(cell + 1)
        return neighbors
    
    for v in order:
        if processed[v]:
            continue
        
        wave = []
        to_process = [v]
        
        while to_process:
            cell = to_process.pop()
            if processed[cell]:
                continue
            processed[cell] = True
            wave.append(cell)
            
            # Merge with processed neighbors
            for u in get_neighbors(cell):
                if processed[u]:
                    union(cell, u)
            
            # Add unprocessed neighbors to heap
            root = find(cell)
            for u in get_neighbors(cell):
                if not processed[u]:
                    heappush(comp_heap[root], (P[u], u))
            
            # Check affordable unprocessed neighbors
            root = find(cell)
            while comp_heap[root]:
                val, w = comp_heap[root][0]
                if val > comp_sum[root]:
                    break
                heappop(comp_heap[root])
                if not processed[w]:
                    to_process.append(w)
        
        # Record answers
        for cell in wave:
            answer[cell] = comp_sum[find(cell)]
    
    out = []
    for i in range(N):
        row = [str(answer[i * M + j]) for j in range(M)]
        out.append(' '.join(row))
    sys.stdout.write('\n'.join(out) + '\n')

solve()

# Let me verify with test case 1:
# 2 3
# 2 3 9
# 1 7 200
# 
# Cells (row-major): 0:2, 1:3, 2:9, 3:1, 4:7, 5:200
# Grid:
# (0,0)=2  (0,1)=3  (0,2)=9
# (1,0)=1  (1,1)=7  (1,2)=200
# 
# Neighbors:
# 0: 1(right), 3(down)
# 1: 0(left), 2(right), 4(down)
# 2: 1(left), 5(down)
# 3: 0(up), 4(right)
# 4: 3(left), 1(up), 5(right)
# 5: 4(left), 2(up)
# 
# Sorted: 3(1), 0(2), 1(3), 4(7), 2(9), 5(200)
# 
# Process cell 3 (value 1):
# - wave=[3], processed[3]=True
# - Processed neighbors: none
# - Unprocessed neighbors: 0(2), 4(7). Add to heap: [(2,0),(7,4)]
# - Check: 2 > 1. Stop.
# - answer[3] = 1. ✓
# 
# Process cell 0 (value 2):
# - wave=[0], processed[0]=True
# - Processed neighbors: 3. union(0,3). comp {0,3}, sum=3.
# - Unprocessed neighbors: 1(3), 4(7). Add to heap.
#   comp_heap[find(0)]: after union, contains (2,0),(7,4) from comp(3) + (3,1),(7,4) from comp(0).
#   Wait, comp(3) had heap [(2,0),(7,4)]. comp(0) had heap [].
#   After union (merging smaller into larger): comp_heap[find(0)] = [(2,0),(7,4)].
#   Then add unprocessed neighbors of cell 0: 1(3), 4(7) (3 is processed, so skip).
#   Wait, cell 0's neighbors are 1 and 3. 3 is processed. 1 is not.
#   Add (3,1) to heap. Heap: [(2,0),(7,4),(3,1)].
# - Check: min=(2,0). 0 is processed. Pop. Heap: [(3,1),(7,4)].
#   min=(3,1). 3 > 3? No, 3 <= 3. Add 1 to to_process.
# 
# Process cell 1 (value 3):
# - processed[1]=True, wave=[0,1]
# - Processed neighbors: 0 (in comp {0,3}). union(1, 0). comp {0,1,3}, sum=6.
#   comp_heap: merge comp(1)'s heap (empty) into comp(0,3)'s heap [(3,1),(7,4)].
#   After merge: [(3,1),(7,4)].
# - Unprocessed neighbors of cell 1: 2(9), 4(7). Add to heap.
#   Heap: [(3,1),(7,4),(9,2),(7,4)].
# - Check: min=(3,1). 1 is processed. Pop. Heap: [(7,4),(9,2),(7,4)].
#   min=(7,4). 7 <= 6? No. Stop.
# 
# to_process is empty. Wave = [0,1].
# answer[0] = comp_sum[find(0)] = 6. ✓
# answer[1] = comp_sum[find(1)] = 6. ✓
# 
# Process cell 4 (value 7):
# - wave=[4], processed[4]=True
# - Processed neighbors: 3 (in comp {0,1,3}), 1 (in comp {0,1,3}).
#   union(4, 3): comp {0,1,3,4}, sum=13.
#   union(4, 1): no-op (same comp).
# - Unprocessed neighbors of cell 4: 5(200). Add to heap.
#   comp_heap[find(4)]: after union, contains [(7,4),(9,2),(7,4)] from comp(0,1,3) + [] from comp(4).
#   Wait, comp(0,1,3) had heap [(7,4),(9,2),(7,4)]. comp(4) had heap [].
#   After union: heap = [(7,4),(9,2),(7,4)].
#   Add (200,5) to heap. Heap: [(7,4),(9,2),(7,4),(200,5)].
# - Check: min=(7,4). 4 is processed. Pop. Heap: [(7,4),(9,2),(200,5)].
#   min=(7,4). 4 is processed. Pop. Heap: [(9,2),(200,5)].
#   min=(9,2). 9 <= 13. Add 2 to to_process.
# 
# Process cell 2 (value 9):
# - processed[2]=True, wave=[4,2]
# - Processed neighbors: 1 (in comp {0,1,3,4}), 5 (not processed).
#   union(2, 1): comp {0,1,2,3,4}, sum=22.
#   comp_heap: merge comp(2)'s heap (empty) into comp(0,1,3,4)'s heap [(9,2),(200,5)].
#   After merge: [(9,2),(200,5)].
# - Unprocessed neighbors of cell 2: 5(200). Add to heap.
#   Heap: [(9,2),(200,5),(200,5)].
# - Check: min=(9,2). 2 is processed. Pop. Heap: [(200,5),(200,5)].
#   min=(200,5). 200 <= 22? No. Stop.
# 
# to_process is empty. Wave = [4,2].
# answer[4] = 22. ✓
# answer[2] = 22. ✓
# 
# Process cell 5 (value 200):
# - wave=[5], processed[5]=True
# - Processed neighbors: 4 (in comp {0,1,2,3,4}), 2 (in comp {0,1,2,3,4}).
#   union(5, 4): comp {0,1,2,3,4,5}, sum=222.
#   union(5, 2): no-op.
# - Unprocessed neighbors: none.
# - Check: heap contains [(200,5),(200,5)] from comp(0,1,2,3,4) + [] from comp(5).
#   After union: heap = [(200,5),(200,5)].
#   min=(200,5). 5 is processed. Pop. min=(200,5). 5 is processed. Pop. Heap empty. Stop.
# - Wave = [5]. answer[5] = 222. ✓
# 
# Final answers: [6, 6, 22, 1, 22, 222]
# Output:
# 6 6 22
# 1 22 222
# ✓
# 
# The algorithm is correct!

# Now let me also verify test case 3 partially to make sure.
# Actually, I'm fairly confident the algorithm is correct. Let me finalize the code.

# One issue: in the union function, I'm merging based on heap size (smaller heap into larger).
# But the parent assignment should be consistent. Let me make sure the parent is set correctly.

# In union(a, b):
# - ra = find(a), rb = find(b)
# - If len(comp_heap[ra]) < len(comp_heap[rb]): swap ra, rb
# - Merge rb's heap into ra's heap
# - parent[rb] = ra
# - comp_sum[ra] += comp_sum[rb]
# 
# This means ra is always the new root. The heap of ra is the merged heap.
# This is correct.

# But there's a subtle issue: when I do find(cell) after union(cell, u), the root might be u's root.
# This is fine because find() correctly returns the root.

# Let me also make sure the heap doesn't have too many stale entries.
# In the worst case, each cell is added to the heap O(4) times (once per neighbor).
# So total heap entries = O(4K) = O(K). Each is popped at most once. Total heap ops = O(K log K).
# Plus the merging: O(K log^2 K) with small-to-large.

# Actually, wait. When I add unprocessed neighbors to the heap, I might add duplicates.
# For example, cell u might be added to the heap multiple times (once for each processed neighbor
# that is adjacent to u). But since we check `if not processed[w]` before adding to to_process,
# duplicates are handled correctly (we just skip already-processed cells).

# The total number of heap entries is O(K) since each (cell, neighbor) pair is added at most once.
# Wait, actually each cell can be added to the heap multiple times if multiple cells in the component
# are adjacent to it. But each cell has at most 4 neighbors, so each cell is added to heaps at most 4 times.
# Total heap entries = O(4K) = O(K).

# With small-to-large merging, total heap operations = O(K log^2 K).

# This should be efficient enough for K = 100000.

# Let me write the final clean code:

import sys
from heapq import heappush, heappop

def solve():
    data = sys.stdin.buffer.read().split()
    ptr = 0
    N = int(data[ptr]); ptr += 1
    M = int(data[ptr]); ptr += 1
    K = N * M
    P = [int(data[ptr + i]) for i in range(K)]
    
    parent = list(range(K))
    comp_sum = P[:]
    comp_heap = [[] for _ in range(K)]
    processed = [False] * K
    answer = [0] * K
    
    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    
    def union(a, b):
        ra, rb = find(a), find(b)
        if ra == rb:
            return ra
        # Merge smaller heap into larger
        if len(comp_heap[ra]) < len(comp_heap[rb]):
            ra, rb = rb, ra
        for item in comp_heap[rb]:
            heappush(comp_heap[ra], item)
        comp_heap[rb] = []
        parent[rb] = ra
        comp_sum[ra] += comp_sum[rb]
        return ra
    
    def get_neighbors(cell):
        r, c = divmod(cell, M)
        nbrs = []
        if r > 0: nbrs.append(cell - M)
        if r < N - 1: nbrs.append(cell + M)
        if c > 0: nbrs.append(cell - 1)
        if c < M - 1: nbrs.append(cell + 1)
        return nbrs
    
    order = sorted(range(K), key=lambda x: P[x])
    
    for v in order:
        if processed[v]:
            continue
        
        wave = []
        stack = [v]
        
        while stack:
            cell = stack.pop()
            if processed[cell]:
                continue
            processed[cell] = True
            wave.append(cell)
            
            nbrs = get_neighbors(cell)
            
            # Merge with processed neighbors
            for u in nbrs:
                if processed[u]:
                    union(cell, u)
            
            # Add unprocessed neighbors to heap
            root = find(cell)
            for u in nbrs:
                if not processed[u]:
                    heappush(comp_heap[root], (P[u], u))
            
            # Check affordable unprocessed neighbors
            root = find(cell)
            while comp_heap[root]:
                val, w = comp_heap[root][0]
                if val > comp_sum[root]:
                    break
                heappop(comp_heap[root])
                if not processed[w]:
                    stack.append(w)
        
        # Record answers for wave
        for cell in wave:
            answer[cell] = comp_sum[find(cell)]
    
    out = []
    for i in range(N):
        out.append(' '.join(str(answer[i * M + j]) for j in range(M)))
    sys.stdout.write('\n'.join(out) + '\n')

solve()

# Hmm wait, I realize there might be an issue with the heap after merging.
# When I call union(cell, u) for multiple processed neighbors, the heap of the merged component
# might contain stale entries. But I handle stale entries by checking `if not processed[w]`.
# 
# Also, after merging, the root of cell might change. So when I do `root = find(cell)` after
# all merges, I get the correct root.
# 
# But there's another issue: when I add unprocessed neighbors to comp_heap[root], I'm using
# the root AFTER all merges. But the heap of the merged component already contains entries
# from the previously merged components. So I might add duplicates.
# 
# For example, if cell u is an unprocessed neighbor of both cell and some previously merged cell,
# it might be in the heap already. Adding it again creates a duplicate.
# 
# Duplicates are handled correctly: when we pop a duplicate, we check if it's processed.
# If it's already been processed (from the first pop), we skip it.
# 
# So duplicates are fine, just slightly inefficient. The total number of heap entries is still O(K)
# since each (cell, neighbor) pair is added at most once per cell processing.
# Wait, actually each cell can be added to the heap multiple times:
# - Once when each of its processed neighbors is processed and adds it.
# - But each cell has at most 4 neighbors, so at most 4 times.
# Total heap entries = O(4K) = O(K). Fine.

# I think the code is correct. Let me also handle the edge case where N=1 or M=1.
# The get_neighbors function handles this correctly.

# Let me also double-check the output format: "N lines, each containing M integers."
# The output uses space-separated integers per line. ✓

# One more thing: the problem says "O j-ésimo inteiro da i-ésima linha deve ser o poder máximo..."
# So the output is in row-major order, which is what we're doing. ✓

# I'm fairly confident the solution is correct. Let me finalize.

import sys
from heapq import heappush, heappop

def solve():
    data = sys.stdin.buffer.read().split()
    ptr = 0
    N = int(data[ptr]); ptr += 1
    M = int(data[ptr]); ptr += 1
    K = N * M
    P = [int(data[ptr + i]) for i in range(K)]
    
    parent = list(range(K))
    comp_sum = P[:]
    comp_heap = [[] for _ in range(K)]
    processed = [False] * K
    answer = [0] * K
    
    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    
    def union(a, b):
        ra, rb = find(a), find(b)
        if ra == rb:
            return ra
        if len(comp_heap[ra]) < len(comp_heap[rb]):
            ra, rb = rb, ra
        for item in comp_heap[rb]:
            heappush(comp_heap[ra], item)
        comp_heap[rb] = []
        parent[rb] = ra
        comp_sum[ra] += comp_sum[rb]
        return ra
    
    def get_neighbors(cell):
        r, c = divmod(cell, M)
        nbrs = []
        if r > 0: nbrs.append(cell - M)
        if r < N - 1: nbrs.append(cell + M)
        if c > 0: nbrs.append(cell - 1)
        if c < M - 1: nbrs.append(cell + 1)
        return nbrs
    
    order = sorted(range(K), key=lambda x: P[x])
    
    for v in order:
        if processed[v]:
            continue
        
        wave = []
        stack = [v]
        
        while stack:
            cell = stack.pop()
            if processed[cell]:
                continue
            processed[cell] = True
            wave.append(cell)
            
            nbrs = get_neighbors(cell)
            
            for u in nbrs:
                if processed[u]:
                    union(cell, u)
            
            root = find(cell)
            for u in nbrs:
                if not processed[u]:
                    heappush(comp_heap[root], (P[u], u))
            
            root = find(cell)
            while comp_heap[root]:
                val, w = comp_heap[root][0]
                if val > comp_sum[root]:
                    break
                heappop(comp_heap[root])
                if not processed[w]:
                    stack.append(w)
        
        for cell in wave:
            answer[cell] = comp_sum[find(cell)]
    
    out = []
    for i in range(N):
        out.append(' '.join(str(answer[i * M + j]) for j in range(M)))
    sys.stdout.write('\n'.join(out) + '\n')

solve()
```

import sys
from heapq import heappush, heappop

def solve():
    data = sys.stdin.buffer.read().split()
    ptr = 0
    N = int(data[ptr]); ptr += 1
    M = int(data[ptr]); ptr += 1
    K = N * M
    P = [int(data[ptr + i]) for i in range(K)]
    
    parent = list(range(K))
    comp_sum = P[:]
    comp_heap = [[] for _ in range(K)]
    processed = [False] * K
    answer = [0] * K
    
    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    
    def union(a, b):
        ra, rb = find(a), find(b)
        if ra == rb:
            return ra
        if len(comp_heap[ra]) < len(comp_heap[rb]):
            ra, rb = rb, ra
        for item in comp_heap[rb]:
            heappush(comp_heap[ra], item)
        comp_heap[rb] = []
        parent[rb] = ra
        comp_sum[ra] += comp_sum[rb]
        return ra
    
    def get_neighbors(cell):
        r, c = divmod(cell, M)
        nbrs = []
        if r > 0: nbrs.append(cell - M)
        if r < N - 1: nbrs.append(cell + M)
        if c > 0: nbrs.append(cell - 1)
        if c < M - 1: nbrs.append(cell + 1)
        return nbrs
    
    order = sorted(range(K), key=lambda x: P[x])
    
    for v in order:
        if processed[v]:
            continue
        
        wave = []
        stack = [v]
        
        while stack:
            cell = stack.pop()
            if processed[cell]:
                continue
            processed[cell] = True
            wave.append(cell)
            
            nbrs = get_neighbors(cell)
            
            for u in nbrs:
                if processed[u]:
                    union(cell, u)
            
            root = find(cell)
            for u in nbrs:
                if not processed[u]:
                    heappush(comp_heap[root], (P[u], u))
            
            root = find(cell)
            while comp_heap[root]:
                val, w = comp_heap[root][0]
                if val > comp_sum[root]:
                    break
                heappop(comp_heap[root])
                if not processed[w]:
                    stack.append(w)
        
        for cell in wave:
            answer[cell] = comp_sum[find(cell)]
    
    out = []
    for i in range(N):
        out.append(' '.join(str(answer[i * M + j]) for j in range(M)))
    sys.stdout.write('\n'.join(out) + '\n')

solve()