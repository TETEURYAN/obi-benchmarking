
```python
import sys
from functools import lru_cache

def solve():
    input_data = sys.stdin.read().split()
    idx = 0
    N, K, T = int(input_data[idx]), int(input_data[idx+1]), int(input_data[idx+2])
    idx += 3
    P = [int(input_data[idx+i]) for i in range(N)]
    idx += N
    G = [int(input_data[idx+i]) for i in range(N)]
    idx += N
    
    # Get initial positions of group members (0-indexed)
    members = [i for i in range(N) if G[i] == 1]
    # K members
    
    # Key insight: members cannot pass through each other (they swap with non-members)
    # So the relative order of members is preserved.
    # Member i (0-indexed among members) will end up at some position,
    # and the positions must be strictly increasing.
    
    # We need to assign K positions from N positions to K members,
    # maintaining relative order, such that:
    # 1. The total "movement cost" <= T
    # 2. The movement cost: if member i starts at members[i] and ends at pos[i],
    #    the cost is sum of |members[i] - pos[i]| BUT we need to be careful about
    #    interactions between members.
    
    # Actually, since members maintain relative order and swap only with non-members,
    # the minimum number of swaps to move member i from members[i] to final_pos[i]
    # (where final positions are sorted) is more complex due to interactions.
    
    # Standard result: if we assign member i to position q[i] (sorted),
    # the total swaps needed = sum |members[i] - q[i]| - (correction for overlaps)
    # Actually the correct formula: total swaps = sum of |members[i] - q[i]| 
    # but we need to account for the fact that members block each other.
    
    # The correct minimum swaps: assign member i (sorted) to target t[i] (sorted),
    # cost = sum |members[i] - t[i]|
    # This works because members maintain relative order.
    
    # So we need to choose K positions (0-indexed) t[0] < t[1] < ... < t[K-1]
    # to maximize sum P[t[i]] subject to sum |members[i] - t[i]| <= T
    
    # DP approach:
    # dp[i][j][cost] = max brigadeiros using first i members assigned to first j positions
    # with total cost = cost
    # But cost can be up to T which is 1e9, too large.
    
    # Better: dp[i][j] = minimum cost to assign first i members to some j positions
    # ending at position j (0-indexed)
    # Then check if min cost <= T
    
    # dp[i][j] = min swaps to place i-th member (0-indexed) at position j,
    # with all previous members placed optimally before j
    # maximize sum of P values
    
    # Since N <= 300 and K <= N, we can do O(N^2 * K) DP
    
    # dp[i][j] = min cost to assign members 0..i to positions ending at j (member i at pos j)
    # We want to maximize sum of P, so we need to track both cost and value.
    
    # Let's do: for each subset assignment, track min cost for each (member_index, position) pair
    # dp[i][j] = min cost when member i is placed at position j (0-indexed), members 0..i placed optimally
    # We want max sum of P[positions] with cost <= T
    
    # But we need to track the sum of P as well. 
    # Alternative: enumerate all possible selections of K positions (sorted),
    # compute cost and value. But C(300,7) can be large...
    
    # Better DP:
    # dp[i][j] = min cost to place first i+1 members (0..i) with member i at position j
    # Transition: dp[i][j] = min over j' < j of dp[i-1][j'] + |members[i] - j|
    # Value: we want to maximize sum of P[j_0] + ... + P[j_{K-1}]
    
    # We need to track value too. Let's do:
    # dp[i][j] = dict or we separate: for each (i,j), store min cost
    # Then greedily... no.
    
    # Since we want to maximize value subject to cost <= T:
    # dp[i][j][v] = min cost to place members 0..i with member i at pos j, total value = v
    # v can be up to 9*300 = 2700, manageable!
    
    # dp[i][j] = min cost to place members 0..i with member i at pos j, maximizing value
    # But we need to track value...
    
    # Let's do: dp[i][j] = min cost for each possible value sum
    # Or: dp2[i][j] = max value achievable with cost <= T for members 0..i, member i at pos j
    # But cost constraint makes it tricky.
    
    # Best approach: dp[i][j] = min cost to place members 0..i optimally with member i at pos j
    # and separately track the value. But value depends on which positions were chosen.
    
    # Full DP: dp[i][j] = (min_cost, max_value) - not straightforward Pareto.
    
    # Since max value sum <= 9*300 = 2700, let's do:
    # dp[i][j][val] = min cost to assign members 0..i with member i at position j, total value = val
    # States: K * N * (9*K) = 300 * 300 * 2700 ~ 2.4 * 10^8 -- too much
    
    # Alternative: dp[i][j] = min cost to place members 0..i with member i at pos j
    # (ignoring value for now, just tracking cost)
    # Then for each valid assignment (cost <= T), compute value.
    # But we need to know which positions were chosen.
    
    # Let me think differently. 
    # dp[i][j] = min cost to place members 0..i with member i at position j
    # We want max sum P[positions] with total cost <= T
    # 
    # We can do: dp[i][j] = min cost, and separately
    # val[i][j] = max value when member i is at position j and cost is minimized
    # But min cost and max value might conflict.
    
    # Correct approach with value tracking:
    # dp[i][j] = max value achievable for members 0..i with member i at pos j AND cost <= T_remaining
    # But T_remaining depends on previous choices...
    
    # Let's use: dp[i][j] = min cost to place members 0..i with member i at pos j, 
    # while maximizing value (lexicographic: first minimize cost, then maximize value) -- NO
    
    # The right DP:
    # For each pair (i, j): we want to know, for each possible "budget used so far",
    # the maximum value. But budget is up to 1e9.
    
    # Key observation: the cost |members[i] - j| is at most N-1 <= 299.
    # Total cost <= K * (N-1) <= 300 * 299 ~ 90000.
    # If T >= 90000, we can reach any configuration!
    # So effective T = min(T, K*(N-1)) <= ~90000.
    
    # Now dp[i][j][cost] = max value, with cost up to ~90000
    # States: K * N * 90000 -- still too large (300 * 300 * 90000 = 8.1 * 10^9)
    
    # Hmm. Let's think again.
    # Actually total cost <= sum |members[i] - t[i]| <= K * N <= 300 * 300 = 90000
    # 
    # dp[i][j] where we track remaining budget:
    # dp[i][j][t] = max value for members 0..i with member i at pos j, having used t swaps
    # t up to 90000, i up to K=300, j up to N=300
    # = 300 * 300 * 90000 = too large
    
    # Better: dp[i][j] = min cost to place members 0..i with member i at pos j
    # AND for that min cost, max value.
    # But this doesn't work because a higher cost might give higher value.
    
    # Actually let's reconsider. The value only depends on which positions are chosen.
    # dp[i][j] = min cost to place members 0..i with member i at pos j
    # val[i][j] = max value when members 0..i placed with member i at pos j AND cost = dp[i][j]
    # 
    # This doesn't capture all Pareto-optimal solutions.
    
    # Let me try a different DP formulation:
    # dp[i][j] = for each possible total cost c, max value of placing members 0..i 
    #            with member i at position j using exactly cost c
    # 
    # But store as: dp[i][j] = array indexed by cost, value = max brigadeiros
    # Cost per step: |members[i] - j| <= N <= 300
    # Total cost <= K*N but we cap at T_eff = min(T, K*N)
    # 
    # With N=300, K=300: too large.
    
    # For the given constraints (N<=300), let me think of a smarter bound on cost.
    # Each member moves at most N positions, so total cost <= K*N.
    # But K*N <= 90000 and we have K*N states for dp[i][j], 
    # so dp[i][j][cost] has K*N*K*N = (K*N)^2 states which is too large.
    
    # Wait, let me reconsider the cost bound more carefully.
    # Member i starts at members[i] and ends at t[i].
    # t[i] is between 0 and N-1.
    # |members[i] - t[i]| <= N-1.
    # Sum over K members: <= K*(N-1) <= 300*299 ~ 90000.
    # 
    # But for the DP, at step i (placing member i), the cost added is |members[i] - j|.
    # The total cost accumulated after placing all K members is at most K*(N-1).
    # 
    # DP: dp[i][j] = array of size (max_cost+1) where dp[i][j][c] = max value
    # Transition: dp[i][j][c] = max over j' < j of dp[i-1][j'][c - |members[i]-j|] + P[j]
    # 
    # Size: K * N * max_cost = 300 * 300 * 90000 -- too large.
    
    # I need a smarter approach.
    # 
    # Key insight: We can reformulate. 
    # Let's define the problem differently.
    # After all moves, member i (0-indexed, sorted by initial position) 
    # occupies position t[i] where t[0] < t[1] < ... < t[K-1].
    # Cost = sum_{i=0}^{K-1} |members[i] - t[i]|
    # Value = sum_{i=0}^{K-1} P[t[i]]
    # Maximize value subject to cost <= T.
    
    # DP over members and positions:
    # dp[i][j] = min cost to assign members 0..i with member i at position j
    # (greedy: for fixed positions, cost is determined)
    # 
    # Then answer = max P[t[0]] + ... + P[t[K-1]] over all valid assignments with cost <= T.
    
    # We need to track both cost and value. 
    # 
    # Alternative: dp[i][j] = min cost to place members 0..i with member i at pos j,
    # for each possible value sum v.
    # dp[i][j][v] = min cost
    # v <= 9*K <= 9*300 = 2700
    # States: K * N * 9K = 300 * 300 * 2700 = 2.43 * 10^8 -- borderline
    # 
    # Transition: dp[i][j][v] = min over j'<j of dp[i-1][j'][v - P[j]] + |members[i] - j|
    # 
    # This might work with careful implementation. Let's try.
    # 
    # Actually states are N * N * (9*N) but K <= N so worst case 300*300*2700.
    # With numpy or optimized code this might be feasible.
    # 
    # Let me think about the time complexity:
    # For each i (K iterations), j (N), j' (N), v (9K):
    # O(K * N^2 * 9K) = O(K^2 * N^2 * 9) 
    # With K=N=300: 300^2 * 300^2 * 9 = way too large.
    
    # Better transition: 
    # dp[i][j][v] = min over j'<j of dp[i-1][j'][v-P[j]] + cost_i(j)
    # = cost_i(j) + P[j] contribution + min over j'<j of dp[i-1][j'][v-P[j]]
    # 
    # For fixed i, j, v: we need min over j'<j of dp[i-1][j'][v-P[j]]
    # We can precompute prefix minimums over j' for each v.
    # 
    # Time: K * N * V where V = 9K
    # = 300 * 300 * 2700 = 2.43 * 10^8 -- still large but maybe ok with numpy
    
    # Let me implement this with numpy.
    
    import numpy as np
    
    T_eff = min(T, K * N)  # effective T
    
    # members: sorted list of initial positions (0-indexed)
    # P: list of brigadeiros per plate (0-indexed)
    
    max_val = 9 * K + 1
    INF = float('inf')
    
    # dp[j][v] = min cost to place members 0..i with member i at pos j, total value = v
    # Initialize for i=0 (first member)
    
    # Use numpy arrays for efficiency
    # dp shape: (N, max_val)
    
    dp = np.full((N, max_val), 10**9, dtype=np.int64)
    
    # Place member 0 at position j (j >= 0)
    for j in range(N):
        cost = abs(members[0] - j)
        v = P[j]
        if cost <= T_eff and v < max_val:
            if cost < dp[j][v]:
                dp[j][v] = cost
    
    # Process members 1..K-1
    for i in range(1, K):
        new_dp = np.full((N, max_val), 10**9, dtype=np.int64)
        
        # prefix_min[j'][v] = min over j''<=j' of dp[j''][v]
        # We need min over j' < j, so we compute prefix min up to j-1
        
        # prefix_min[v] updated as we go
        prefix_min = np.full(max_val, 10**9, dtype=np.int64)
        
        for j in range(N):
            # Update new_dp[j][v] = cost_i(j) + min over j'<j of dp[j'][v - P[j]]
            cost_j = abs(members[i] - j)
            pj = P[j]
            
            if pj < max_val:
                # new_dp[j][v] = cost_j + prefix_min[v - pj] for v >= pj
                # i.e., new_dp[j][pj:] = cost_j + prefix_min[:max_val-pj]
                candidates = prefix_min[:max_val - pj]
                # Add cost_j where candidates < INF
                vals = candidates + cost_j
                # Only update where vals <= T_eff
                new_dp[j][pj:] = np.minimum(new_dp[j][pj:], vals)
            
            # Update prefix_min with dp[j] (for next j+1)
            prefix_min = np.minimum(prefix_min, dp[j])
        
        dp = new_dp
    
    # Find max v such that min cost over all j <= T_eff
    min_cost_per_v = dp.min(axis=0)  # shape (max_val,)
    
    ans = 0
    for v in range(max_val - 1, -1, -1):
        if min_cost_per_v[v] <= T_eff:
            ans = v
            break
    
    print(ans)

solve()
```

