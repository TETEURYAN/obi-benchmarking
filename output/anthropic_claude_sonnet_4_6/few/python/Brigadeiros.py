import sys

def solve():
    data = sys.stdin.read().split()
    idx = 0
    N = int(data[idx]); idx+=1
    K = int(data[idx]); idx+=1
    T = int(data[idx]); idx+=1
    
    P = [int(data[idx+i]) for i in range(N)]; idx+=N
    G = [int(data[idx+i]) for i in range(N)]; idx+=N
    
    # positions of group members (0-indexed)
    members = [i for i in range(N) if G[i] == 1]
    # K members
    
    # Key insight: members cannot pass through each other (they swap with neighbors,
    # but two group members can't occupy same position, and relative order is preserved).
    # So we need to assign K members to K positions (maintaining relative order),
    # choosing a contiguous or non-contiguous subset of positions, 
    # with total movement cost <= T.
    
    # The cost for member j (originally at members[j]) to move to position pos[j]
    # is |members[j] - pos[j]|, BUT we need to account for the fact that members
    # block each other. Since relative order is preserved, if we assign member j
    # to target position t[j] where t[0] < t[1] < ... < t[K-1], the actual swap
    # cost is sum of |members[j] - t[j]| BUT we need to be careful about crossings.
    # Actually, since members maintain relative order, the minimum cost to move
    # member j to t[j] (with t strictly increasing) is indeed sum |members[j] - t[j]|
    # as long as t[j] are distinct and ordered. This is a known result.
    
    # DP: dp[j][last_pos][swaps_used] - but swaps can be up to 1e9
    # Better: dp[j][last_pos] = minimum swaps to place first j+1 members with last one at last_pos
    # Then check if min_swaps <= T and maximize sum of P[t[j]]
    
    # N<=300, K<=300
    # dp[j][p] = min cost to assign first j members to positions, with j-th at position p
    # We want to maximize sum of brigadeiros subject to cost <= T
    
    # Alternative: dp[j][p] = min cost to place members 0..j with member j at position p
    # Then answer = max over all valid assignments with cost <= T of sum P[t[j]]
    
    # But we need to track both cost and sum. 
    # dp[j][p] = min cost to place first j+1 members (0-indexed) ending at position p,
    #            for each possible total brigadeiro sum
    # This is too much.
    
    # Better approach: since N<=300, K<=300, positions<=300
    # dp[j][p] = min swaps needed to place first j members with j-th member at position p,
    #            maximizing brigadeiros - but we need to track brigadeiros too.
    
    # Let's do: dp[j][p] = for each (j, p), store min cost achieving maximum brigadeiros
    # Not straightforward.
    
    # Standard approach: dp[j][p] = min cost to assign member j to position p (0-indexed positions)
    # with members 0..j assigned optimally. But we want max brigadeiros with cost<=T.
    
    # dp[j][p][s] = is it possible to assign first j+1 members ending at p with sum s and cost <= T?
    # s <= 9*300 = 2700, j<=300, p<=300 => 300*300*2700 ~ 2.4*10^8 too much
    
    # Better: dp[j][p] = min cost to place first j+1 members with j-th at position p, 
    #                    given we pick the best brigadeiros
    # We want max sum subject to cost<=T, so:
    # dp[j][p] = min cost to achieve a certain sum... 
    
    # Let's do dp[j][p] = array where dp[j][p][s] = min cost to place members 0..j 
    # with j-th at p and total brigadeiros = s. Then answer = max s where min over p of dp[K-1][p][s] <= T
    
    # Dimensions: K * N * (9*N+1) = 300 * 300 * 2701 ~ 2.4*10^8 - might be tight but let's try with numpy or optimize
    
    # Actually max sum = 9*300=2700, K<=300, N<=300
    # Use dp[p][s] = min cost, iterate over members
    
    INF = float('inf')
    max_sum = 9 * N
    
    # dp[p][s] = min cost to place members 0..j with j-th at position p, sum of brigadeiros = s
    # Initialize for j=0 (first member at position members[0])
    
    dp = [[INF] * (max_sum + 1) for _ in range(N)]
    
    m0 = members[0]
    for p in range(N):
        cost = abs(p - m0)
        s = P[p]
        if cost < dp[p][s]:
            dp[p][s] = cost
    
    for j in range(1, K):
        new_dp = [[INF] * (max_sum + 1) for _ in range(N)]
        mj = members[j]
        for prev_p in range(N):
            for s in range(max_sum + 1):
                if dp[prev_p][s] == INF:
                    continue
                prev_cost = dp[prev_p][s]
                # next position must be > prev_p
                for p in range(prev_p + 1, N):
                    cost = prev_cost + abs(p - mj)
                    ns = s + P[p]
                    if ns > max_sum:
                        ns = max_sum  # won't happen since P[p]<=9 and we track correctly
                    if cost < new_dp[p][ns]:
                        new_dp[p][ns] = cost
        dp = new_dp
    
    ans = 0
    for p in range(N):
        for s in range(max_sum + 1):
            if dp[p][s] <= T:
                if s > ans:
                    ans = s
    
    print(ans)

solve()