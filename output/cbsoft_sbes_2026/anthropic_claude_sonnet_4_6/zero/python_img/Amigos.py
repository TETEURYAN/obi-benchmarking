import sys
from itertools import permutations

def solve():
    input_data = sys.stdin.read().split()
    idx = 0
    N = int(input_data[idx]); idx += 1
    K = int(input_data[idx]); idx += 1
    
    a = []
    for i in range(N):
        a.append(int(input_data[idx])); idx += 1
    
    b = []
    for i in range(N):
        b.append(int(input_data[idx])); idx += 1
    
    # positions of friends (1-indexed)
    top = [i+1 for i in range(N) if a[i] == 1]  # K positions
    bot = [i+1 for i in range(N) if b[i] == 1]  # K positions
    
    # We need to choose K positions (a subset of size K from N positions)
    # such that top friends move to those positions and bot friends move to same positions
    # minimizing total swaps.
    
    # Number of swaps to move a sorted sequence of elements to target positions
    # equals sum of |pos[i] - target[i]| when both are sorted (optimal matching).
    
    # We need to find K positions p1 < p2 < ... < pK such that
    # cost(top -> positions) + cost(bot -> positions) is minimized.
    
    # cost to move sorted array src to sorted array dst = sum |src[i] - dst[i]|
    
    # The optimal set of meeting positions: we need to choose K positions from 1..N
    # This is a DP problem.
    
    # DP: dp[i][j] = min swaps using first i positions considered, having chosen j meeting spots
    # For each chosen position p, top[j] moves to p and bot[j] moves to p
    # top and bot are sorted, so we match them in order.
    
    # dp[j] after processing positions = min cost of assigning j pairs
    # When we pick position p as the j-th meeting spot:
    # cost += |top[j-1] - p| + |bot[j-1] - p|
    
    # We iterate over all possible positions 1..N and decide which K to pick.
    
    # dp[j] = min cost having chosen j meeting positions so far
    # Transition: for position p (in order), dp[j] = min(dp[j-1] + |top[j-1]-p| + |bot[j-1]-p|)
    
    # But we need p to be chosen in increasing order and we need exactly K chosen from N positions.
    # Also the j-th chosen position must be >= j (at least j positions available)
    # and <= N - (K - j) (at least K-j positions remaining)
    
    INF = float('inf')
    
    # dp[j] = minimum cost having selected j meeting positions
    # We process positions 1..N left to right
    
    dp = [INF] * (K + 1)
    dp[0] = 0
    
    for p in range(1, N + 1):
        # Process position p, update dp in reverse to avoid using p twice
        new_dp = dp[:]
        for j in range(1, K + 1):
            if dp[j-1] < INF:
                cost = abs(top[j-1] - p) + abs(bot[j-1] - p)
                if dp[j-1] + cost < new_dp[j]:
                    new_dp[j] = dp[j-1] + cost
        dp = new_dp
    
    print(dp[K])

solve()