Wait, I need to reconsider. Let me trace through the examples to verify my approach, then clean up.

```python
import sys
import numpy as np

def solve():
    data = sys.stdin.read().split()
    idx = 0
    N, K, T = int(data[idx]), int(data[idx+1]), int(data[idx+2])
    idx += 3
    P = [int(data[idx+i]) for i in range(N)]
    idx += N
    G = [int(data[idx+i]) for i in range(N)]
    
    members = [i for i in range(N) if G[i] == 1]
    
    T_eff = min(T, K * N)
    max_val = 9 * K + 1
    
    INF = 10**9
    
    dp = np.full((N, max_val), INF, dtype=np.int64)
    
    for j in range(N):
        cost = abs(members[0] - j)
        v = P[j]
        if cost < dp[j][v]:
            dp[j][v] = cost
    
    for i in range(1, K):
        new_dp = np.full((N, max_val), INF, dtype=np.int64)
        prefix_min = np.full(max_val, INF, dtype=np.int64)
        
        for j in range(N):
            cost_j = abs(members[i] - j)
            pj = P[j]
            
            if max_val - pj > 0:
                candidates = prefix_min[:max_val - pj].copy()
                mask = candidates < INF
                if mask.any():
                    vals = np.where(mask, candidates + cost_j, INF)
                    new_dp[j][pj:pj + len(vals)] = np.minimum(new_dp[j][pj:pj + len(vals)], vals)
            
            prefix_min = np.minimum(prefix_min, dp[j])
        
        dp = new_dp
    
    min_cost_per_v = dp.min(axis=0)
    
    ans = 0
    for v in range(max_val - 1, -1, -1):
        if min_cost_per_v[v] <= T_eff:
            ans = v
            break
    
    print(ans)

solve()
```