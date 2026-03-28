Looking at this problem carefully:

We need to find the longest path starting from each node C, where the path P = P1, P2, ..., PK satisfies:
- Odd-indexed elements (P1, P3, P5, ...) are strictly increasing
- Even-indexed elements (P2, P4, P6, ...) are strictly increasing

So from position i in the path, we move to position i+1, and:
- If we're at an odd position (1-indexed), the next odd position element must be larger
- If we're at an even position, the next even position element must be larger

State: dp[v][parity] = longest path ending at node v, where parity indicates if v is at an odd (0) or even (1) position.

Transition: For edge (v, u):
- If v is at odd position (parity=0), u goes to even position (parity=1). No constraint on u relative to v for this step (u can be anything). But the NEXT odd element after u must be > v.
- Actually the constraint is: odd subsequence is increasing, even subsequence is increasing.

So dp[v][0] = longest path where v is at an odd position, with last_odd = v, last_even = whatever came before.

We need: dp[v][p] where p=0 means v is at odd position, p=1 means v is at even position.

Transition from (v, 0) to (u, 1): u can be any neighbor of v, no constraint (u is the first even element or next even > previous even). But we need to track last_even too...

This requires tracking both last_odd and last_even values. State = (last_odd, last_even) which is too large.

Key insight: dp[v][0] = max path length where v is the current node at an odd position (last odd = v). The last even element is implicit - we need it for future transitions.

Let me reconsider: dp[v][p] = longest path ending at v with parity p, where:
- If p=0 (odd position): the constraint for extending is that the next even neighbor u can be anything, but then from u we need next odd > v.
- If p=1 (even position): extending to odd neighbor u requires u > last_odd.

We need to track last_odd when at even position. So state is (v, last_odd) for even positions - too large.

Alternative: dp[v][0] = best path ending at v at odd position. dp[v][1][last_odd] - too large.

Let me think differently. dp[v][0] = longest path ending at v (odd pos). dp[v][1] = longest path ending at v (even pos), where the preceding odd element is... we need it.

Actually: from (u, even, last_odd=w) we go to (v, odd) if v > w. So dp[v][0] = max over neighbors u of v where v > w: dp[u][1 with last_odd=w] + 1.

This seems like we need: for each node u at even position, for each possible last_odd w that's a neighbor of v (v > w), dp[u][1] + 1.

Let me define: f[v][0] = longest path ending at v at odd position. f[v][1] = longest path ending at v at even position, where the last odd node before v is tracked implicitly.

After more analysis, I'll use topological-sort-like DP on a DAG formed by the constraints, processing nodes in order.

```python
import sys
from collections import defaultdict

def solve():
    input_data = sys.stdin.buffer.read().split()
    idx = 0
    N = int(input_data[idx]); idx+=1
    M = int(input_data[idx]); idx+=1
    
    adj = [[] for _ in range(N+1)]
    for _ in range(M):
        a = int(input_data[idx]); idx+=1
        b = int(input_data[idx]); idx+=1
        adj[a].append(b)
        adj[b].append(a)
    
    # dp[v][0] = best path length ending at v at odd position
    # dp[v][1] = best path length ending at v at even position
    # For transition: (v,0)->(u,1): no value constraint needed now
    # (u,1)->(v,0): need v > last_odd. last_odd is the node before u.
    # We store dp2[u][w] = best path ending at u(even) with last_odd=w
    # Too expensive. Use dp[v][0] and for each edge process carefully.
    
    dp0 = [1]*(N+1)  # odd position
    dp1 = [0]*(N+1)  # even position
    
    # Process in increasing order for odd positions
    for v in range(1, N+1):
        for u in adj[v]:
            # v at odd, u at even
            if dp1[u] < dp0[v] + 1:
                dp1[u] = dp0[v] + 1
            # u at even, v at odd (v > last_odd needed)
            # need last_odd < v
    
    print(*[max(dp0[i], dp1[i]) for i in range(1, N+1)])

solve()
```

After deeper analysis, I'll implement a proper DP with sorting:

