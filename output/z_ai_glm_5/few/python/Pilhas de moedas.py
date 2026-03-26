import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    iterator = iter(input_data)
    try:
        N = int(next(iterator))
        K = int(next(iterator))
        P = []
        for _ in range(N):
            P.append(int(next(iterator)))
    except StopIteration:
        return

    # If K is greater or equal to N, we can have 0 coins added by making each pile distinct
    # or keeping them as is. Since we can only add coins, if there are duplicates,
    # we can just not add anything to them, or add to make them distinct.
    # Actually, if K >= N, we can just leave the array as is (or add 0 coins to make all distinct).
    # The number of distinct values initially is <= N <= K.
    # So 0 coins are needed.
    if K >= N:
        print(0)
        return

    P.sort()
    
    # Prefix sums
    S = [0] * (N + 1)
    for i in range(N):
        S[i + 1] = S[i] + P[i]
    
    # dp[j][i] = min cost to partition first i elements into j groups
    # We only need the previous row to calculate the current row
    # Initialize dp table with infinity
    dp_prev = [float('inf')] * (N + 1)
    
    # Base case: 1 group
    # Cost to merge P[0...i-1] into 1 group is sum(P[i-1] - P[k]) for k in 0..i-1
    # Which equals i * P[i-1] - S[i]
    for i in range(1, N + 1):
        dp_prev[i] = i * P[i - 1] - S[i]
        
    # The answer for K=1 is dp_prev[N]
    ans = dp_prev[N]
    
    # Iterate for j = 2 to K
    for j in range(2, K + 1):
        dp_curr = [float('inf')] * (N + 1)
        
        # Convex Hull Trick structures
        # Lines are stored as (m, c)
        # We need a deque
        dq = []
        
        # For j groups, we need at least j elements.
        # The transition is dp[j][i] = min(dp[j-1][k] + cost(k+1, i)) for k < i
        # cost(k+1, i) = (i - k) * P[i-1] - (S[i] - S[k])
        # dp[j][i] = min( (dp[j-1][k] + S[k] - k*P[i-1]) + i*P[i-1] - S[i] )
        # Let m = -k, x = P[i-1], c = dp[j-1][k] + S[k]
        # We want to minimize m*x + c.
        # Slopes m are added in decreasing order (-1, -2, -3...).
        # Queries x are processed in increasing order (P is sorted).
        
        # We start by adding the line corresponding to k = j-1
        # dp[j-1][j-1] must be valid. 
        # For j=2, k=1. dp[1][1] is valid.
        
        # Add line for k = j - 1
        m_init = -(j - 1)
        c_init = dp_prev[j - 1] + S[j - 1]
        dq.append((m_init, c_init))
        
        for i in range(j, N + 1):
            # Query for x = P[i-1]
            x = P[i - 1]
            
            # Pop from front while next line gives better value
            while len(dq) >= 2:
                m1, c1 = dq[0]
                m2, c2 = dq[1]
                # Check if m1*x + c1 >= m2*x + c2
                # Since m1 > m2 (slopes are decreasing), m1 - m2 > 0
                # x >= (c2 - c1) / (m1 - m2)
                # Use cross multiplication to avoid floats
                if x * (m1 - m2) >= c2 - c1:
                    dq.pop(0)
                else:
                    break
            
            # Calculate min value
            m_best, c_best = dq[0]
            min_val = m_best * x + c_best
            
            # Calculate dp[j][i]
            dp_curr[i] = min_val + i * P[i - 1] - S[i]
            
            # Add line for k = i
            # This line will be used for future i' > i
            m_new = -i
            c_new = dp_prev[i] + S[i]
            
            # Add to back, maintain convex hull
            # If the new line makes the previous line obsolete, pop it
            while len(dq) >= 2:
                # Let lines be l1, l2, l3 (l3 is new)
                # l1 = dq[-2], l2 = dq[-1], l3 = new
                m1, c1 = dq[-2]
                m2, c2 = dq[-1]
                m3, c3 = m_new, c_new
                
                # Check if l2 is bad
                # Intersection(l1, l2) >= Intersection(l2, l3)
                # (c2 - c1)(m2 - m3) >= (c3 - c2)(m1 - m2)
                # Note: m1 > m2 > m3, so m1 - m2 > 0 and m2 - m3 > 0
                if (c2 - c1) * (m2 - m3) >= (c3 - c2) * (m1 - m2):
                    dq.pop()
                else:
                    break
            dq.append((m_new, c_new))
            
        dp_prev = dp_curr
        if dp_prev[N] < ans:
            ans = dp_prev[N]

    print(ans)

if __name__ == '__main__':
    solve()