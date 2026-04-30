
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
    
    # positions of group members (0-indexed)
    members = [i for i in range(N) if G[i] == 1]
    # K members
    
    # We need to assign K members to K positions (subset of N positions)
    # such that the total cost (swaps needed) <= T and total brigadeiros is maximized.
    
    # Key insight: members maintain relative order (they can't pass through each other
    # without cost, but actually they CAN pass through each other - wait, no.
    # Members swap with non-members. Two members can't swap with each other directly
    # in this problem? Actually re-reading: "cada membro do grupo pode pedir para trocar 
    # de lugar com um dos alunos sentados nas cadeiras vizinhas"
    # The others always accept. But what if two group members are adjacent?
    # They could swap with each other too, but that doesn't help.
    # The key insight for competitive programming: the optimal assignment preserves
    # the relative order of members. So member i goes to position j[i] where j is sorted.
    
    # The minimum number of swaps to move members from positions members[] to targets[]
    # (both sorted) is sum of |members[i] - targets[i]| BUT we need to account for
    # the fact that members block each other.
    
    # Actually the minimum swaps when members maintain relative order:
    # cost = sum |members[i] - targets[i]| but members can't cross each other.
    # If we assign sorted members to sorted targets, the cost is sum |members[i] - targets[i]|
    # This is the standard result.
    
    # So: choose K positions from N (0-indexed), sort them as t[0]<t[1]<...<t[K-1]
    # cost = sum_{i=0}^{K-1} |members[i] - t[i]|
    # maximize sum P[t[i]] subject to cost <= T
    
    # N <= 300, K <= 300
    # DP: dp[i][j] = min cost to assign first j members to j positions chosen from first i positions
    # Then check if sum of brigadeiros is achievable.
    
    # Better: dp over positions and members
    # dp[j][m] = minimum cost when we've considered first j positions (0..j-1) and assigned m members
    # to some of those positions.
    # Transition: either position j is not chosen: dp[j+1][m] = dp[j][m]
    # or position j is chosen as the m-th target (0-indexed m): 
    #   dp[j+1][m+1] = dp[j][m] + |members[m] - j|
    
    # Then for each subset size m=K, dp[N][K] gives min cost for some assignment.
    # But we want to maximize brigadeiros, so we need to track which positions are chosen.
    
    # Alternative DP: 
    # dp[j][m] = max brigadeiros using first j positions, having assigned m members,
    #            with minimum cost among all such assignments achieving that max.
    # This is tricky.
    
    # Better: dp[j][m] = for each possible total brigadeiros value, min cost
    # Max brigadeiros = 9*300 = 2700, N=300, K=300
    # dp[j][m][b] = min cost considering first j positions, m assigned, b brigadeiros
    # That's 300*300*2700 = too large? 300*300*2700 = 243,000,000 - too much.
    
    # Simpler: dp[j][m] = min cost to pick m targets from first j positions for first m members
    # Then we want max sum P[targets] with cost <= T.
    # We can do: dp[j][m] = list of (cost, brigadeiros) pareto-optimal pairs? 
    
    # Since max brigadeiros = 2700, dp[j][m] = array of size 2701 where dp[j][m][b] = min cost to get b brigadeiros
    
    INF = float('inf')
    max_b = 9 * N
    # dp[m][b] = min cost to assign m members to m chosen positions with total b brigadeiros
    # considering positions 0..j-1
    
    dp = [[INF] * (max_b + 1) for _ in range(K + 1)]
    dp[0][0] = 0
    
    for j in range(N):
        # iterate in reverse to avoid using position j twice
        new_dp = [row[:] for row in dp]
        for m in range(K - 1, -1, -1):
            for b in range(max_b + 1 - P[j]):
                if dp[m][b] < INF:
                    cost = dp[m][b] + abs(members[m] - j)
                    nb = b + P[j]
                    if cost < new_dp[m+1][nb]:
                        new_dp[m+1][nb] = cost
        dp = new_dp
    
    ans = 0
    for b in range(max_b + 1):
        if dp[K][b] <= T:
            ans = b
    
    print(ans)

solve()