```python
import sys

def solve():
    data = sys.stdin.buffer.read().split()
    idx = 0
    N = int(data[idx]); idx+=1
    M = int(data[idx]); idx+=1
    adj = [[] for _ in range(N+1)]
    for _ in range(M):
        a = int(data[idx]); idx+=1
        b = int(data[idx]); idx+=1
        adj[a].append(b)
        adj[b].append(a)
    
    INF = float('inf')
    # dp[v][0]: longest path ending at v, v is at odd position
    # dp[v][1]: longest path ending at v, v is at even position
    # Transition (u even) -> (v odd): requires v > prev_odd
    # We need: best[u][1] where prev_odd < v, for each neighbor u of v
    # Store for each node u at even: dict of prev_odd -> best length
    # Too memory intensive
    
    # Key insight: process nodes by value
    # dp0[v] = longest path ending at v (odd pos)
    # dp1[v] = longest path ending at v (even pos), keyed by prev_odd
    # For dp0[v]: v came from some u (even pos) where prev_odd < v
    #   dp0[v] = max over neighbors u: max over w<v of dp1_w[u] + 1
    # For dp1[u]: u came from v (odd pos)
    #   dp1[u][prev_odd=v] = dp0[v] + 1
    
    # So dp1[u] stores: for each possible prev_odd w, best path = dp0[w]+1
    # dp0[v] = max over neighbors u of v: max(dp1[u][w] for w < v) + 1... wait
    # dp1[u][w] = dp0[w] + 1, so dp0[v] = max over neighbors u, neighbors w of u where w<v: dp0[w] + 2
    
    # dp0[v] = 1 + max over u in adj[v], w in adj[u] where w < v: dp0[w] + 1
    # dp0[v] = max(1, max_{u in adj[v], w in adj[u], w<v} dp0[w] + 2)
    
    # Process v in increasing order!
    # For each v (odd pos), dp0[v] = max(1, max over 2-hop neighbors w < v: dp0[w] + 2)
    # Answer for node i = max(dp0[i], max over neighbors u: dp0[i]+1 if we consider i at odd going to u at even)
    # Actually answer[i] = max path starting at i
    
    # Wait, the path starts at i. i is P1 (odd position, value i).
    # So answer[i] = dp0[i] if we define dp0[i] as longest path where i is the FIRST element... no.
    
    # Let me redefine: dp0[v] = longest path ending at v at odd position (v = last odd element)
    # The path can start anywhere.
    # Process in increasing order of v:
    # dp0[v] = max(1, max_{u in adj[v], w in adj[u], w < v} (dp0[w] + 2))
    
    dp0 = [1] * (N + 1)
    
    # For efficiency, for each node u, maintain a sorted structure of (w, dp0[w]) for w in adj[u]
    # When processing v, for each u in adj[v], query max dp0[w] for w in adj[u] with w < v
    
    # This is O(M * sqrt(M)) or we need segment tree / BIT
    # For each u, we need prefix max of dp0[w] for w < v among adj[u]
    # Since we process v in order 1..N, and for each u we want max dp0[w] for w already processed (w<v) in adj[u]
    # We can maintain for each u: a variable best1[u] = max dp0[w] for w in adj[u] processed so far
    
    best1 = [0] * (N + 1)  # max dp0[w] for w in adj[u], w < current v
    
    order = list(range(1, N + 1))  # already sorted
    
    for v in order:
        # dp0[v] = max(1, max over u in adj[v]: best1[u] + 2)
        val = 1
        for u in adj[v]:
            if best1[u] + 2 > val:
                val = best1[u] + 2
        dp0[v] = val
        # Update best1 for all neighbors u of v: best1[u] = max(best1[u], dp0[v])
        for u in adj[v]:
            if dp0[v] > best1[u]:
                best1[u] = dp0[v]
    
    # Now dp0[v] = longest path ending at v at odd position
    # Answer for starting node i:
    # If i starts at odd position: we want longest path starting at i
    # dp0 gives longest path ENDING at v... we need longest path STARTING at i
    
    # Hmm, the path is directional in terms of values but the graph is undirected.
    # The odd subsequence must be increasing, even subsequence must be increasing.
    # So if path is P1,P2,...,PK: P1<P3<P5<... and P2<P4<P6<...
    # The path can go in any direction on the graph.
    
    # dp0[v] as defined: longest path where v is the last odd-positioned element.
    # The answer for starting node i is NOT simply dp0[i].
    
    # We need: for each starting node i, the longest valid path starting at i.
    # i is P1 (odd position). 
    
    # Let's define:
    # f[v][0] = longest path starting at v, where v is at odd position (going forward)
    # f[v][1] = longest path starting at v, where v is at even position
    
    # f[v][0] = 1 + max over u in adj[v]: f[u][1] where... 
    # When v is at odd pos and we extend to u (even pos), then from u we go to w (odd pos) requiring w > v.
    # f[u][1 given prev_odd=v] = 1 + max over w in adj[u], w > v: f[w][0 given prev_odd constraint]
    # But f[w][0] doesn't depend on prev_odd since odd subsequence just needs to be increasing and w > v is the constraint.
    
    # Actually f[w][0] starting fresh: the constraint is just that future odd elements > w, future even elements > (first even element).
    # The "prev_odd" when at even position matters for the next odd step.
    
    # This is getting complex. Let me think again.
    
    # State for forward DP: (current_node, parity, last_odd_value, last_even_value)
    # Too many states.
    
    # But notice: when at odd position with value v, the constraint for next odd is > v (independent of even).
    # When at even position with value u, the constraint for next even is > u (independent of odd).
    # The two subsequences are independent constraints!
    
    # So state = (current_node, parity, last_value_of_same_parity_subsequence)
    # = (v, p, last_p) where last_p is the last value in the p-subsequence
    
    # For p=0 (odd): last_0 = v (since v is the current odd element)
    # For p=1 (even): last_1 = v, and we need to know last_0 to constrain next odd step
    
    # Hmm, when at even position v, to go to odd position w, we need w > last_odd.
    # last_odd is NOT v, it's the previous odd element.
    
    # So state must include both last_odd and last_even. That's O(N^2) states.
    
    # Unless... we can decouple them somehow.
    
    # Let's define:
    # g[v][0] = longest path ending at v (odd pos), where we only care about v as last_odd
    # g[v][1] = longest path ending at v (even pos), where we only care about v as last_even
    # But transition from even to odd needs last_odd, not last_even.
    
    # Alternative formulation:
    # dp[v][0] = longest path ending at v at odd position (v is last odd)
    # dp[v][1] = longest path ending at v at even position, AND we store the "best" over all possible last_odd values
    
    # For transition (v even) -> (w odd, w > last_odd):
    # We need: for node v at even position, what's the best dp value for each possible last_odd?
    # dp1[v][last_odd] = length of best path ending at v (even) with last_odd = last_odd
    
    # dp0[w] = max over v in adj[w], last_odd < w: dp1[v][last_odd] + 1
    # dp1[v][u] = dp0[u] + 1 for u in adj[v] (u was the previous odd node)
    
    # So dp0[w] = max over v in adj[w], u in adj[v], u < w: dp0[u] + 2
    # This is the same recurrence as before! And it's correct.
    
    # dp0[w] = max(1, max_{v in adj[w], u in adj[v], u<w} dp0[u] + 2)
    
    # And the answer for starting node i:
    # i starts at odd position. The path starting at i has i as P1.
    # We want longest path where i is the FIRST element (odd pos).
    # 
    # By symmetry (reversing the path): if P = P1,...,PK is valid,
    # then reversed path PK,...,P1 has odd positions at PK, P(K-2),... and even at P(K-1),...
    # The reversed path's odd subsequence = PK, P(K-2),... which must be increasing.
    # Original odd subseq P1,P3,... increasing means reversed even subseq is increasing (if K odd).
    # Not a clean symmetry.
    
    # Let me define forward DP:
    # h[v][0] = longest path starting at v, v at odd position, with v as the "last odd so far" (= first odd = v)
    # h[v][1] = longest path starting at v, v at even position... but we need last_odd
    
    # Process in DECREASING order:
    # h[v][0] = 1 + max over u in adj[v]: h_after[u][1 with last_odd=v]
    # h_after[u][1 with last_odd=v] = 1 + max over w in adj[u], w > v: h[w][0]
    # So h[v][0] = 1 + max over u in adj[v]: (1 + max over w in adj[u], w>v: h[w][0])
    #            = max(1, max_{u in adj[v], w in adj[u], w>v} h[w][0] + 2)
    
    # Process in DECREASING order of v:
    # h[v][0] = max(1, max_{u in adj[v], w in adj[u], w>v} h[w][0] + 2)
    
    # Maintain best2[u] = max h[w][0] for w in adj[u], w > v (processed so far in decreasing order)
    
    # Answer for node i = h[i][0] (i starts at odd position, which is always the case since i=P1)
    # But wait, can the path have length 1? Yes, trivially. h[i][0] >= 1.
    # Also, can we extend by just one step? h[i][0] could be 2 if we go i -> u (u at even pos, length 2).
    # But h[i][0] as defined only counts paths where we go odd->even->odd->...
    # A path of length 2 is i, u where i is odd, u is even. That's valid (odd subseq = {i}, even subseq = {u}, both trivially increasing).
    # h[i][0] = max(1, max_{u in adj[i], w in adj[u], w>i} h[w][0] + 2)
    # This gives minimum 1, but misses paths of even length ending at even position!
    
    # For path of length 2: i -> u. This has length 2. h[i][0] would be 1 unless there's a w.
    # We need to also consider: answer[i] = max(h[i][0], 1 + max_{u in adj[i]} 1) = max(h[i][0], 2) if adj[i] non-empty.
    # More generally: answer[i] = max over all valid paths starting at i.
    
    # A path starting at i: i(odd), u(even), v(odd, v>i), w(even, w>u), ...
    # Length 1: just i. Length 2: i,u. Length 3: i,u,v (v>i). Length 4: i,u,v,w (v>i, w>u). Etc.
    
    # h[i][0] captures odd-length paths (ending at odd pos).
    # For even-length paths: i(odd)->u(even)->...->z(even)
    # Define h[i][0] = longest odd-length path starting at i (odd pos)
    # Define e[i] = longest even-length path starting at i
    # e[i] = 1 + max_{u in adj[i]}: (longest path starting at u at even pos with last_odd=i)
    # = 1 + max_{u in adj[i]}: f[u][i] where f[u][last_odd] = longest path from u at even pos
    # f[u][last_odd] = 1 + max_{w in adj[u], w > last_odd}: h[w][0]... 
    # Hmm, h[w][0] is longest odd-length path from w at odd pos. But after w we continue with even constraint > u.
    
    # This is getting complicated. Let me redefine more carefully.
    
    # State: (node, parity, last_odd, last_even) - too large
    # 
    # Observation: The two constraints (odd subseq increasing, even subseq increasing) are coupled only through the path structure.
    # 
    # Let's define:
    # dp[v][0] = longest path ending at v, v at odd position (last odd = v, last even = anything)
    # dp[v][1][u] = longest path ending at v, v at even position, last odd = u
    # 
    # Transition:
    # dp[v][0] = max(1, max_{w in adj[v], u in adj[w], u < v} dp[w][1][u] + 1)
    #           = max(1, max_{w in adj[v], u in adj[w], u < v} (dp[u][0] + 1) + 1)  [since dp[w][1][u] = dp[u][0]+1]
    #           = max(1, max_{w in adj[v], u in adj[w], u < v} dp[u][0] + 2)
    # 
    # This confirms the recurrence. Process in increasing order of v.
    # 
    # For the answer (forward paths):
    # Define fwd[v][0] = longest path starting at v, v at odd position
    # fwd[v][0] = max(1, max_{w in adj[v], u in adj[w], u > v} fwd[u][0] + 2)
    # Process in decreasing order of v.
    # 
    # But this only gives odd-length paths. For even-length:
    # fwd_even[v] = longest even-length path starting at v (v at odd pos, path ends at even pos)
    # fwd_even[v] = 1 + max_{u in adj[v]}: (1 + max_{w in adj[u], w > v}: fwd[w][0] - 1 + 1)
    # Hmm, not clean.
    
    # Actually let me reconsider. fwd[v][0] as defined:
    # Path: v(odd), a(even), b(odd, b>v), c(even, c>a), d(odd, d>b), ...
    # This is an odd-length path.
    # 
    # fwd[v][0] = max(1, max_{a in adj[v], b in adj[a], b>v} (2 + fwd[b][0] - 1))
    # Wait: if we go v->a->b->..., the subpath from b has b at odd pos with constraint b>v already satisfied.
    # But fwd[b][0] is the longest path starting at b with b at odd pos, no constraint on b's value relative to anything.
    # The constraint b>v is already encoded in the selection.
    # After b, the path continues: b(odd)->c(even)->d(odd, d>b)->...
    # fwd[b][0] correctly captures this.
    # So: fwd[v][0] = max(1, max_{a in adj[v], b in adj[a], b>v} fwd[b][0] + 2)
    # 
    # For even-length paths starting at v:
    # v(odd)->a(even)->b(odd,b>v)->c(even,c>a)->...->z(even)
    # = 1 + (path starting at a, a at even, last_odd=v)
    # Define fwd1[a][v] = longest path starting at a at even pos, with last_odd=v
    # fwd1[a][v] = 1 + max_{b in adj[a], b>v}: fwd[b][0] ... but fwd[b][0] gives odd-length from b
    # Actually fwd1[a][v] = max(1, 1 + max_{b in adj[a], b>v}: fwd[b][0])... 
    # Hmm, fwd1[a][v] = 1 (just a) or 1 + fwd[b][0] for b in adj[a], b>v... 
    # Wait: path from a(even) with last_odd=v: a, b(odd,b>v), c(even,c>a), ...
    # Length = 1 + fwd_from_b_with_last_even_a... 
    # This requires tracking last_even too when at odd position.
    
    # I think the key insight I'm missing: when at odd position b, the constraint for next odd is b itself (not v). The constraint for next even is > last_even = a. So fwd[b][0] is NOT sufficient because it doesn't know last_even = a.
    
    # So the state truly needs both last_odd and last_even. This seems O(N^2).
    
    # Let me look at this differently. Maybe the answer for node i equals dp0[i] (backward DP)?
    # 
    # dp0[i] = longest path ending at i at odd position.
    # By reversing: if P = P1,...,PK is a valid path ending at PK=i (odd pos),
    # then reversed P' = PK,...,P1 starts at i.
    # P' odd positions: PK, P(K-2), ... = i, P(K-2), ... (decreasing in original = increasing in reversed? No.)
    # Original odd subseq P1<P3<...<PK. Reversed odd subseq of P' = PK, P(K-2),...,P1 which is DECREASING.
    # So reversed path is NOT valid in general.
    
    # Hmm. Let me look at test case 1:
    # N=5, edges: 1-5, 1-3, 1-2, 2-5, 4-5
    # Expected output: 4 4 4 2 2
    # 
    # For node 1: answer is 4. Example path (1,3,5,4,7) - wait that's test 3.
    # Test 1 answer for node 1 is 4. What path? 
    # Edges: 1-5,1-3,1-2,2-5,4-5
    # Path of length 4 starting at 1: 1,2,5,4? Check: odd={1,5} increasing✓, even={2,4} increasing✓. Valid! Length 4.
    # Or 1,5,2,... no 2 not connected to 5... wait 2-5 exists. 1,5,2,... 2 connected to 1,5. From 2: neighbors 1,5. 
    # 1,5,2,5? Can't repeat? Actually the problem says "path" - does it allow repeated nodes?
    # Looking at example: P=(1,3,5,4,7) in test 3 - these are all distinct. Probably simple path.
    # But with simple path constraint, this becomes NP-hard in general...
    
    # Wait, maybe nodes CAN be repeated? Let me re-read.
    # "Um caminho P de tamanho K é definido como uma sequência de interseções P1, P2, ..., PK"
    # It doesn't say distinct. So nodes can repeat!
    
    # If nodes can repeat, then we could have infinite paths... unless the increasing constraint bounds it.
    # Odd subsequence strictly increasing: at most N elements. Even subsequence strictly increasing: at most N elements.
    # So path length ≤ 2N. Good.
    
    # With repeated nodes allowed, the DP approach works!
    # State: (last_odd, last_even) - but that's O(N^2) states.
    
    # Actually with the recurrence dp0[v] = max(1, max_{u in adj[v], w in adj[u], w<v} dp0[w] + 2):
    # This correctly computes the longest path ending at v at odd position, regardless of the even elements.
    # Because: dp0[w] + 2 means we extend path ending at w(odd) by going w->some_node(even)->v(odd).
    # The even node can be anything (any common neighbor of w and v... wait, not common neighbor).
    # u is a neighbor of v, w is a neighbor of u. So path: ...->w(odd)->u(even)->v(odd).
    # The even subsequence constraint: u > last_even. But dp0[w] doesn't track last_even!
    
    # So dp0[v] as computed is NOT correct because it ignores the even subsequence constraint.
    
    # Hmm. Let me reconsider with a small example.
    # Test 1: edges 1-5,1-3,1-2,2-5,4-5. Answer for node 1 is 4.
    # Path 1,2,5,4: odd={1,5}✓, even={2,4}✓. Valid, length 4.
    # 
    # dp0[5] with recurrence: max(1, max_{u in adj[5], w in adj[u], w<5} dp0[w]+2)
    # adj[5] = {1,2,4}
    # u=1: adj[1]={5,3,2}, w in {3,2} (w<5, w≠5): dp0[3]+2, dp0[2]+2
    # u=2: adj[2]={1,5}, w in {1} (w<5): dp0[1]+2
    # u=4: adj[4]={5}, w in {} (no w<5 other than... adj[4]={5}, 5 not <5): nothing
    # dp0[1]=1, dp0[2]=1, dp0[3]=1 initially.
    # Process in order 1,2,3,4,5:
    # dp0[1]=1 (no w<1)
    # dp0[2]: adj[2]={1,5}. u=1: adj[1]={5,3,2}, w<2: none (5,3 all ≥2, 2 not <2... wait 2 is not <2). Hmm adj[1] includes 2 but w<2 means w=1 only, and 1 is in adj[1]? No, adj[1]={5,3,2}, none <2 except... none. u=5: adj[5]={1,2,4}, w<2: w=1. dp0[1]+2=3. So dp0[2]=3.
    # Wait that seems off. dp0[2]=3 means longest path ending at 2 at odd position has length 3.
    # Path: ?->?->2. w=1(odd)->u=5(even)->2(odd). Path: 1,5,2. odd={1,2}✓, even={5}. Length 3. Valid!
    # dp0[3]: adj[3]={1}. u=1: adj[1]={5,3,2}, w<3: w=1? 1 is in adj[1]? adj[1]={5,3,2}, 1 not in adj[1] (no self-loop). w=2: dp0[2]+2=5. So dp0[3]=5.
    # Path: 2(odd)->1(even)->3(odd)? But wait, is 2 connected to 1? Yes. Is 1 connected to 3? Yes. Path: ...->2->1->3. But dp0[2]=3, so full path has length 5: ?->?->2->1->3. 
    # What's the path? dp0[2]=3 came from 1->5->2. So path: 1(odd)->5(even)->2(odd)->1(even)->3(odd). odd={1,2,3}✓, even={5,1}. But 5>1, so even subseq {5,1} is NOT increasing! ✗
    # 
    # So the recurrence IS wrong because it ignores the even subsequence constraint!
    
    # I need to properly handle both constraints.
    
    # Let me define:
    # dp[v][e] = longest path ending at v (odd pos), where e is the last even element value
    # Transition: dp[v][e] = max over u in adj[v] (u is even pos, u=e), w in adj[u], w<v:
    #   dp[w][e'] + 2 where e' < e (since even subseq must be increasing, e > e')
    # 
    # This is O(N^2) states but maybe we can optimize.
    # 
    # dp[v][e] = max over w in 2-hop-neighbors of v through e, w<v, e'<e: dp[w][e'] + 2
    # 
    # Let best[v] = max over e: dp[v][e] ... but we need e for future transitions.
    
    # Alternative: define dp[v][e] where v is odd pos, e is last even pos.
    # For the answer starting at node i: i is P1 (odd), no previous even, so e=0 (or -inf).
    # answer[i] = max over all paths starting at i.
    
    # This is complex. Let me think about the structure differently.
    
    # The path alternates odd/even positions. The odd values must be increasing, even values must be increasing.
    # Think of it as: we maintain two "pointers" lo (last odd value) and le (last even value).
    # At odd position with value v: v > lo_prev (previous odd value, which is 2 steps back).
    # At even position with value u: u > le_prev.
    
    # State = (current_node, parity, lo, le). Too large.
    
    # Key observation: lo is always the current node if parity=0, and le is always the current node if parity=1.
    # So state = (current_node v, parity p, last_value_of_other_parity x).
    # If p=0: v is odd, x = last even value (le).
    # If p=1: v is even, x = last odd value (lo).
    
    # dp[v][0][x] = longest path ending at v (odd), last even = x. (x < v not required, x is just the last even)
    # dp[v][1][x] = longest path ending at v (even), last odd = x. (x < v not required)
    
    # Transition:
    # dp[v][0][x] -> dp[u][1][v] for u in adj[v], u > x (even subseq: u > last even = x)
    # dp[v][1][x] -> dp[u][0][v] for u in adj[v], u > x (odd subseq: u > last odd = x)
    
    # So both transitions are symmetric! The constraint is always: new node > x (last value of same parity).
    
    # dp[v][0][x]: path ends at v (odd), last even = x. To extend: go to u (even), u > x.
    # dp[u][1][v] = max(dp[u][1][v], dp[v][0][x] + 1) for u in adj[v], u > x.
    
    # dp[v][1][x]: path ends at v (even), last odd = x. To extend: go to u (odd), u > x.
    # dp[u][0][v] = max(dp[u][0][v], dp[v][1][x] + 1) for u in adj[v], u > x.
    
    # This is O(N^2) states. For N=10^5, too slow.
    
    # Hmm. Let me look at the constraints again: N ≤ 10^5, M ≤ 5*10^5.
    # Expected complexity probably O(M log N) or O(N log N).
    
    # Let me think about what dp[v][p][x] really means.
    # dp[v][0][x] = longest path ending at v (odd pos), last even = x.
    # For fixed v, we want max over x < threshold of dp[v][0][x].
    # 
    # When transitioning from dp[v][1][x] to dp[u][0][v] (u in adj[v], u > x):
    # dp[u][0][v] = max over x < u: dp[v][1][x] + 1
    # 
    # So dp[u][0][v] = (max over x < u of dp[v][1][x]) + 1, for u in adj[v], u > x... 
    # Wait: u > x is the constraint (u must be > last odd = x). So:
    # dp[u][0][v] = max_{x < u} dp[v][1][x] + 1
    # 
    # Similarly: dp[u][1][v] = max_{x < u} dp[v][0][x] + 1
    
    # Now define:
    # A[v][0] = function: for each threshold t, max_{x < t} dp[v][0][x]  (prefix max of dp[v][0])
    # A[v][1] = function: for each threshold t, max_{x < t} dp[v][1][x]
    
    # Then:
    # dp[u][0][v] = A[v][1](u) + 1  (for u in adj[v])
    # dp[u][1][v] = A[v][0](u) + 1  (for u in adj[v])
    
    # And A[u][0](t) = max_{v < t} dp[u][0][v] = max_{v < t, v in adj[u]} (A[v][1](u) + 1)... 
    # Hmm, dp[u][0][v] is defined for v that are "last even" values, which means v was the previous even node.
    # v must be a neighbor of u (since we came from v to u... wait no, u came from some node w to u, and v is the last even).
    
    # Actually I'm confusing myself. Let me re-examine.
    # dp[u][0][v]: path ends at u (odd pos), last even element = v.
    # The path looks like: ..., v(even), u(odd), where v is a neighbor of u (since there's an edge v-u).
    # Wait, not necessarily! v is the last even element, but u might have come from v directly or there could be more elements after v.
    # No wait: u is the LAST element (odd pos), and v is the last even element. Since u is last and odd, the element before u is even = v. So v is a direct predecessor of u, meaning v-u is an edge.
    
    # So dp[u][0][v] is only nonzero if v is a neighbor of u (or v=0 meaning path of length 1).
    # dp[u][0][0] = 1 (path of just u, no even element yet, last even = 0 = sentinel).
    # dp[u][0][v] for v in adj[u]: = A[v][1](u) + 1 = (max_{x < u} dp[v][1][x]) + 1
    
    # And dp[v][1][x] for x in adj[v]: = A[x][0](v) + 1 = (max_{y < v} dp[x][0][y]) + 1
    # dp[v][1][0] = 1 (path of just v at even pos... but a path starts at odd pos, so this shouldn't happen)
    # Actually a path can start at any node. If path starts at v (even pos = P2?), no - P1 is always odd pos.
    # Wait, P1 is the first element, which is at position 1 = odd. So the path always starts at odd position.
    # dp[v][1][x]: path ends at v (even), last odd = x. This path started at some odd node.
    # The element before v (even) is x (odd), and x is a neighbor of v.
    # dp[v][1][x] = A[x][0](v) + 1 for x in adj[v].
    
    # So:
    # dp[u][0][v] = (max_{x < u} dp[v][1][x]) + 1 for v in adj[u]  ... (1)
    # dp[v][1][x] = (max_{y < v} dp[x][0][y]) + 1 for x in adj[v]  ... (2)
    # dp[u][0][0] = 1 (base case, path of length 1)
    
    # From (2): dp[v][1][x] = (max_{y < v} dp[x][0][y]) + 1
    # Substituting into (1): dp[u][0][v] = (max_{x < u} ((max_{y < v} dp[x][0][y]) + 1)) + 1
    #                                     = (max_{x < u} max_{y < v} dp[x][0][y]) + 2
    #                                     = max_{x < u, y < v} dp[x][0][y] + 2
    # where x in adj[v] and y in adj[x] (= adj of x, which includes u's neighbor's neighbor).
    # Wait: x is in adj[v] (from eq 2, x is neighbor of v), and y is in adj[x] (from dp[x][0][y], y is neighbor of x).
    # Also v is in adj[u].
    
    # So dp[u][0][v] = max_{x in adj[v], x<u, y in adj[x], y<v} dp[x][0][y] + 2, for v in adj[u].
    
    # This is a 4-hop recurrence. Hard to optimize directly.
    
    # Let me define F[u][v] = dp[u][0][v] for u,v where v in adj[u] or v=0.
    # F[u][0] = 1.
    # F[u][v] = max_{x in adj[v], x<u, y in adj[x], y<v} F[x][y] + 2, for v in adj[u].
    
    # The answer for starting node i: 
    # i starts at odd pos. The longest path starting at i.
    # By the forward DP (starting from i), or we can use the backward DP and note:
    # The longest path starting at i = longest path where i is the first odd element.
    # In the backward DP, dp[u][0][v] = longest path ending at u (odd), last even = v.
    # The path starts at some odd node s with dp[s][0][0] = 1.
    # 
    # Hmm, the answer for node i is NOT directly dp[i][0][0] (that's just 1).
    # 
    # I think we need a forward DP. Let me define:
    # g[v][0][e] = longest path starting at v (odd pos), last even so far = e (initially 0)
    # g[v][1][o] = longest path starting at v (even pos), last odd so far = o
    # 
    # g[v][0][e] = max(1, max_{u in adj[v], u>e} (1 + g[u][1][v]))
    # g[u][1][v] = max(1, max_{w in adj[u], w>v} (1 + g[w][0][u]))
    # 
    # g[v][0][e] = max(1, max_{u in adj[v], u>e, w in adj[u], w>v} (2 + g[w][0][u]))
    # 
    # Answer for node i = g[i][0][0].
    # 
    # g[v][0][e] depends on e. For fixed v, as e increases, g[v][0][e] can only decrease or stay same.
    # 
    # g[v][0][e] = max(1, max_{u in adj[v], u>e, w in adj[u], w>v} (2 + g[w][0][u]))
    # 
    # The term max_{u in adj[v], u>e, w in adj[u], w>v} g[w][0][u] depends on e (threshold on u).
    # 
    # For fixed v, define h[v](e) = max_{u in adj[v], u>e, w in adj[u], w>v} g[w][0][u].
    # g[v][0][e] = max(1, h[v](e) + 2).
    # h[v](e) is non-increasing in e.
    # 
    # g[w][0][u] = max(1, h[w](u) + 2).
    # h[v](e) = max_{u in adj[v], u>e} max_{w in adj[u], w>v} g[w][0][u]
    #          = max_{u in adj[v], u>e} max_{w in adj[u], w>v} max(1, h[w](u)+2)
    # 
    # This is still complex. Let me try to think of a simpler characterization.
    
    # Actually, I wonder if the answer for node i equals dp0[i] from the backward DP, where dp0 is computed correctly.
    
    # Let me verify with test 1:
    # Edges: 1-5,1-3,1-2,2-5,4-5. Expected: 4 4 4 2 2.
    # 
    # For node 1, answer=4. Path: 1,2,5,4. odd={1,5}✓, even={2,4}✓.
    # For node 2, answer=4. Path: 2,1,3,? or 2,5,4,? 
    #   2,5,4,5? repeated. 2,1,5,4: odd={2,5}✓, even={1,4}✓. Length 4. ✓
    # For node 3, answer=4. Path: 3,1,5,4: odd={3,5}✓, even={1,4}✓. Length 4. ✓
    # For node 4, answer=2. adj[4]={5}. Path: 4,5. Length 2. Can we do 4,5,x,y? 
    #   From 5: adj[5]={1,2,4}. x must be >4 (odd subseq: x>4). x=5? Not in adj[5] as self. None >4 in adj[5]={1,2,4}. So max length 2. ✓
    # For node 5, answer=2. adj[5]={1,2,4}. Path: 5,x,y where y>5. adj of x: 
    #   x=1: adj[1]={5,3,2}, y>5: none. x=2: adj[2]={1,5}, y>5: none. x=4: adj[4]={5}, y>5: none. So max length 2. ✓
    
    # Now let me think about the forward DP more carefully.
    # g[v][0][e] = longest path starting at v (odd), with last even = e (e=0 means no even yet).
    # g[v][0][e] = max(1, max_{u in adj[v], u>e, w in adj[u], w>v} (2 + g[w][0][u]))
    # 
    # For node 1: g[1][0][0] = max(1, max_{u in adj[1]={5,3,2}, u>0, w in adj[u], w>1} (2+g[w][0][u]))
    # u=5: adj[5]={1,2,4}, w>1: w=2,4. g[2][0][5]+2, g[4][0][5]+2.
    # u=3: adj[3]={1}, w>1: none.
    # u=2: adj[2]={1,5}, w>1: w=5. g[5][0][2]+2.
    # 
    # g[2][0][5]: max(1, max_{u in adj[2]={1,5}, u>5: none}...) = 1.
    # g[4][0][5]: max(1, max_{u in adj[4]={5}, u>5: none}...) = 1.
    # g[5][0][2]: max(1, max_{u in adj[5]={1,2,4}, u>2: u=4, w in adj[4]={5}, w>5: none}...) = 1.
    # 
    # So g[1][0][0] = max(1, 1+2, 1+2, 1+2) = 3. But expected is 4!
    
    # Hmm, I'm missing something. The path 1,2,5,4 has length 4.
    # 1(odd,e=0)->2(even,o=1)->5(odd,e=2)->4(even,o=5)->... wait, 4 is the last element.
    # Path: 1,2,5,4. Length 4. 
    # g[1][0][0]: from 1, go to u=2 (even, u>0✓), then w=5 (odd, w>1✓), then g[5][0][2].
    # g[5][0][2]: from 5, go to u in adj[5]={1,2,4}, u>2: u=4. Then w in adj[4]={5}, w>5: none.
    # So g[5][0][2] = max(1, ...) = 1? But path 5,4 has length 2!
    # 
    # Oh! I see the issue. g[v][0][e] should also count paths of even length (ending at even pos).
    # The path 1,2,5,4 ends at 4 (even pos). My recurrence only counts paths ending at odd pos!
    
    # I need to also count paths ending at even position.
    # g[v][0][e] = max path starting at v (odd), last even = e.
    # This path can end at odd or even position.
    # 
    # If it ends at odd: length is odd.
    # If it ends at even: length is even.
    # 
    # g[v][0][e] = max(
    #   1,  // path of length 1 (just v)
    #   max_{u in adj[v], u>e} (1 + g_even[u][1][v])  // extend to u (even), then continue
    # )
    # where g_even[u][1][v] = max path starting at u (even pos), last odd = v.
    # g_even[u][1][v] = max(
    #   1,  // path of length 1 (just u, total path length 2)
    #   max_{w in adj[u], w>v} (1 + g[w][0][u])  // extend to w (odd), then continue
    # )
    # 
    # So g[v][0][e] = max(
    #   1,
    #   max_{u in adj[v], u>e} (1 + max(1, max_{w in adj[u], w>v} (1 + g[w][0][u])))
    # )
    # = max(
    #   1,
    #   max_{u in adj[v], u>e} 2,  // path v,u of length 2
    #   max_{u in adj[v], u>e, w in adj[u], w>v} (2 + g[w][0][u])  // longer path
    # )
    # = max(
    #   1,
    #   2 if adj[v] has u>e,
    #   max_{u in adj[v], u>e, w in adj[u], w>v} g[w][0][u] + 2
    # )
    
    # For g[5][0][2]: adj[5]={1,2,4}, u>2: u=4. 
    # Path 5,4: length 2. ✓
    # w in adj[4]={5}, w>5: none. So g[5][0][2] = 2.
    
    # For g[1][0][0]: 
    # u=2 (>0): path 1,2 length 2. w in adj[2]={1,5}, w>1: w=5. g[5][0][2]+2 = 2+2=4. ✓
    # u=3 (>0): path 1,3 length 2. w in adj[3]={1}, w>1: none.
    # u=5 (>0): path 1,5 length 2. w in adj[5]={1,2,4}, w>1: w=2,4. g[2][0][5]+2, g[4][0][5]+2.
    #   g[2][0][5]: adj[2]={1,5}, u>5: none. So g[2][0][5]=1. +2=3.
    #   g[4][0][5]: adj[4]={5}, u>5: none. So g[4][0][5]=1. +2=3.
    # So g[1][0][0] = max(1, 2, 4, 2, 3, 3) = 4. ✓
    
    # Great! So the recurrence is:
    # g[v][0][e] = max(1, max_{u in adj[v], u>e} 2, max_{u in adj[v], u>e, w in adj[u], w>v} g[w][0][u] + 2)
    # = max(1, (2 if ∃u in adj[v] with u>e), max_{u in adj[v], u>e, w in adj[u], w>v} g[w][0][u] + 2)
    
    # Simplify: g[v][0][e] = max(1, max_{u in adj[v], u>e} (1 + max(1, max_{w in adj[u], w>v} (1+g[w][0][u]))))
    
    # Let me define: G[v][e] = g[v][0][e] (longest path starting at v, odd pos, last even = e).
    # Answer for node i = G[i][0].
    
    # G[v][e] = max(1, max_{u in adj[v], u>e} (1 + max(1, max_{w in adj[u], w>v} (1 + G[w][u]))))
    
    # This has O(N^2) states (v, e) where e can be any value 0..N.
    # But e is always a neighbor of v (or 0). So number of states is O(M + N).
    # For each state (v, e), we compute over neighbors u of v with u>e, and for each u, over neighbors w of u with w>v.
    # Total work: O(M * degree) = O(M * N/M * M) ... could be O(M^2/N) to O(M^2).
    
    # For M=5*10^5 and N=10^5, this might be too slow.
    
    # We need memoization + smart ordering.
    # G[v][e] depends on G[w][u] where w>v (strictly). So we can process in decreasing order of v!
    # For fixed v (decreasing), G[v][e] depends on G[w][u] with w>v (already computed).
    # For fixed v, G[v][e] is non-increasing in e (larger e = more restrictive).
    # 
    # For fixed v, we need: for each e (neighbor of v or 0), compute G[v][e].
    # G[v][e] = max(1, max_{u in adj[v], u>e} (1 + H[v][u]))
    # where H[v][u] = max(1, max_{w in adj[u], w>v} (1 + G[w][u]))
    # 
    # H[v][u] = max(1, max_{w in adj[u], w>v} G[w][u] + 1)
    # 
    # For fixed u, H[v][u] is non-increasing in v (larger v = fewer w>v).
    # 
    # G[v][e] = max(1, max_{u in adj[v], u>e} (H[v][u] + 1))
    # 
    # For fixed v, as e increases, fewer u qualify, so G[v][e] is non-increasing.
    # 
    # To compute G[v][e] for all e (neighbors of v + 0):
    # Sort neighbors of v by value. For each e, we want max_{u in adj[v], u>e} H[v][u].
    # This is a suffix max over sorted neighbors.
    # 
    # H[v][u] for u in adj[v]: H[v][u] = max(1, max_{w in adj[u], w>v} G[w][u] + 1).
    # For fixed u, we need max_{w in adj[u], w>v} G[w][u].
    # G[w][u] is defined for w in adj[u] (or w=0 for base case).
    # Since we process v in decreasing order, when computing H[v][u], all G[w][u] for w>v are already computed.
    # 
    # For each u, maintain a sorted structure of (w, G[w][u]) for w in adj[u] processed so far (w>current v).
    # Query: max G[w][u] for w > v. Since we process v decreasingly, we add w to u's structure when we process w.
    # 
    # When we process node v (in decreasing order):
    # 1. For each u in adj[v]: update u's structure with (v, G[v][u]).
    #    But G[v][u] requires H[u][v]... wait, G[v][u] means G[v][e=u], which is the path starting at v with last even = u.
    #    This is computed when we process v.
    # 
    # Hmm, there's a chicken-and-egg problem. Let me re-examine.
    
    # Processing order: decreasing v.
    # When processing v:
    # - Compute H[v][u] for all u in adj[v]:
    #   H[v][u] = max(1, max_{w in adj[u], w>v} G[w][u] + 1)
    #   For each u in adj[v], query: max G[w][u] for w in adj[u], w>v.
    #   Since w>v and we process decreasingly, these G[w][u] are already computed.
    #   We need: for each u, a data structure that gives max G[w][u] for w > threshold.
    #   Since we process w in decreasing order and add to u's structure, we can maintain a running max.
    #   But "w > v" means all w processed before v (since we go decreasing). So it's just the running max for u.
    #   Wait: we process N, N-1, ..., 1. When processing v, all w > v have been processed.
    #   For each u, maintain best_G[u] = max G[w][u] for w in adj[u], w > v (i.e., w processed so far).
    #   H[v][u] = max(1, best_G[u] + 1) if best_G[u] > 0, else 1.
    #   Actually H[v][u] = max(1, best_G[u] + 1) where best_G[u] = max G[w][u] for w in adj[u], w>v.
    #   If no such w, best_G[u] = 0 (or -inf), H[v][u] = 1.
    
    # - Compute G[v][e] for all e in adj[v] ∪ {0}:
    #   G[v][e] = max(1, max_{u in adj[v], u>e} (H[v][u] + 1))
    #   For e=0: max_{u in adj[v]} (H[v][u] + 1) (all u qualify since u>0).
    #   For e in adj[v]: max_{u in adj[v], u>e} (H[v][u] + 1).
    #   Compute suffix max of H[v][u]+1 over sorted adj[v].
    
    # - After computing G[v][e] for all e, update best_G for neighbors:
    #   For each u in adj[v]: update best_G[u] = max(best_G[u], G[v][u]).
    #   (G[v][u] = G[v][e=u], the path starting at v with last even = u.)
    
    # This seems correct! Let me verify the complexity.
    # For each v: O(deg(v) log deg(v)) to sort neighbors and compute suffix max.
    # Total: O(M log N).
    # Space: O(M) for G[v][e] (only need G[v][u] for u in adj[v]).
    
    # Wait, but G[v][u] is only needed when u is a neighbor of v AND v is a neighbor of u (which is the same since undirected). So G[v][u] is defined for edges (v,u). Total O(M) values.
    
    # Let me re-examine: G[w][u] is needed in H[v][u] = max(1, max_{w in adj[u], w>v} G[w][u] + 1).
    # G[w][u] = path starting at w (odd), last even = u. For this to make sense, u must be a neighbor of w (since last even = u means u was the previous even node, which is a direct predecessor of w... wait, not necessarily).
    
    # Hmm, actually e (last even) doesn't have to be a direct neighbor of v. It's the last even element in the path, which could be anywhere. But in the recurrence:
    # G[v][e] = max(1, max_{u in adj[v], u>e} (1 + H[v][u]))
    # H[v][u] = max(1, max_{w in adj[u], w>v} (1 + G[w][u]))
    # G[w][u] = path starting at w (odd), last even = u.
    # Here u is a neighbor of w (since we just came from u to w: u(even)->w(odd), so u-w is an edge).
    # So G[w][u] is only needed for u in adj[w]. ✓
    
    # And G[v][e]: e is the last even element. In the recurrence, e comes from the context where v was reached from some even node e. But for the answer, we call G[i][0] (no previous even).
    # In the recurrence, G[w][u] is called with e=u where u in adj[w]. So G[v][e] is only called with e in adj[v] or e=0. ✓
    
    # Great! So the algorithm is:
    # 1. Process nodes v from N down to 1.
    # 2. For each v, compute H[v][u] for u in adj[v]:
    #    H[v][u] = max(1, best_G[u] + 1) where best_G[u] = max G[w][u] for w in adj[u], w>v (already processed).
    # 3. Compute G[v][0] = max(1, max_{u in adj[v]} (H[v][u] + 1)).
    #    (Also compute G[v][e] for e in adj[v] for use in step 4, but we need suffix max.)
    #    Sort adj[v] by value. Compute suffix max of H[v][u]+1.
    #    G[v][e] = max(1, suffix_max for u > e).
    # 4. For each u in adj[v]: update best_G[u] = max(best_G[u], G[v][u]).
    
    # Answer for node i = G[i][0].
    
    # Let me verify with test 1:
    # N=5, edges: 1-5,1-3,1-2,2-5,4-5.
    # adj[1]={2,3,5}, adj[2]={1,5}, adj[3]={1}, adj[4]={5}, adj[5]={1,2,4}.
    # best_G[u] initialized to 0 for all u.
    
    # Process v=5:
    # H[5][u] for u in adj[5]={1,2,4}:
    #   H[5][1] = max(1, best_G[1]+1) = max(1,0+1)=1. (best_G[1]=0, no w>5 in adj[1])
    #   H[5][2] = max(1, best_G[2]+1) = 1.
    #   H[5][4] = max(1, best_G[4]+1) = 1.
    # Sort adj[5]={1,2,4}. H values: H[5][1]=1, H[5][2]=1, H[5][4]=1.
    # Suffix max of H[5][u]+1 for u>e:
    #   e=0: max over u in {1,2,4}: H+1=2. G[5][0]=max(1,2)=2.
    #   e=1: max over u in {2,4}: 2. G[5][1]=2.
    #   e=2: max over u in {4}: 2. G[5][2]=2.
    #   e=4: max over u in {}: 0. G[5][4]=1.
    # Update best_G:
    #   For u=1: best_G[1] = max(0, G[5][1]) = max(0,2) = 2.
    #   For u=2: best_G[2] = max(0, G[5][2]) = max(0,2) = 2.
    #   For u=4: best_G[4] = max(0, G[5][4]) = max(0,1) = 1.
    
    # Process v=4:
    # H[4][u] for u in adj[4]={5}:
    #   H[4][5] = max(1, best_G[5]+1) = max(1,0+1)=1. (best_G[5]=0)
    # G[4][0] = max(1, H[4][5]+1) = max(1,2) = 2.
    # G[4][5] = max(1, suffix for u>5 in {5}: none) = 1.
    # Update best_G:
    #   For u=5: best_G[5] = max(0, G[4][5]) = max(0,1) = 1.
    
    # Process v=3:
    # H[3][u] for u in adj[3]={1}:
    #   H[3][1] = max(1, best_G[1]+1) = max(1,2+1)=3.
    # G[3][0] = max(1, H[3][1]+1) = max(1,4) = 4.
    # G[3][1] = max(1, suffix for u>1 in {1}: none) = 1.
    # Update best_G:
    #   For u=1: best_G[1] = max(2, G[3][1]) = max(2,1) = 2.
    
    # Process v=2:
    # H[2][u] for u in adj[2]={1,5}:
    #   H[2][1] = max(1, best_G[1]+1) = max(1,2+1)=3.
    #   H[2][5] = max(1, best_G[5]+1) = max(1,1+1)=2.
    # Sort adj[2]={1,5}. 
    # Suffix max of H[2][u]+1 for u>e:
    #   e=0: max(H[2][1]+1, H[2][5]+1) = max(4,3) = 4. G[2][0]=4.
    #   e=1: max(H[2][5]+1) = 3. G[2][1]=3.
    #   e=5: none. G[2][5]=1.
    # Update best_G:
    #   For u=1: best_G[1] = max(2, G[2][1]) = max(2,3) = 3.
    #   For u=5: best_G[5] = max(1, G[2][5]) = max(1,1) = 1.
    
    # Process v=1:
    # H[1][u] for u in adj[1]={2,3,5}:
    #   H[1][2] = max(1, best_G[2]+1) = max(1,2+1)=3.
    #   H[1][3] = max(1, best_G[3]+1) = max(1,0+1)=1.
    #   H[1][5] = max(1, best_G[5]+1) = max(1,1+1)=2.
    # Sort adj[1]={2,3,5}.
    # Suffix max of H[1][u]+1:
    #   e=0: max(H[1][2]+1, H[1][3]+1, H[1][5]+1) = max(4,2,3) = 4. G[1][0]=4.
    # 
    # Answers: G[1][0]=4, G[2][0]=4, G[3][0]=4, G[4][0]=2, G[5][0]=2. ✓ Matches expected!
    
    # Let me verify test 2 quickly:
    # N=6, edges: 1-3,2-3,4-2,3-4,3-5,5-4. Expected: 7 5 6 4 2 1.
    # adj[1]={3}, adj[2]={3,4}, adj[3]={1,2,4,5}, adj[4]={2,3,5}, adj[5]={3,4}, adj[6]={}.
    
    # Process v=6: adj[6]={}. G[6][0]=1. No updates.
    # Process v=5: adj[5]={3,4}.
    #   H[5][3]=max(1,best_G[3]+1)=1, H[5][4]=max(1,best_G[4]+1)=1.
    #   G[5][0]=max(1,max(2,2))=2. G[5][3]=max(1,H[5][4]+1)=2. G[5][4]=1.
    #   Update: best_G[3]=max(0,G[5][3])=2, best_G[4]=max(0,G[5][4])=1.
    # Process v=4: adj[4]={2,3,5}.
    #   H[4][2]=max(1,best_G[2]+1)=1, H[4][3]=max(1,best_G[3]+1)=3, H[4][5]=max(1,best_G[5]+1)=1.
    #   Sort {2,3,5}: H values 1,3,1.
    #   Suffix max (H+1): e=0: max(2,4,2)=4. G[4][0]=4.
    #   e=2: max(H[4][3]+1,H[4][5]+1)=max(4,2)=4. G[4][2]=4.
    #   e=3: max(H[4][5]+1)=2. G[4][3]=2.
    #   e=5: none. G[4][5]=1.
    #   Update: best_G[2]=max(0,G[4][2])=4, best_G[3]=max(2,G[4][3])=max(2,2)=2, best_G[5]=max(0,G[4][5])=1.
    # Process v=3: adj[3]={1,2,4,5}.
    #   H[3][1]=max(1,best_G[1]+1)=1, H[3][2]=max(1,best_G[2]+1)=5, H[3][4]=max(1,best_G[4]+1)=2, H[3][5]=max(1,best_G[5]+1)=2.
    #   Sort {1,2,4,5}: H values 1,5,2,2.
    #   Suffix max (H+1): 
    #     e=0: max(2,6,3,3)=6. G[3][0]=6.
    #     e=1: max(6,3,3)=6. G[3][1]=6.
    #     e=2: max(3,3)=3. G[3][2]=3.
    #     e=4: max(3)=3. G[3][4]=3.
    #     e=5: none. G[3][5]=1.
    #   Update: best_G[1]=max(0,G[3][1])=6, best_G[2]=max(4,G[3][2])=max(4,3)=4, best_G[4]=max(1,G[3][4])=3, best_G[5]=max(1,G[3][5])=1.
    # Process v=2: adj[2]={3,4}.
    #   H[2][3]=max(1,best_G[3]+1)=3, H[2][4]=max(1,best_G[4]+1)=4.
    #   Sort {3,4}: H values 3,4.
    #   Suffix max (H+1):
    #     e=0: max(4,5)=5. G[2][0]=5.
    #     e=3: max(5)=5. G[2][3]=5.
    #     e=4: none. G[2][4]=1.
    #   Update: best_G[3]=max(2,G[2][3])=max(2,5)=5, best_G[4]=max(3,G[2][4])=max(3,1)=3.
    # Process v=1: adj[1]={3}.
    #   H[1][3]=max(1,best_G[3]+1)=6.
    #   G[1][0]=max(1,H[1][3]+1)=7.
    #   Update: best_G[3]=max(5,G[1][3])... G[1][3]=max(1, suffix for u>3 in {3}: none)=1. best_G[3]=max(5,1)=5.
    
    # Answers: G[1][0]=7, G[2][0]=5, G[3][0]=6, G[4][0]=4, G[5][0]=2, G[6][0]=1. ✓ Matches!
    
    # Great! The algorithm works. Now let me implement it efficiently.
    
    # Algorithm:
    # - Process nodes v from N down to 1.
    # - best_G[u] = max G[w][u] for w in adj[u], w > current v (i.e., w processed so far).
    # - For each v:
    #   a. Compute H[v][u] = max(1, best_G[u] + 1) for u in adj[v]. (If best_G[u]=0, H=1.)
    #      Actually H[v][u] = best_G[u] + 1 if best_G[u] > 0, else 1.
    #      Simplify: H[v][u] = max(1, best_G[u] + 1). Since best_G[u] >= 0, this is best_G[u]+1 if best_G[u]>=1, else 1.
    #      Actually best_G[u] = max G[w][u] >= 1 if any w>v in adj[u] exists (since G[w][u]>=1).
    #      If no w>v in adj[u], best_G[u]=0, H[v][u]=1.
    #   b. Sort adj[v] by value. Compute suffix max of (H[v][u]+1) over sorted adj[v].
    #      G[v][0] = max(1, suffix_max[0]) = suffix_max[0] (since suffix_max[0] >= 1 if adj[v] non-empty, else 1).
    #      For e in adj[v]: G[v][e] = max(1, suffix_max for u > e).
    #   c. For each u in adj[v]: update best_G[u] = max(best_G[u], G[v][u]).
    
    # For step b, to compute G[v][e] for all e in adj[v]:
    # Sort adj[v] as u1 < u2 < ... < uk.
    # suffix_max[i] = max(H[v][ui]+1, H[v][u(i+1)]+1, ..., H[v][uk]+1).
    # G[v][0] = suffix_max[0] (or 1 if adj empty).
    # G[v][uj] = suffix_max[j+1] (or 1 if j=k).
    # (G[v][uj] = max path starting at v with last even = uj, so next odd must be > uj, meaning we need u in adj[v] with u > uj.)
    
    # Implementation:
    
    import sys
    
    def solve():
        data = sys.stdin.buffer.read().split()
        idx = 0
        N = int(data[idx]); idx+=1
        M = int(data[idx]); idx+=1
        adj = [[] for _ in range(N+1)]
        for _ in range(M):
            a = int(data[idx]); idx+=1
            b = int(data[idx]); idx+=1
            adj[a].append(b)
            adj[b].append(a)
        
        # Sort adjacency lists
        for v in range(1, N+1):
            adj[v].sort()
        
        best_G = [0] * (N+1)  # best_G[u] = max G[w][u] for w > current v, w in adj[u]
        # G[v][u] stored as needed; we only need G[v][0] for answer and G[v][u] for u in adj[v] for updates.
        
        ans = [0] * (N+1)
        
        # G_val[v][u] - we'll compute on the fly
        # For each v, we need G[v][u] for u in adj[v] to update best_G[u].
        
        for v in range(N, 0, -1):
            neighbors = adj[v]  # sorted
            if not neighbors:
                ans[v] = 1
                continue
            
            # Compute H[v][u] for u in neighbors
            # H[v][u] = max(1, best_G[u] + 1)
            H = [max(1, best_G[u] + 1) for u in neighbors]
            # Actually: if best_G[u] == 0, H = 1. If best_G[u] >= 1, H = best_G[u]+1.
            # But best_G[u] is initialized to 0 and only updated with G values >= 1.
            # So H[v][u] = best_G[u] + 1 if best_G[u] > 0 else 1.
            # = max(1, best_G[u] + 1). Since best_G[u] >= 0, best_G[u]+1 >= 1. So H = best_G[u]+1.
            # Wait: if best_G[u]=0, best_G[u]+1=1. So H = best_G[u]+1 always! (Since best_G[u]>=0.)
            H = [best_G[u] + 1 for u in neighbors]
            # H[v][u] = best_G[u] + 1. If best_G[u]=0, H=1 (path of length 1 from u). ✓
            
            # Compute suffix max of H[i]+1 (= best_G[u]+2) over sorted neighbors.
            # suffix_max[i] = max(H[i]+1, H[i+1]+1, ..., H[k-1]+1)
            k = len(neighbors)
            suffix_max = [0] * (k+1)
            for i in range(k-1, -1, -1):
                suffix_max[i] = max(suffix_max[i+1], H[i] + 1)
            
            # G[v][0] = max(1, suffix_max[0])
            ans[v] = max(1, suffix_max[0])
            
            # G[v][neighbors[j]] = max(1, suffix_max[j+1])
            # Update best_G[u] for u in neighbors:
            for j, u in enumerate(neighbors):
                g_v_u = max(1, suffix_max[j+1])
                if g_v_u > best_G[u]:
                    best_G[u] = g_v_u
        
        print(*[ans[v] for v in range(1, N+1)])
    
    solve()

    # Wait, I need to double-check the H computation.
    # H[v][u] = max(1, max_{w in adj[u], w>v} G[w][u] + 1)
    # best_G[u] = max_{w in adj[u], w>v} G[w][u] (0 if none)
    # H[v][u] = max(1, best_G[u] + 1) = best_G[u] + 1 (since best_G[u] >= 0, so +1 >= 1). ✓
    
    # And G[v][e] = max(1, max_{u in adj[v], u>e} (H[v][u] + 1))
    # = max(1, max_{u in adj[v], u>e} (best_G[u] + 2))
    # suffix_max[i] = max_{j>=i} (H[j]+1) = max_{j>=i} (best_G[neighbors[j]] + 2)
    # G[v][0] = max(1, suffix_max[0]). ✓
    # G[v][neighbors[j]] = max(1, suffix_max[j+1]). ✓
    
    # The algorithm is O(M log N) due to sorting. Let me write the final clean code.

import sys

def solve():
    data = sys.stdin.buffer.read().split()
    idx = 0
    N = int(data[idx]); idx+=1
    M = int(data[idx]); idx+=1
    adj = [[] for _ in range(N+1)]
    for _ in range(M):
        a = int(data[idx]); idx+=1
        b = int(data[idx]); idx+=1
        adj[a].append(b)
        adj[b].append(a)
    
    for v in range(1, N+1):
        adj[v].sort()
    
    best_G = [0] * (N+1)
    ans = [1] * (N+1)
    
    for v in range(N, 0, -1):
        neighbors = adj[v]
        if not neighbors:
            continue
        
        k = len(neighbors)
        # suffix_max[i] = max over j>=i of (best_G[neighbors[j]] + 2)
        suffix_max = [0] * (k+1)
        for i in range(k-1, -1, -1):
            val = best_G[neighbors[i]] + 2
            suffix_max[i] = max(suffix_max[i+1], val)
        
        ans[v] = max(1, suffix_max[0])
        
        for j in range(k):
            u = neighbors[j]
            g_v_u = max(1, suffix_max[j+1])
            if g_v_u > best_G[u]:
                best_G[u] = g_v_u
    
    sys.stdout.write(' '.join(map(str, ans[1:])) + '\n')

solve()