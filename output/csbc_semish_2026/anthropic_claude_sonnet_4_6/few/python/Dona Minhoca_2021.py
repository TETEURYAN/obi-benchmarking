import sys
from collections import deque

def solve():
    sys.setrecursionlimit(200000)
    data = sys.stdin.read().split()
    idx = 0
    N = int(data[idx]); idx += 1
    
    adj = [[] for _ in range(N + 1)]
    for _ in range(N - 1):
        x = int(data[idx]); idx += 1
        y = int(data[idx]); idx += 1
        adj[x].append(y)
        adj[y].append(x)
    
    # For each pair of nodes (u, v) not connected by an edge,
    # adding edge (u,v) creates a cycle of length dist(u,v) + 1
    # We need to find the maximum dist(u,v)+1 and count pairs achieving it.
    
    # The diameter of the tree gives the maximum cycle length.
    # We need to find all pairs at maximum distance.
    
    # BFS from each node is O(N^2) which for N=50000 is too slow.
    # We need a smarter approach.
    
    # Key insight: The maximum distance in a tree is the diameter.
    # We need to count pairs at that distance.
    
    # To count pairs at diameter distance efficiently:
    # Use the fact that all pairs achieving diameter distance can be found
    # by finding all "diameter endpoints".
    
    # Standard approach: 
    # 1. Find diameter length D using two BFS
    # 2. Find all nodes that are endpoints of some diameter path
    # 3. Count pairs among those endpoints that are at distance D
    # But this is still tricky.
    
    # For N<=50000, we can do BFS from O(N) nodes but that's O(N^2).
    # Let's think about the constraint: number of possible cycles < 10^8
    # This suggests the answer count can be large but we just need to compute it.
    
    # Actually for N=50000, O(N^2) might be too slow. But let's check:
    # 50000^2 = 2.5*10^9 operations - too slow.
    
    # Better approach: 
    # The diameter endpoints form two sets. All pairs (u,v) where u is in one 
    # "end" and v is in the other "end" at distance D.
    
    # Use the following: do BFS from arbitrary node, find farthest node u.
    # BFS from u, find distance array dist_u. Diameter D = max(dist_u).
    # BFS from any farthest node v, find dist_v.
    # A pair (a,b) has distance D iff dist_u[a] + dist_u[b] = D (not always true)
    # Actually: dist(a,b) = D iff dist_u[a] + dist_v[b] = D or dist_v[a] + dist_u[b] = D
    # where v is a farthest node from u... This isn't straightforward.
    
    # For this problem size, let's try O(N^2) with BFS but optimized.
    # N=50000 is too large. Let me think differently.
    
    # Actually the problem says N<=50000 but the number of pairs at max distance < 10^8.
    # We need to count pairs (u,v) not adjacent with dist(u,v) = diameter.
    # 
    # Use: do BFS from u (one diameter endpoint), get dist_u.
    # do BFS from v (other diameter endpoint), get dist_v.
    # pair (a,b) is at distance D iff dist_u[a]+dist_u[b]=D AND dist_v[a]+dist_v[b]=D... no.
    # 
    # Correct: dist(a,b) = D iff dist_u[a]+dist_v[b] = D+dist(u,v)... complicated.
    # 
    # Simple correct approach for trees:
    # dist(a,b) = D iff dist_u[a] + dist_u[b] = D where u,v are the two BFS endpoints
    # This is NOT generally true.
    # 
    # Let's just do BFS from all nodes with N<=50000 but use fast BFS.
    # Actually for competitive programming, O(N^2) with N=50000 in Python is too slow.
    # Let me use the two-BFS diameter approach and count via frequency arrays.
    
    def bfs(start):
        dist = [-1] * (N + 1)
        dist[start] = 0
        q = deque([start])
        while q:
            node = q.popleft()
            for nb in adj[node]:
                if dist[nb] == -1:
                    dist[nb] = dist[node] + 1
                    q.append(nb)
        return dist
    
    dist1 = bfs(1)
    far1 = dist1.index(max(dist1[1:]))
    dist_u = bfs(far1)
    D = max(dist_u[1:])
    far2 = dist_u.index(D)
    dist_v = bfs(far2)
    
    # For a tree, dist(a,b) = D (diameter) iff dist_u[a] + dist_v[b] = D + dist_u[far2]
    # Wait, dist_u[far2] = D. dist(a,b) <= D always.
    # dist(a,b) = dist_u[a] + dist_u[b] - 2*dist_u[lca(a,b,rooted at u)]
    # This is complex. Let me use: for trees, 
    # dist(a,b) = D iff dist_u[a] + dist_v[b] = D (since dist(u,v)=D and u,v are diameter ends)
    # Actually this holds! Because dist(a,b) >= |dist_u[a] - dist_u[b]| and 
    # dist(a,b) = dist_u[a] + dist_v[b] when the path a->b goes through the u-v path... not always.
    
    # The correct characterization: in a tree,
    # dist(a,b) = D iff dist_u[a] + dist_v[b] = D OR dist_v[a] + dist_u[b] = D
    # This is also not always correct.
    
    # Let me just verify with examples and use the approach:
    # Count pairs where dist_u[a] + dist_u[b] = D (BFS from one diameter endpoint)
    # This counts pairs at distance D from u... no that's not dist(a,b).
    
    # I'll use a different correct method:
    # dist(a,b) = D iff dist_u[a] + dist_v[b] = D where dist(u,v)=D
    # Proof: dist(a,b) <= D. dist_u[a]+dist_v[b] >= dist(a,b) by triangle... 
    # Actually dist_u[a]+dist_v[b] >= dist(u,v) = D by triangle inequality on trees? No.
    # In trees there's no triangle inequality shortcut issue.
    # dist_u[a] + dist_v[b] >= dist(u,v) = D (triangle: u->a->b->v path length)
    # So dist_u[a]+dist_v[b] >= D always.
    # dist(a,b) = D iff dist_u[a]+dist_v[b] = D (since dist(a,b) <= D and 
    # dist(a,b) = D means a,b are diameter endpoints too, and 
    # dist_u[a]+dist_v[b] = D means the path u->a->b->v has length D meaning a,b are on diameter path)
    # Hmm, this would only count pairs where a is "close to u side" and b is "close to v side".
    
    # Actually the correct statement is:
    # dist(a,b) = D iff dist_u[a] + dist_v[b] = D OR dist_u[b] + dist_v[a] = D
    # But since dist_u[a]+dist_v[b] + dist_u[b]+dist_v[a] >= 2D and both terms >= 0...
    # Let me just verify with test case 1.
    
    # Test 1: N=5, edges: 1-2, 2-4, 4-5, 4-3
    # Tree: 1-2-4-5, 4-3
    # Diameter: longest path. 1-2-4-5 = length 3, 1-2-4-3 = length 3, 3-4-5 = length 2, 5-4-3=2
    # Wait, 1-2-4-5 has 4 nodes, length 3. 1-2-4-3 has 4 nodes, length 3.
    # So diameter D=3, cycle length = D+1 = 4. Answer is 4 with count 2. Matches!
    
    # Pairs at distance 3: (1,5), (1,3). Count=2. But we need to subtract adjacent pairs.
    # (1,5) not adjacent, (1,3) not adjacent. So count=2. Correct!
    
    # Now let's verify the formula dist_u[a]+dist_v[b]=D:
    # u=1 (or 5 or 3), let's say far1 from node 1: dist1 from node 1: 
    # dist[1]=0,dist[2]=1,dist[4]=2,dist[5]=3,dist[3]=3. far1=5 (or 3, first occurrence of 3)
    # Let's say far1=5. dist_u = bfs(5): dist[5]=0,dist[4]=1,dist[2]=2,dist[3]=2,dist[1]=3
    # D=3, far2=1. dist_v = bfs(1): dist[1]=0,dist[2]=1,dist[4]=2,dist[5]=3,dist[3]=3
    
    # Pairs (a,b) with dist_u[a]+dist_v[b]=3:
    # dist_u: 5->0,4->1,2->2,3->2,1->3
    # dist_v: 1->0,2->1,4->2,5->3,3->3
    # dist_u[a]+dist_v[b]=3: 
    # (5,5):0+3=3, (5,3):0+3=3, (4,5):1+3=4 no, (4,2):1+... 
    # Wait I need dist_v[b] where dist_v is from node 1.
    # (a=5,b=5): dist_u[5]+dist_v[5]=0+3=3 ✓ but a=b
    # (a=5,b=3): 0+3=3 ✓
    # (a=4,b=5): 1+3=4 ✗
    # (a=2,b=5): 2+3=5 ✗
    # (a=1,b=1): 3+0=3 ✓ but a=b
    # (a=3,b=5): 2+3=5 ✗
    # Hmm, this doesn't give (1,5) and (1,3).
    
    # Let me try dist_u[a]+dist_v[b]=D OR dist_v[a]+dist_u[b]=D:
    # dist_v[a]+dist_u[b]=3:
    # (a=1,b=5): dist_v[1]+dist_u[5]=0+0=0 ✗
    # (a=5,b=1): dist_v[5]+dist_u[1]=3+3=6 ✗
    # (a=1,b=3): dist_v[1]+dist_u[3]=0+2=2 ✗
    # (a=3,b=1): dist_v[3]+dist_u[1]=3+3=6 ✗
    
    # This approach doesn't work directly. Let me think again.
    
    # The correct approach: dist(a,b) = D iff 
    # dist_u[a] + dist_u[b] = D (where u is one diameter endpoint)
    # NO. dist_u[a]+dist_u[b] is not dist(a,b) in general.
    
    # Actually in a tree, dist(a,b) can be computed as:
    # dist(a,b) = dist_u[a] + dist_u[b] - 2*dist_u[LCA(a,b)]
    # This requires LCA computation.
    
    # For counting pairs at distance exactly D, let me think of a smarter way.
    
    # Alternative: The set of nodes at distance D from u (one diameter endpoint) 
    # are all nodes v such that dist_u[v] = D. These are all "other diameter endpoints".
    # For each such v, dist(u,v)=D. But we need ALL pairs at distance D, not just from u.
    
    # For a tree, the pairs at maximum distance (diameter) can be characterized as follows:
    # Root the tree. The diameter endpoints are nodes with eccentricity = D (where D is diameter).
    # Actually eccentricity = max distance from that node. Nodes with eccentricity = D are 
    # the "peripheral" nodes.
    
    # Hmm, let me think differently. For N<=50000, maybe O(N * diameter) is feasible?
    # Or maybe we can use the following property:
    
    # In a tree, all pairs (a,b) at distance D (diameter) can be found as follows:
    # - Find all nodes at distance D from u (call this set S_u)
    # - Find all nodes at distance D from v (call this set S_v) where v is another diameter endpoint
    # - The pairs at distance D are exactly pairs (a,b) where a ∈ S_v and b ∈ S_u? No...
    
    # Let me just do O(N^2) for small N and see if it passes within time.
    # N=50000, O(N^2) = 2.5*10^9 in Python... definitely too slow.
    
    # Better approach using tree structure:
    # 
    # Key theorem: In a tree, dist(a,b) = D (diameter) if and only if 
    # dist_u[a] + dist_u[b] = D where u is a fixed diameter endpoint.
    # 
    # Wait, is this true? Let me check:
    # u=5 (diameter endpoint), dist_u: 5->0,4->1,2->2,3->2,1->3
    # Pairs with dist_u[a]+dist_u[b]=3 (excluding a=b):
    # (5,1): 0+3=3. dist(5,1)=3 ✓
    # (4,2): 1+2=3. dist(4,2)=1 ✗ 
    # (4,3): 1+2=3. dist(4,3)=1 ✗
    # So this is wrong.
    
    # The correct theorem I recall: 
    # dist(a,b) = D iff dist_u[a] + dist_v[b] = D where u,v are the two endpoints of a fixed diameter.
    # But I showed above this doesn't work either.
    
    # Let me reconsider. In test 1:
    # Diameter path: 1-2-4-5 (length 3) and 1-2-4-3 (length 3)
    # Pairs at distance 3: (1,5) and (1,3).
    # u=5, v=1 (or u=1, v=5 or v=3).
    
    # dist_u (from 5): 5->0, 4->1, 2->2, 3->2, 1->3
    # dist_v (from 1): 1->0, 2->1, 4->2, 5->3, 3->3
    
    # For pair (1,5): dist_u[1]=3, dist_v[5]=3. Sum=6≠3.
    # For pair (1,3): dist_u[1]=3, dist_v[3]=3. Sum=6≠3.
    
    # Hmm. What about dist_u[a] + dist_v[b] = D + dist(u,v)?
    # D + dist(u,v) = 3 + 3 = 6.
    # (1,5): 3+3=6 ✓
    # (1,3): 3+3=6 ✓
    # (5,1): 0+0=0 ✗
    # (4,2): 1+1=2 ✗
    # (4,3): 1+3=4 ✗
    # (2,5): 2+3=5 ✗
    # (2,3): 2+3=5 ✗
    # (3,5): 2+3=5 ✗
    # (5,3): 0+3=3 ✗
    
    # So dist_u[a]+dist_v[b] = 2D works for (1,5) and (1,3) but not symmetric.
    # Also need dist_v[a]+dist_u[b] = 2D:
    # (5,1): dist_v[5]+dist_u[1]=3+3=6 ✓ (same pair as (1,5))
    # (3,1): dist_v[3]+dist_u[1]=3+3=6 ✓ (same pair as (1,3))
    
    # So the condition is: dist_u[a]+dist_v[b]=2D OR dist_v[a]+dist_u[b]=2D
    # But since we're counting unordered pairs, we just need dist_u[a]+dist_v[b]=2D 
    # for ordered pairs and divide by... no, (1,5) gives dist_u[1]+dist_v[5]=3+3=6=2D ✓
    # and (5,1) gives dist_u[5]+dist_v[1]=0+0=0 ✗.
    # So for unordered pairs, we check both orderings.
    
    # But wait, is this formula correct in general?
    # dist(a,b) = D iff dist_u[a]+dist_v[b] = 2D or dist_v[a]+dist_u[b] = 2D?
    # 
    # Hmm, dist_u[a]+dist_v[b] = dist(u,a) + dist(v,b).
    # By triangle: dist(a,b) >= |dist(u,a) - dist(u,b)| (not directly useful)
    # dist(u,v) <= dist(u,a) + dist(a,b) + dist(b,v) = dist_u[a] + dist(a,b) + dist_v[b]
    # So D <= dist_u[a] + dist(a,b) + dist_v[b]
    # => dist(a,b) >= D - dist_u[a] - dist_v[b]
    # Also dist(a,b) <= D (diameter).
    # 
    # dist_u[a] + dist_v[b] >= dist(u,v) = D (by triangle: u->a->b->v)? 
    # No! Triangle inequality in trees: dist(u,v) <= dist(u,a) + dist(a,b) + dist(b,v)
    # but dist(u,a) + dist(a,b) + dist(b,v) >= dist(u,v) only if a,b are on the path.
    # In a tree, dist(u,v) = dist(u,a) + dist(a,v) only if a is on the path u->v.
    # In general, dist(u,a) + dist(a,b) + dist(b,v) >= dist(u,v) always (triangle).
    # So dist_u[a] + dist(a,b) + dist_v[b] >= D.
    # => dist(a,b) >= D - dist_u[a] - dist_v[b].
    # 
    # If dist_u[a] + dist_v[b] = 2D, then dist(a,b) >= D - 2D = -D (trivially true).
    # This doesn't prove dist(a,b) = D.
    
    # I think my formula is wrong. Let me try a completely different approach.
    
    # For N <= 50000, let me think about what's feasible in Python:
    # O(N * sqrt(N)) ~ 50000 * 224 ~ 10^7: feasible
    # O(N log N): feasible
    # O(N^2): not feasible for N=50000
    
    # The key insight for this problem:
    # Adding edge (u,v) creates a cycle of length dist(u,v) + 1.
    # We want to maximize dist(u,v) over all non-adjacent pairs (u,v).
    # The maximum dist(u,v) is the tree diameter D (since we can always find non-adjacent 
    # pairs at distance D for D >= 2, which is always true for N >= 3).
    # Wait, what if the diameter endpoints are adjacent? Then dist=1, but we need dist >= 2 
    # for a meaningful cycle (length >= 3). But diameter >= 2 for N >= 3 (since it's a tree).
    # Actually if diameter = 1, all nodes are connected to one center (star), but then 
    # any two leaves are at distance 2. So the max cycle would be 3.
    # For diameter D, the max cycle is D+1, achieved by non-adjacent pairs at distance D.
    # Are diameter endpoints always non-adjacent? Not necessarily if D=1, but D=1 means N=2 
    # which is excluded (N>=3). For D>=2, diameter endpoints are at distance >= 2, so not adjacent.
    # Actually D could be 2 and the two endpoints could be non-adjacent (distance 2 means 
    # there's one node between them). So yes, for D >= 2, diameter endpoints are non-adjacent.
    
    # So the answer to "max cycle length" is D+1 where D is the diameter.
    # The count is the number of pairs (u,v) with dist(u,v) = D (and u < v, unordered).
    # Since D >= 2, all such pairs are non-adjacent (distance >= 2 > 1).
    # Wait, could dist(u,v) = D = 1? Only if N=2, excluded. So D >= 2 always for N >= 3.
    # Actually for N=3 with a path 1-2-3, D=2. For a star with center 2 and leaves 1,3,4: D=2.
    # So D >= 2 always, and pairs at distance D are non-adjacent. Good.
    
    # Now I need to count pairs at distance exactly D efficiently.
    
    # Approach: Use the "all-pairs distance" via centroid decomposition or other tree techniques.
    # 
    # Centroid decomposition allows counting pairs at distance exactly D in O(N log N).
    
    # Let me implement centroid decomposition to count pairs at distance D.
    
    # Actually, there's a simpler observation:
    # The pairs at distance D are exactly the pairs (a, b) where:
    # dist_u[a] = D and dist_u[b] = 0 (i.e., b = u) -- no, that's just pairs involving u.
    
    # Let me think about the structure of diameter pairs in a tree.
    # 
    # Claim: All nodes that are endpoints of some diameter path form a set S.
    # The pairs at distance D are exactly the pairs (a,b) with a,b ∈ S and dist(a,b) = D.
    # 
    # To find S: a node v is in S iff there exists a node w with dist(v,w) = D.
    # Equivalently, v ∈ S iff dist_u[v] = D or dist_v[v] = D (where u,v are fixed diameter endpoints).
    # Wait, that's not right either.
    
    # Actually: v is a diameter endpoint iff the eccentricity of v equals D.
    # ecc(v) = max_w dist(v,w) = D.
    # 
    # For a tree, ecc(v) = max(dist_u[v], dist_w[v]) where u,w are the two endpoints of 
    # a fixed diameter... this is a known result? Let me think.
    # 
    # Known result: For any node v in a tree, ecc(v) = max(dist_u[v], dist_w[v]) 
    # where u,w are the endpoints of any fixed diameter.
    # This is TRUE! (Standard result in tree algorithms.)
    # 
    # So ecc(v) = D iff max(dist_u[v], dist_w[v]) = D.
    # 
    # Now, the set S of diameter endpoints = {v : ecc(v) = D} = {v : max(dist_u[v], dist_w[v]) = D}.
    
    # But even knowing S, I need to count pairs in S at distance D.
    # |S| could be O(N) and counting pairs in S at distance D is still O(|S|^2) in the worst case.
    
    # Hmm. Let me think about the structure more carefully.
    
    # In a tree, the set of nodes at distance D from a fixed node u forms a set.
    # Let A = {v : dist_u[v] = D} (nodes at max distance from u).
    # Let B = {v : dist_w[v] = D} (nodes at max distance from w, another diameter endpoint).
    # 
    # Pairs at distance D: could be (a,b) with a ∈ A, b ∈ B, or both in A, or both in B.
    
    # This is getting complex. Let me just implement centroid decomposition.
    
    # Centroid decomposition to count pairs at distance exactly D:
    
    # Actually, for this specific problem, let me think about an O(N^2) solution 
    # but with the observation that N <= 50000 might still be too slow in Python.
    # 
    # Wait, let me re-read the constraints: N <= 50000.
    # In Python, O(N^2) with N=50000 is 2.5*10^9 operations - definitely too slow.
    # 
    # But wait - the number of pairs at max distance is < 10^8 (given in constraints).
    # This doesn't help with the algorithm complexity.
    
    # Let me think about a smarter O(N log N) or O(N) approach.
    
    # Key insight for trees:
    # 
    # Root the tree at the center of the diameter path.
    # The diameter endpoints are in different subtrees.
    # 
    # Actually, let me use the following approach:
    # 
    # 1. Find diameter D using two BFS.
    # 2. Find all nodes at distance D from u (call this set A) and from w (call this set B).
    #    where u, w are the two diameter endpoints found.
    # 3. The pairs at distance D are:
    #    - Pairs (a, b) where a ∈ A, b ∈ B, and dist(a,b) = D
    #    - Pairs (a, b) where both in A and dist(a,b) = D
    #    - Pairs (a, b) where both in B and dist(a,b) = D
    # 
    # This still requires computing distances between pairs in A and B.
    
    # Let me look at this from a different angle.
    # 
    # Observation: In a tree, dist(a,b) = D iff 
    # dist_u[a] + dist_u[b] - 2*dist_u[LCA_u(a,b)] = D
    # where LCA_u is the LCA when rooted at u.
    # 
    # This equals D iff dist_u[a] + dist_u[b] - 2*dist_u[LCA_u(a,b)] = D.
    # 
    # Since dist_u[a] <= D and dist_u[b] <= D, and dist_u[LCA] >= 0:
    # For this to equal D, we need dist_u[a] + dist_u[b] to be large and LCA to be close to u.
    
    # I think the most practical approach for this problem in a competition setting 
    # with N <= 50000 is to use BFS from each node but optimize it.
    # In Python, BFS from each node: 50000 * 50000 = 2.5*10^9 - too slow.
    
    # Let me think about the problem differently using the tree's diameter structure.
    
    # IMPORTANT OBSERVATION:
    # In a tree, the pairs (a,b) at distance D (diameter) have a specific structure.
    # 
    # Let's root the tree at any node. For each node v, let depth[v] = dist(root, v).
    # dist(a,b) = depth[a] + depth[b] - 2*depth[LCA(a,b)].
    # 
    # For dist(a,b) = D: depth[a] + depth[b] - 2*depth[LCA(a,b)] = D.
    # 
    # This is maximized when depth[a] + depth[b] is maximized and depth[LCA(a,b)] is minimized.
    # 
    # The maximum of depth[a] + depth[b] - 2*depth[LCA(a,b)] over all pairs is D.
    
    # For counting, I can use the following approach:
    # Root at u (one diameter endpoint). Then depth[v] = dist_u[v].
    # dist(a,b) = dist_u[a] + dist_u[b] - 2*dist_u[LCA(a,b)].
    # = D iff dist_u[a] + dist_u[b] - 2*dist_u[LCA(a,b)] = D.
    # 
    # Since dist_u[a] <= D and dist_u[b] <= D:
    # dist_u[a] + dist_u[b] <= 2D.
    # dist_u[LCA(a,b)] >= 0.
    # So dist(a,b) <= 2D - 0 = 2D, but we know dist(a,b) <= D.
    # 
    # For dist(a,b) = D: dist_u[a] + dist_u[b] - 2*dist_u[LCA] = D.
    # => dist_u[LCA] = (dist_u[a] + dist_u[b] - D) / 2.
    # 
    # This must be a non-negative integer.
    # 
    # Hmm, this is getting complex. Let me just implement a solution that works for 
    # the given constraints using a smarter algorithm.
    
    # FINAL APPROACH: 
    # Use the fact that for counting pairs at distance D in a tree, we can use 
    # the following O(N log N) approach with centroid decomposition.
    # 
    # But implementing centroid decomposition in Python for a competition is complex.
    # Let me think if there's a simpler O(N) or O(N log N) approach specific to 
    # counting pairs at the MAXIMUM distance (diameter).
    
    # SIMPLER APPROACH:
    # 
    # Observation: dist(a,b) = D iff both a and b are "peripheral" nodes AND 
    # they are in different "branches" of the diameter path.
    # 
    # More precisely: Let P = u = p_0, p_1, ..., p_D = w be the diameter path.
    # For each node v, let f(v) = the node on P closest to v (the "foot" of v on P).
    # Let d(v) = dist(v, f(v)) (distance from v to the diameter path).
    # 
    # Then dist(a,b) = d(a) + dist(f(a), f(b)) + d(b).
    # 
    # For dist(a,b) = D: d(a) + dist(f(a), f(b)) + d(b) = D.
    # 
    # Let i = position of f(a) on P (0 to D), j = position of f(b) on P (0 to D).
    # WLOG i <= j. dist(f(a), f(b)) = j - i.
    # 
    # So: d(a) + (j - i) + d(b) = D.
    # => d(a) + d(b) = D - (j - i) = D - j + i.
    # 
    # Also, for a to be a valid node: d(a) + max(i, D-i) <= D (eccentricity constraint? No...)
    # Actually, we need dist(a, u) = d(a) + i <= D and dist(a, w) = d(a) + (D-i) <= D.
    # The second gives d(a) <= i. Similarly d(b) <= D - j.
    # 
    # So: d(a) <= i, d(b) <= D - j, and d(a) + d(b) = D - j + i.
    # => d(a) + d(b) = i + (D - j).
    # Since d(a) <= i and d(b) <= D-j: d(a) + d(b) <= i + (D-j).
    # Combined with d(a) + d(b) = i + (D-j): we need d(a) = i and d(b) = D-j.
    # 
    # So dist(a,b) = D iff d(a) = i (= position of f(a)) and d(b) = D - j (= D - position of f(b)).
    # In other words: dist(a, u) = d(a) + i = 2i = ... wait.
    # 
    # dist(a, u) = dist(a, p_0) = d(a) + i (since f(a) = p_i and dist(p_i, p_0) = i).
    # For d(a) = i: dist(a, u) = 2i. Hmm, that doesn't seem right.
    # 
    # Wait, I think I made an error. Let me redo.
    # dist(a, u) = dist(a, p_0). The path from a to u goes: a -> f(a) = p_i -> p_{i-1} -> ... -> p_0.
    # So dist(a, u) = d(a) + i.
    # For d(a) = i: dist(a, u) = 2i.
    # 
    # dist(a, w) = dist(a, p_D) = d(a) + (D - i) = i + D - i = D.
    # So dist(a, w) = D! This means a is at distance D from w.
    # 
    # Similarly, dist(b, u) = d(b) + j = (D-j) + j = D.
    # So dist(b, u) = D! This means b is at distance D from u.
    # 
    # So the condition dist(a,b) = D is equivalent to:
    # dist(a, w) = D AND dist(b, u) = D.
    # 
    # In other words: a is at distance D from w (i.e., a ∈ A_w = {v : dist_w[v] = D})
    # AND b is at distance D from u (i.e., b ∈ A_u = {v : dist_u[v] = D}).
    # 
    # But wait, this seems to say that ALL pairs (a,b) with a ∈ A_w and b ∈ A_u are at distance D.
    # Is that true? Let me verify with test 1.
    # 
    # u=5, w=1 (or u=1, w=5). Let's use u=5, w=1.
    # dist_u (from 5): 5->0, 4->1, 2->2, 3->2, 1->3. D=3.
    # A_u = {v : dist_u[v] = 3} = {1}.
    # dist_w (from 1): 1->0, 2->1, 4->2, 5->3, 3->3.
    # A_w = {v : dist_w[v] = 3} = {5, 3}.
    # 
    # Pairs (a,b) with a ∈ A_w, b ∈ A_u: (5,1) and (3,1).
    # dist(5,1) = 3 ✓, dist(3,1) = 3 ✓.
    # Count = 2. Correct!
    # 
    # But wait, what about pairs (a,b) with a ∈ A_u, b ∈ A_w? That's the same pairs (unordered).
    # And what about pairs within A_u or within A_w?
    # A_u = {1}, |A_u| = 1, no pairs within.
    # A_w = {5, 3}, dist(5,3) = 2 ≠ 3. So no pairs within A_w at distance D.
    # 
    # So total pairs at distance D = |A_w| * |A_u| - (pairs in A_w ∩ A_u at distance D)?
    # Wait, A_w ∩ A_u = {} in this case.
    # 
    # Hmm, but what if A_w ∩ A_u is non-empty? And what about pairs within A_w or A_u?
    # 
    # Let me re-examine my derivation. I showed:
    # dist(a,b) = D => dist(a,w) = D AND dist(b,u) = D.
    # i.e., a ∈ A_w AND b ∈ A_u.
    # 
    # Conversely, if a ∈ A_w and b ∈ A_u, is dist(a,b) = D?
    # dist(a,w) = D and dist(b,u) = D.
    # dist(a,b) <= D (diameter).
    # dist(a,b) >= dist(a,w) - dist(b,w) = D - dist(b,w).
    # dist(b,w) <= D (diameter), so this gives dist(a,b) >= 0 (not useful).
    # 
    # Hmm, the converse might not hold. Let me think of a counterexample.
    # 
    # Consider a path: 1-2-3-4-5. D=4. u=1, w=5.
    # A_u = {v : dist(1,v) = 4} = {5}.
    # A_w = {v : dist(5,v) = 4} = {1}.
    # Pairs: (1,5). dist(1,5)=4 ✓. Count=1.
    # 
    # Now consider: 1-2-3, 3-4, 3-5. (Star with center 3, plus path 1-2-3.)
    # D = dist(1,4) = dist(1,5) = 3. u=1, w=4 (or 5).
    # dist_u (from 1): 1->0, 2->1, 3->2, 4->3, 5->3.
    # A_u = {4, 5}.
    # dist_w (from 4): 4->0, 3->1, 2->2, 5->2, 1->3.
    # A_w = {1}.
    # Pairs (a ∈ A_w, b ∈ A_u): (1,4) and (1,5).
    # dist(1,4)=3 ✓, dist(1,5)=3 ✓. Count=2.
    # 
    # Are there other pairs at distance 3? dist(4,5)=2, dist(2,4)=2, dist(2,5)=2. No.
    # So count=2 is correct.
    # 
    # Now let me check: is the converse always true?
    # If a ∈ A_w and b ∈ A_u, then dist(a,b) = D?
    # 
    # Proof attempt: 
    # dist(a,b) >= dist(a,u) + dist(b,w) - dist(u,w)? No, triangle inequality doesn't work like that.
    # 
    # Actually: dist(a,b) + dist(u,w) >= dist(a,u) + dist(b,w)? (quadrilateral inequality for trees?)
    # In trees: dist(a,b) + dist(u,w) >= dist(a,u) + dist(b,w) OR dist(a,w) + dist(b,u)?
    # This is the "four-point condition" for trees.
    # 
    # Four-point condition: For any four nodes a,b,u,w in a tree:
    # dist(a,b) + dist(u,w) = max(dist(a,u)+dist(b,w), dist(a,w)+dist(b,u))
    # (the maximum of the three pairwise sums of opposite pairs equals the sum of the other two,
    # and the minimum equals the third... actually the four-point condition states that 
    # among the three sums, the two largest are equal.)
    # 
    # More precisely: dist(a,b)+dist(u,w), dist(a,u)+dist(b,w), dist(a,w)+dist(b,u)
    # The maximum of these three is achieved by at least two of them.
    # 
    # Given dist(a,w) = D and dist(b,u) = D:
    # dist(a,w) + dist(b,u) = 2D.
    # dist(a,b) + dist(u,w) = dist(a,b) + D.
    # dist(a,u) + dist(b,w) = some value.
    # 
    # By four-point condition, the max of {dist(a,b)+D, dist(a,u)+dist(b,w), 2D} is achieved 
    # by at least two values.
    # 
    # Since dist(a,b) <= D: dist(a,b)+D <= 2D.
    # Since dist(a,u) <= D and dist(b,w) <= D: dist(a,u)+dist(b,w) <= 2D.
    # 
    # The maximum is 2D (achieved by dist(a,w)+dist(b,u)).
    # By four-point condition, at least one other sum also equals 2D.
    # 
    # Case 1: dist(a,b)+D = 2D => dist(a,b) = D. ✓
    # Case 2: dist(a,u)+dist(b,w) = 2D => dist(a,u) = D and dist(b,w) = D.
    # 
    # In Case 2, dist(a,b)+D = dist(a,u)+dist(b,w) = 2D => dist(a,b) = D. ✓
    # Wait, by four-point condition, the two largest sums are equal.
    # If 2D is the maximum, then either:
    # - dist(a,b)+D = 2D (so dist(a,b)=D), or
    # - dist(a,u)+dist(b,w) = 2D.
    # But actually the four-point condition says the two LARGEST are equal.
    # So if 2D is the max, then at least one other sum = 2D.
    # 
    # If dist(a,b)+D = 2D: dist(a,b) = D ✓.
    # If dist(a,u)+dist(b,w) = 2D: then dist(a,u)=D and dist(b,w)=D.
    #   Now apply four-point condition to (a,b,u,w) again... we already have dist(a,w)=D, dist(b,u)=D, dist(a,u)=D, dist(b,w)=D.
    #   dist(a,b)+dist(u,w) = dist(a,b)+D.
    #   dist(a,u)+dist(b,w) = 2D.
    #   dist(a,w)+dist(b,u) = 2D.
    #   Max = 2D, achieved by last two. By four-point, the two largest are equal, so dist(a,b)+D could be <= 2D.
    #   But four-point says the two largest are equal, meaning dist(a,b)+D = 2D => dist(a,b)=D.
    #   OR the three sums are all equal (degenerate case).
    # 
    # Hmm, I'm going in circles. Let me just trust the four-point condition:
    # In a tree, for any four nodes, the maximum of the three pairwise sums is achieved by 
    # exactly two of them (or all three if degenerate).
    # 
    # Given dist(a,w)+dist(b,u) = 2D is the maximum:
    # The four-point condition says one of the other two sums also equals 2D.
    # Either dist(a,b)+dist(u,w) = 2D => dist(a,b) = D.
    # Or dist(a,u)+dist(b,w) = 2D.
    # 
    # In the second case, dist(a,u)=D and dist(b,w)=D. Now consider the four-point condition 
    # for (a,b,u,w) with these values:
    # dist(a,b)+D, 2D, 2D. The max is 2D achieved by two sums. The third sum dist(a,b)+D 
    # must be <= 2D. But by four-point, the two largest must be equal. If dist(a,b)+D < 2D, 
    # then the two largest are both 2D, which is fine. But then dist(a,b) < D.
    # 
    # Wait, can this happen? Let me construct a counterexample.
    # 
    # Tree: 1-2-3-4-5 (path). D=4. u=1, w=5.
    # A_w = {v : dist(5,v)=4} = {1}. A_u = {v : dist(1,v)=4} = {5}.
    # Only pair: (1,5). dist(1,5)=4=D ✓.
    # 
    # Tree: star with center c, leaves l1,...,lk. D=2. u=l1, w=l2.
    # A_w = {v : dist(l2,v)=2} = {l1, l3, ..., lk} (all leaves except l2).
    # A_u = {v : dist(l1,v)=2} = {l2, l3, ..., lk} (all leaves except l1).
    # Pairs (a ∈ A_w, b ∈ A_u): a ∈ {l1,...,lk}\{l2}, b ∈ {l2,...,lk}\{l1}.
    # dist(a,b) for a,b both leaves (a≠b): dist = 2 = D ✓.
    # dist(a,b) for a=b: same node, skip.
    # So all pairs (a,b) with a ∈ A_w, b ∈ A_u, a≠b have dist=D=2 ✓.
    # 
    # Let me try to construct a case where a ∈ A_w, b ∈ A_u but dist(a,b) < D.
    # 
    # Tree: 
    #   1-2-3-4-5 (path of length 4, D=4)
    #   3-6 (branch from middle)
    # D is still 4 (path 1-2-3-4-5). u=1, w=5.
    # A_w = {v : dist(5,v)=4} = {1}. A_u = {v : dist(1,v)=4} = {5}.
    # Only pair: (1,5). dist=4 ✓.
    # 
    # Tree:
    #   1-2-3-4-5 (path)
    #   1-6-7-8-9 (another path from 1)
    # D = max path = dist(5,9) = dist(5,1)+dist(1,9) = 4+4 = 8? No wait.
    # dist(5,9): 5-4-3-2-1-6-7-8-9 = 8. D=8. u=5, w=9.
    # A_w = {v : dist(9,v)=8} = {5}. A_u = {v : dist(5,v)=8} = {9}.
    # Only pair: (5,9). dist=8 ✓.
    # 
    # Hmm, I can't seem to construct a counterexample. Let me try harder.
    # 
    # Tree:
    #   Center node c.
    #   Two paths from c: c-a1-a2-a3 (length 3) and c-b1-b2-b3 (length 3).
    #   D = 6 (a3 to b3). u=a3, w=b3.
    #   A_w = {v : dist(b3,v)=6} = {a3}. A_u = {v : dist(a3,v)=6} = {b3}.
    #   Only pair: (a3,b3). dist=6 ✓.
    # 
    # Tree with multiple diameter paths:
    #   1-2-3-4-5 (path)
    #   2-6-7-8 (branch from 2, length 3)
    # dist(1,5)=4, dist(1,8)=4, dist(5,8)=dist(5,4)+dist(4,3)+dist(3,2)+dist(2,6)+dist(6,7)+dist(7,8)=1+1+1+1+1+1=6? 
    # Wait: 5-4-3-2-6-7-8 = 6. D=6. u=5, w=8.
    # A_w = {v : dist(8,v)=6} = {5}. A_u = {v : dist(5,v)=6} = {8}.
    # Only pair: (5,8). dist=6 ✓.
    # 
    # Let me try a tree where there are multiple diameter pairs:
    #   1-3-5 (path)
    #   2-3-4 (path through same center 3)
    #   So: 1-3, 2-3, 3-4, 3-5. Star with 4 leaves? No, 3 has degree 4.
    #   D = 2 (any two leaves). u=1, w=2 (or any two leaves).
    #   A_w = {v : dist(2,v)=2} = {1,4,5}. A_u = {v : dist(1,v)=2} = {2,4,5}.
    #   Pairs (a ∈ A_w, b ∈ A_u, a≠b):
    #   (1,2): dist=2 ✓, (1,4): dist=2 ✓, (1,5): dist=2 ✓,
    #   (4,2): dist=2 ✓, (4,4): same, (4,5): dist=2 ✓,
    #   (5,2): dist=2 ✓, (5,4): dist=2 ✓, (5,5): same.
    #   Unordered pairs: (1,2),(1,4),(1,5),(4,2),(4,5),(5,2) = 6 pairs.
    #   Total pairs at distance 2: C(4,2) = 6 (all pairs of leaves). ✓
    # 
    # Great, so the formula works: count = |A_w| * |A_u| - |A_w ∩ A_u| * (|A_w ∩ A_u| - 1) / 2?
    # No wait. Let me recount.
    # 
    # A_w = {1,4,5}, A_u = {2,4,5}.
    # Pairs (a,b) with a ∈ A_w, b ∈ A_u, a ≠ b (unordered):
    # We need to count unordered pairs {a,b} where a ∈ A_w and b ∈ A_u (or vice versa).
    # 
    # Actually, the condition is: dist(a,b) = D iff a ∈ A_w AND b ∈ A_u (for ordered pair (a,b)).
    # For unordered pairs: {a,b} is a diameter pair iff (a ∈ A_w and b ∈ A_u) or (b ∈ A_w and a ∈ A_u).
    # = (a ∈ A_w and b ∈ A_u) or (a ∈ A_u and b ∈ A_w).
    # = a ∈ A_w ∪ A_u and b ∈ A_w ∪ A_u and (a ∈ A_w iff b ∈ A_u)?
    # 
    # Hmm, let me think about this more carefully.
    # 
    # From my derivation: dist(a,b) = D iff a ∈ A_w AND b ∈ A_u.
    # But this is for ordered pair (a,b). For unordered pair {a,b}:
    # dist(a,b) = D iff (a ∈ A_w and b ∈ A_u) OR (a ∈ A_u and b ∈ A_w).
    # 
    # But dist(a,b) = dist(b,a), so if (a ∈ A_w and b ∈ A_u) then dist(a,b)=D,
    # and also dist(b,a)=D, so (b ∈ A_w and a ∈ A_u) should also hold.
    # 
    # Wait, that means: a ∈ A_w and b ∈ A_u implies b ∈ A_w and a ∈ A_u?
    # In the star example: a=1 ∈ A_w={1,4,5}, b=2 ∈ A_u={2,4,5}.
    # Is b=2 ∈ A_w? A_w = {1,4,5}. 2 ∉ A_w. So NO.
    # 
    # So the condition is NOT symmetric in general. Let me recheck.
    # 
    # For ordered pair (a,b): dist(a,b) = D iff a ∈ A_w AND b ∈ A_u.
    # For ordered pair (b,a): dist(b,a) = D iff b ∈ A_w AND a ∈ A_u.
    # 
    # Since dist(a,b) = dist(b,a), both conditions are equivalent.
    # So: (a ∈ A_w AND b ∈ A_u) iff (b ∈ A_w AND a ∈ A_u).
    # 
    # In the star example: a=1, b=2.
    # (a ∈ A_w AND b ∈ A_u) = (1 ∈ {1,4,5} AND 2 ∈ {2,4,5}) = TRUE.
    # (b ∈ A_w AND a ∈ A_u) = (2 ∈ {1,4,5} AND 1 ∈ {2,4,5}) = FALSE.
    # 
    # But dist(1,2) = 2 = D. So the first condition is TRUE but the second is FALSE.
    # This means my claim "(a ∈ A_w AND b ∈ A_u) iff (b ∈ A_w AND a ∈ A_u)" is WRONG.
    # 
    # So the condition for unordered pair {a,b} to be at distance D is:
    # (a ∈ A_w AND b ∈ A_u) OR (b ∈ A_w AND a ∈ A_u).
    # 
    # And these two conditions are NOT equivalent in general.
    # 
    # So the count of unordered pairs at distance D is:
    # |{(a,b) : a ∈ A_w, b ∈ A_u, a ≠ b}| / 2 + |{(a,b) : a ∈ A_w ∩ A_u, b ∈ A_w ∩ A_u, a ≠ b}| / 2?
    # 
    # No, let me think again. For unordered pairs:
    # Count = |{(a,b) : a < b, (a ∈ A_w and b ∈ A_u) or (b ∈ A_w and a ∈ A_u)}|
    # = |{(a,b) : a < b, a ∈ A_w ∪ A_u, b ∈ A_w ∪ A_u, not (a ∉ A_w and b ∉ A_u) and not (b ∉ A_w and a ∉ A_u)}|
    # 
    # Hmm, let me use inclusion-exclusion.
    # Let X = {(a,b) : a ∈ A_w, b ∈ A_u, a ≠ b} (ordered pairs).
    # Let Y = {(a,b) : b ∈ A_w, a ∈ A_u, a ≠ b} (ordered pairs).
    # 
    # Unordered pairs at distance D = |X ∪ Y| / 2? No, X and Y are ordered pairs.
    # 
    # Actually, for each unordered pair {a,b} at distance D:
    # Either (a ∈ A_w, b ∈ A_u) or (b ∈ A_w, a ∈ A_u) or both.
    # 
    # The ordered pair (a,b) is in X iff a ∈ A_w and b ∈ A_u.
    # The ordered pair (b,a) is in X iff b ∈ A_w and a ∈ A_u.
    # 
    # So the unordered pair {a,b} corresponds to ordered pairs (a,b) and (b,a).
    # {a,b} is at distance D iff (a,b) ∈ X or (b,a) ∈ X.
    # 
    # Count of unordered pairs = (|X| + |X ∩ {(a,b) : (b,a) ∈ X}|) / 2?
    # No...
    # 
    # Let me just count directly:
    # Count = number of unordered pairs {a,b} with a ≠ b such that 
    #         (a ∈ A_w and b ∈ A_u) or (b ∈ A_w and a ∈ A_u).
    # 
    # Let C = A_w ∩ A_u (nodes in both sets).
    # Let P = A_w \ A_u (nodes only in A_w).
    # Let Q = A_u \ A_w (nodes only in A_u).
    # 
    # For unordered pair {a,b}:
    # - a ∈ P, b ∈ Q: (a ∈ A_w, b ∈ A_u) ✓. Condition satisfied.
    # - a ∈ P, b ∈ C: (a ∈ A_w, b ∈ A_u) ✓. Condition satisfied.
    # - a ∈ Q, b ∈ C: (b ∈ A_w, a ∈ A_u) ✓. Condition satisfied.
    # - a ∈ C, b ∈ C: (a ∈ A_w, b ∈ A_u) ✓ and (b ∈ A_w, a ∈ A_u) ✓. Condition satisfied.
    # - a ∈ P, b ∈ P: (a ∈ A_w, b ∉ A_u) and (b ∈ A_w, a ∉ A_u). Condition NOT satisfied.
    # - a ∈ Q, b ∈ Q: (a ∉ A_w, b ∈ A_u) and (b ∉ A_w, a ∈ A_u). Condition NOT satisfied.
    # 
    # Wait, but I need to verify these with the actual distances!
    # 
    # In the star example: A_w = {1,4,5}, A_u = {2,4,5}.
    # P = A_w \ A_u = {1}, Q = A_u \ A_w = {2}, C = A_w ∩ A_u = {4,5}.
    # 
    # Pairs:
    # P×Q: (1,2). dist(1,2)=2=D ✓.
    # P×C: (1,4),(1,5). dist=2=D ✓.
    # Q×C: (2,4),(2,5). dist=2=D ✓.
    # C×C: (4,5). dist=2=D ✓.
    # P×P: {} (only one element in P).
    # Q×Q: {} (only one element in Q).
    # 
    # Total: 1+2+2+1 = 6 = C(4,2) ✓.
    # 
    # But wait, I claimed P×P pairs are NOT at distance D. Let me verify with another example.
    # 
    # Tree: 1-2-3-4-5 (path). D=4. u=1, w=5.
    # A_u = {v : dist(1,v)=4} = {5}. A_w = {v : dist(5,v)=4} = {1}.
    # P = A_w \ A_u = {1}, Q = A_u \ A_w = {5}, C = {}.
    # Pairs: P×Q = (1,5). dist=4 ✓. Count=1 ✓.
    # 
    # Tree: 1-2-3, 3-4, 3-5. D=3. u=1, w=4 (or 5).
    # dist_u (from 1): 1->0, 2->1, 3->2, 4->3, 5->3. A_u = {4,5}.
    # dist_w (from 4): 4->0, 3->1, 2->2, 5->2, 1->3. A_w = {1}.
    # P = {1}, Q = {4,5}, C = {}.
    # Pairs: P×Q = (1,4),(1,5). dist(1,4)=3 ✓, dist(1,5)=3 ✓. Count=2 ✓.
    # 
    # Now let me try a case where C is non-empty and P×P might have pairs at distance D.
    # 
    # Tree: 
    #   1-2-3-4-5 (path)
    #   1-6-7-8-9 (another path from 1)
    # D = dist(5,9) = 4+4 = 8. u=5, w=9.
    # dist_u (from 5): 5->0,4->1,3->2,2->3,1->4,6->5,7->6,8->7,9->8. A_u={9}.
    # dist_w (from 9): 9->0,8->1,7->2,6->3,1->4,2->5,3->6,4->7,5->8. A_w={5}.
    # P={5}, Q={9}, C={}. Count=1 ✓.
    # 
    # Hmm, I can't seem to get C non-empty with P non-empty. Let me think...
    # 
    # For a node v to be in C = A_w ∩ A_u: dist(u,v)=D and dist(w,v)=D.
    # But dist(u,w)=D (diameter). By triangle: dist(u,v)+dist(v,w) >= dist(u,w)=D.
    # dist(u,v)=D and dist(v,w)=D => dist(u,v)+dist(v,w)=2D >= D ✓.
    # But also dist(u,v) <= D and dist(v,w) <= D.
    # 
    # Can dist(u,v)=D and dist(v,w)=D simultaneously? 
    # dist(u,w) <= dist(u,v)+dist(v,w) = 2D. But dist(u,w)=D.
    # This is possible if v is "between" u and w in some sense... but in a tree, 
    # dist(u,w) = D and dist(u,v)+dist(v,w) = 2D means v is NOT on the path u->w 
    # (otherwise dist(u,v)+dist(v,w)=D).
    # 
    # Example: u=1, w=5 in a star with center c and leaves 1,2,3,4,5.
    # D=2. dist(1,v)=2 for v ∈ {2,3,4,5}. dist(5,v)=2 for v ∈ {1,2,3,4}.
    # C = A_u ∩ A_w = {2,3,4}. P = A_w \ A_u = {1}. Q = A_u \ A_w = {5}.
    # 
    # Pairs:
    # P×Q: (1,5). dist=2 ✓.
    # P×C: (1,2),(1,3),(1,4). dist=2 ✓.
    # Q×C: (5,2),(5,3),(5,4). dist=2 ✓.
    # C×C: (2,3),(2,4),(3,4). dist=2 ✓.
    # Total: 1+3+3+3 = 10 = C(5,2) ✓.
    # 
    # Now, P×P: {} (only one element). Q×Q: {} (only one element).
    # C×C: (2,3),(2,4),(3,4). dist=2=D ✓. These are included.
    # 
    # So the formula works! The count of unordered pairs at distance D is:
    # |P|*|Q| + |P|*|C| + |Q|*|C| + C(|C|,2)
    # = |P|*(|Q|+|C|) + |C|*(|Q| + (|C|-1)/2)
    # 
    # Hmm, let me simplify. Let p=|P|, q=|Q|, c=|C|.
    # Count = p*q + p*c + q*c + c*(c-1)/2
    # = p*(q+c) + c*(q + (c-1)/2)
    # = p*|A_u| + c*(q + (c-1)/2)
    # 
    # Alternatively:
    # Count = p*q + p*c + q*c + c*(c-1)/2
    # = p*(q+c) + c*(q+(c-1)/2)
    # 
    # Let me verify: p=1, q=1, c=3 (star with 5 leaves):
    # 1*1 + 1*3 + 1*3 + 3*2/2 = 1+3+3+3 = 10 ✓.
    # 
    # p=1, q=1, c=0 (path 1-2-3-4-5):
    # 1*1 + 0 + 0 + 0 = 1 ✓.
    # 
    # p=1, q=2, c=0 (tree 1-2-3, 3-4, 3-5):
    # 1*2 + 0 + 0 + 0 = 2 ✓.
    # 
    # p=0, q=0, c=4 (star with 4 leaves, u=l1, w=l2):
    # Wait, if u=l1 and w=l2 are both leaves:
    # A_u = {v : dist(l1,v)=2} = all leaves except l1 = {l2,l3,l4}.
    # A_w = {v : dist(l2,v)=2} = all leaves except l2 = {l1,l3,l4}.
    # P = A_w \ A_u = {l1}, Q = A_u \ A_w = {l2}, C = {l3,l4}.
    # p=1, q=1, c=2.
    # Count = 1*1 + 1*2 + 1*2 + 2*1/2 = 1+2+2+1 = 6 = C(4,2) ✓.
    # 
    # Great! So the formula is:
    # Count = p*q + p*c + q*c + c*(c-1)//2
    # where p = |A_w \ A_u|, q = |A_u \ A_w|, c = |A_u ∩ A_w|.
    # 
    # But wait, I need to verify that ALL pairs in P×P and Q×Q are NOT at distance D.
    # 
    # For a,b ∈ P = A_w \ A_u: dist(a,w)=D and dist(b,w)=D, but dist(a,u)<D and dist(b,u)<D.
    # dist(a,b) <= D. Is dist(a,b) = D possible?
    # 
    # If dist(a,b) = D, then by my earlier derivation, a ∈ A_w' and b ∈ A_u' for some 
    # diameter endpoints u', w'. But u and w are THE diameter endpoints (found by BFS).
    # 
    # Hmm, but there might be multiple diameter paths. Let me think of a case where 
    # two nodes in P are at distance D.
    # 
    # Tree: 
    #   1-2-3-4-5 (path, D=4)
    #   5-6-7-8-9 (extending from 5)
    # D = dist(1,9) = 4+4 = 8. u=1, w=9.
    # A_u = {v : dist(1,v)=8} = {9}. A_w = {v : dist(9,v)=8} = {1}.
    # P = {1}, Q = {9}, C = {}. Count = 1 ✓.
    # 
    # Tree with two "branches" of equal length from a center:
    #   Center c. Two paths: c-a1-a2-a3 and c-b1-b2-b3. D=6. u=a3, w=b3.
    #   A_u = {b3}. A_w = {a3}. P={a3}, Q={b3}, C={}. Count=1 ✓.
    # 
    # Tree with three branches of equal length:
    #   Center c. Three paths: c-a1-a2-a3, c-b1-b2-b3, c-d1-d2-d3. D=6.
    #   u=a3, w=b3 (one diameter pair).
    #   A_u = {v : dist(a3,v)=6} = {b3, d3}. A_w = {v : dist(b3,v)=6} = {a3, d3}.
    #   P = A_w \ A_u = {a3}, Q = A_u \ A_w = {b3}, C = {d3}.
    #   Count = 1*1 + 1*1 + 1*1 + 0 = 3.
    #   Actual pairs at distance 6: (a3,b3), (a3,d3), (b3,d3). Count=3 ✓.
    # 
    # Now, are there pairs in P×P or Q×Q at distance D?
    # P = {a3}, Q = {b3}. Only one element each, so no pairs.
    # 
    # Let me try to construct a case with |P| >= 2.
    # 
    # Tree: 
    #   Center c. 
    #   Path c-a1-a2-a3 (length 3).
    #   Path c-b1-b2-b3 (length 3).
    #   Path c-d1-d2-d3 (length 3).
    #   Additional node: a3-e (so a3 has a leaf e).
    # D = dist(e, b3) = dist(e,a3)+dist(a3,c)+dist(c,b3) = 1+3+3 = 7.
    # u=e, w=b3.
    # A_u = {v : dist(e,v)=7} = {b3}. A_w = {v : dist(b3,v)=7} = {e}.
    # P={e}, Q={b3}, C={}. Count=1.
    # But dist(e,d3) = 1+3+3 = 7 = D? Yes! So (e,d3) is also a diameter pair.
    # But A_u = {b3} doesn't include d3. Something is wrong.
    # 
    # Oh wait, dist(e,d3) = 7 = D. So d3 should be in A_u = {v : dist(e,v)=7}.
    # Let me recompute: dist(e,b3) = 1+3+3=7, dist(e,d3) = 1+3+3=7. So A_u = {b3, d3}.
    # And dist(b3,e) = 7, dist(b3,a3) = 3+3=6 < 7, dist(b3,d3) = 3+3=6 < 7.
    # A_w = {v : dist(b3,v)=7} = {e}.
    # P = A_w \ A_u = {e}, Q = A_u \ A_w = {b3, d3}, C = {}.
    # Count = 1*2 + 0 + 0 + 0 = 2.
    # Actual pairs at distance 7: (e,b3) and (e,d3). Count=2 ✓.
    # 
    # Hmm, still no P×P pairs. Let me try harder.
    # 
    # Tree:
    #   1-2-3-4-5 (path)
    #   1-6-7-8-9 (path from 1)
    #   5-10-11-12-13 (path from 5)
    # D = dist(9,13) = dist(9,1)+dist(1,5)+dist(5,13) = 4+4+4 = 12.
    # u=9, w=13.
    # A_u = {v : dist(9,v)=12} = {13}. A_w = {v : dist(13,v)=12} = {9}.
    # P={9}, Q={13}, C={}. Count=1.
    # But dist(9,5) = 4+4=8 < 12. dist(1,13) = 4+4=8 < 12. So only (9,13) at distance 12. ✓
    # 
    # I'm having trouble constructing a case with |P| >= 2. Let me think theoretically.
    # 
    # For a,b ∈ P = A_w \ A_u: dist(a,w)=D and dist(b,w)=D, dist(a,u)<D, dist(b,u)<D.
    # Can dist(a,b) = D?
    # 
    # By four-point condition on (a,b,u,w):
    # The three sums: dist(a,b)+dist(u,w), dist(a,u)+dist(b,w), dist(a,w)+dist(b,u).
    # = dist(a,b)+D, dist(a,u)+D, D+dist(b,u).
    # 
    # The max of these three is achieved by at least two.
    # dist(a,u) < D and dist(b,u) < D, so dist(a,u)+D < 2D and D+dist(b,u) < 2D.
    # dist(a,b) <= D, so dist(a,b)+D <= 2D.
    # 
    # The maximum is at most 2D. For dist(a,b)=D: dist(a,b)+D = 2D.
    # For this to be the max, we need dist(a,u)+D <= 2D (true) and D+dist(b,u) <= 2D (true).
    # But by four-point, the max must be achieved by at least two sums.
    # If dist(a,b)+D = 2D is the max, then at least one of dist(a,u)+D or D+dist(b,u) = 2D.
    # But dist(a,u) < D and dist(b,u) < D, so neither can equal 2D.
    # Contradiction! So dist(a,b) < D for a,b ∈ P.
    # 
    # GREAT! So pairs in P×P and Q×Q are NEVER at distance D.
    # 
    # Therefore, the count formula is:
    # Count = p*q + p*c + q*c + c*(c-1)//2
    # where p = |A_w \ A_u|, q = |A_u \ A_w|, c = |A_u ∩ A_w|.
    # 
    # This can be simplified:
    # Count = p*q + (p+q)*c + c*(c-1)//2
    # = p*q + c*(p+q) + c*(c-1)//2
    # = p*q + c*(p+q+(c-1)/2)
    # 
    # Or: Let a = |A_u|, b = |A_w|.
    # p = b - c, q = a - c.
    # Count = (b-c)*(a-c) + (b-c)*c + (a-c)*c + c*(c-1)//2
    # = (b-c)*(a-c+c) + (a-c)*c + c*(c-1)//2
    # = (b-c)*a + c*(a-c) + c*(c-1)//2
    # = a*b - a*c + a*c - c^2 + c*(c-1)//2
    # = a*b - c^2 + c*(c-1)//2
    # = a*b - c*(c+1)//2
    # 
    # Wait: -c^2 + c*(c-1)/2 = c*(-c + (c-1)/2) = c*(-c/2 - 1/2) = -c*(c+1)/2.
    # So Count = a*b - c*(c+1)//2.
    # 
    # Let me verify:
    # Star with 5 leaves, u=l1, w=l2: a=|A_u|=3, b=|A_w|=3, c=|C|=2.
    # Count = 3*3 - 2*3//2 = 9 - 3 = 6 ✓.
    # 
    # Three branches of length 3, u=a3, w=b3: a=2, b=2, c=1.
    # Count = 2*2 - 1*2//2 = 4 - 1 = 3 ✓.
    # 
    # Test 1: a=|A_u|=1 (A_u={1}), b=|A_w|=2 (A_w={5,3}), c=0.
    # Count = 1*2 - 0 = 2 ✓.
    # 
    # Test 2: Let me compute.
    # Tree: 1-2, 2-3, 3-4, 3-6, 5-3, 1-8, 1-7.
    # Edges: 1-2, 2-3, 3-4, 3-6, 3-5, 1-8, 1-7.
    # Adjacency: 1:[2,8,7], 2:[1,3], 3:[2,4,6,5], 4:[3], 5:[3], 6:[3], 7:[1], 8:[1].
    # 
    # BFS from 1: dist[1]=0,dist[2]=1,dist[8]=1,dist[7]=1,dist[3]=2,dist[4]=3,dist[6]=3,dist[5]=3.
    # Farthest from 1: nodes 4,6,5 at distance 3. far1 = 4 (first occurrence).
    # 
    # BFS from 4: dist[4]=0,dist[3]=1,dist[2]=2,dist[6]=2,dist[5]=2,dist[1]=3,dist[8]=4,dist[7]=4.
    # D=4. far2=8 (or 7, first occurrence of 4). Let's say far2=8.
    # 
    # A_u = {v : dist_u[v]=4} = {8,7} (dist from 4: 8->4, 7->4).
    # 
    # BFS from 8: dist[8]=0,dist[1]=1,dist[2]=2,dist[7]=2,dist[3]=3,dist[4]=4,dist[6]=4,dist[5]=4.
    # A_w = {v : dist_w[v]=4} = {4,6,5}.
    # 
    # a=|A_u|=2, b=|A_w|=3, c=|A_u ∩ A_w|=0.
    # Count = 2*3 - 0 = 6 ✓ (expected output is 6).
    # 
    # PERFECT! The formula works.
    # 
    # So the algorithm is:
    # 1. BFS from node 1 to find farthest node u.
    # 2. BFS from u to find distances dist_u. D = max(dist_u). Find farthest node w.
    # 3. BFS from w to find distances dist_w.
    # 4. A_u = {v : dist_u[v] = D}, A_w = {v : dist_w[v] = D}.
    # 5. a = |A_u|, b = |A_w|, c = |A_u ∩ A_w|.
    # 6. Count = a*b - c*(c+1)//2.
    # 7. Output D+1 and Count.
    # 
    # Wait, but I need to be careful: the formula Count = a*b - c*(c+1)//2 counts 
    # ORDERED pairs divided by... no, let me recheck.
    # 
    # From my derivation: unordered pair {a,b} is at distance D iff 
    # (a ∈ A_w and b ∈ A_u) or (b ∈ A_w and a ∈ A_u).
    # 
    # Count of unordered pairs = p*q + p*c + q*c + c*(c-1)//2 = a*b - c*(c+1)//2.
    # 
    # Let me re-derive this more carefully.
    # 
    # Unordered pairs {a,b} (a≠b) at distance D:
    # Case 1: a ∈ P, b ∈ Q (or a ∈ Q, b ∈ P): p*q pairs.
    # Case 2: a ∈ P, b ∈ C (or a ∈ C, b ∈ P): p*c pairs.
    # Case 3: a ∈ Q, b ∈ C (or a ∈ C, b ∈ Q): q*c pairs.
    # Case 4: a ∈ C, b ∈ C: c*(c-1)//2 pairs.
    # 
    # Total = p*q + p*c + q*c + c*(c-1)//2.
    # 
    # With p = b-c, q = a-c:
    # = (b-c)*(a-c) + (b-c)*c + (a-c)*c + c*(c-1)//2
    # = (b-c)*a + (a-c)*c + c*(c-1)//2  [since (b-c)*(a-c) + (b-c)*c = (b-c)*a]
    # = a*b - a*c + a*c - c^2 + c*(c-1)//2
    # = a*b - c^2 + c*(c-1)//2
    # = a*b - c*(2c - c + 1)//2  [hmm let me redo]
    # = a*b + c*(-c + (c-1)/2)
    # = a*b + c*(-(c+1)/2)
    # = a*b - c*(c+1)//2.
    # 
    # ✓ (assuming c*(c+1) is always even, which it is since one of c, c+1 is even).
    # 
    # So the final formula is: Count = a*b - c*(c+1)//2.
    # 
    # But wait, I need to double-check that I'm not double-counting.
    # For unordered pair {a,b} with a ∈ P, b ∈ Q: this is counted once in p*q.
    # For unordered pair {a,b} with a ∈ P, b ∈ C: counted once in p*c.
    # For unordered pair {a,b} with a ∈ C, b ∈ Q: counted once in q*c.
    # For unordered pair {a,b} with a,b ∈ C: counted once in c*(c-1)//2.
    # 
    # These cases are mutually exclusive and cover all pairs at distance D. ✓
    # 
    # Also, I need to verify that pairs in P×P and Q×Q are indeed NOT at distance D.
    # I proved this above using the four-point condition. ✓
    # 
    # And I need to verify that ALL pairs in the above cases ARE at distance D.
    # I proved this above (the condition dist(a,b)=D iff a ∈ A_w and b ∈ A_u). ✓
    # 
    # One more thing: I need to make sure that the pairs are non-adjacent (since we're 
    # adding a new tunnel). But since D >= 2 (for N >= 3), all pairs at distance D are 
    # non-adjacent (distance >= 2 > 1). ✓
    # 
    # Actually wait - could D = 1? Only if the tree has diameter 1, meaning all nodes are 
    # connected to a single center (star) with N=2. But N >= 3, so D >= 2. ✓
    # 
    # Actually for N=3 with a path 1-2-3: D=2. Pairs at distance 2: (1,3). Count=1.
    # For N=3 with a star (1-2, 1-3): D=2. Pairs at distance 2: (2,3). Count=1.
    # Both give cycle length 3 with count 1. Makes sense.
    # 
    # ALGORITHM SUMMARY:
    # 1. BFS from node 1 -> find u (farthest node).
    # 2. BFS from u -> find D (diameter) and w (farthest node from u).
    # 3. BFS from w -> find dist_w.
    # 4. A_u = set of nodes at distance D from u.
    # 5. A_w = set of nodes at distance D from w.
    # 6. a = |A_u|, b = |A_w|, c = |A_u ∩ A_w|.
    # 7. Count = a*b - c*(c+1)//2.
    # 8. Output D+1 and Count.
    # 
    # Time complexity: O(N) for three BFS passes. ✓
    
    # Compute A_u and A_w as sets
    A_u_set = set(v for v in range(1, N+1) if dist_u[v] == D)
    A_w_set = set(v for v in range(1, N+1) if dist_v[v] == D)
    
    a = len(A_u_set)
    b = len(A_w_set)
    c = len(A_u_set & A_w_set)
    
    count = a * b - c * (c + 1) // 2
    
    print(D + 1)
    print(count)

solve()