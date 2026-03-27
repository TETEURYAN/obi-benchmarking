import sys

# Increase recursion depth just in case, though not needed for this iterative solution.
sys.setrecursionlimit(200000)

def solve():
    # Use fast I/O
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    iterator = iter(input_data)
    
    try:
        N = int(next(iterator))
        K = int(next(iterator))
        T = int(next(iterator))
    except StopIteration:
        return

    # Read P (brigadeiros counts)
    P = [0] * (N + 1)
    for i in range(1, N + 1):
        P[i] = int(next(iterator))
    
    # Read G (group members initial positions)
    # We need to extract the indices where G[i] == 1
    # There are exactly K such indices.
    pos = [0] * (K + 1)
    current_k = 1
    for i in range(1, N + 1):
        g_val = int(next(iterator))
        if g_val == 1:
            pos[current_k] = i
            current_k += 1
            
    # Maximum possible sum of brigadeiros is K * 9
    max_val = 9 * K
    
    # dp[j][v] will store the minimum cost to achieve value v
    # with the first k members, such that the k-th member is at position j.
    # We use a 2D array. Dimensions: (N+1) x (max_val + 1)
    # Initialize with infinity (a value larger than any possible cost)
    INF = 1000000000000000
    
    # Current dp table
    # We initialize dp for k=0 members.
    # To have 0 members, we can consider a virtual position 0.
    # dp[0][0] = 0 cost to get 0 value with 0 members at position 0.
    # Note: We will manage the 'k' dimension by updating the table iteratively.
    
    # We can use a single table and update it, but the dependency is on the previous k.
    # So we need prev_dp and curr_dp.
    
    prev_dp = [[INF] * (max_val + 1) for _ in range(N + 1)]
    prev_dp[0][0] = 0
    
    # Iterate for each member from 1 to K
    for k in range(1, K + 1):
        curr_dp = [[INF] * (max_val + 1) for _ in range(N + 1)]
        
        # min_prev[v] stores the minimum cost to achieve value v
        # using the first k-1 members, ending at any position p < j.
        # We maintain this array as we iterate j from left to right.
        
        # Initialize min_prev with the state from prev_dp[0] (virtual start)
        # For k=1, valid previous positions are 0.
        # For k>1, valid previous positions start at k-1.
        # However, the loop for j starts at k. So j-1 >= k-1.
        # We initialize min_prev with prev_dp[k-1] effectively.
        # But simpler: initialize with prev_dp[0] (which is INF for k>1 except for k=1 case logic handled implicitly)
        # Actually, let's just initialize min_prev with infinity and update it.
        
        min_prev = [INF] * (max_val + 1)
        
        # The first valid position for member k is k.
        # The minimum valid previous position for member k-1 is k-1.
        # So before processing j=k, min_prev should represent min over prev_dp[p] for p < k.
        # Which is just prev_dp[k-1].
        
        # Let's refine the initialization of min_prev
        # If k=1, we iterate j from 1. min_prev starts as prev_dp[0].
        # If k=2, we iterate j from 2. min_prev should start as prev_dp[1].
        # So we set min_prev = prev_dp[k-1]
        
        # Copy values
        for v in range(max_val + 1):
            min_prev[v] = prev_dp[k-1][v]
            
        # Iterate j from k to N
        for j in range(k, N + 1):
            cost_move = abs(pos[k] - j)
            val_at_j = P[j]
            
            # Calculate curr_dp[j]
            # curr_dp[j][v] = cost_move + min_prev[v - P[j]]
            # We only update if v >= P[j]
            
            # Optimization: Slice operations are faster in Python
            # We update curr_dp[j][val_at_j : max_val + 1]
            # source is min_prev[0 : max_val + 1 - val_at_j]
            
            # Using list comprehension for speed
            if val_at_j == 0:
                # If val is 0, just add cost_move to min_prev
                # But we need to take min with existing INF
                # curr_dp[j] starts as INF
                # So we just assign
                # Actually, if val=0, v-v_j = v.
                # curr_dp[j][v] = cost_move + min_prev[v]
                new_vals = [cost_move + x for x in min_prev]
                # Assign to curr_dp[j]
                # Since curr_dp[j] is all INF, we can just write
                curr_dp[j] = new_vals
            else:
                # v ranges from val_at_j to max_val
                # index in min_prev ranges from 0 to max_val - val_at_j
                len_range = max_val + 1 - val_at_j
                new_vals = [cost_move + min_prev[i] for i in range(len_range)]
                # Write into curr_dp[j] starting at index val_at_j
                # In python: curr_dp[j][val_at_j:] = new_vals
                # This assignment is efficient
                curr_dp[j][val_at_j:] = new_vals
            
            # Update min_prev with prev_dp[j]
            # min_prev[v] = min(min_prev[v], prev_dp[j][v])
            # We can use a loop or list comprehension
            # Since we need element-wise min:
            row_prev = prev_dp[j]
            # Manual loop is sometimes faster than zip for simple types if not careful,
            # but let's try to be clean.
            # Actually, updating min_prev is crucial.
            for v_idx in range(max_val + 1):
                if row_prev[v_idx] < min_prev[v_idx]:
                    min_prev[v_idx] = row_prev[v_idx]
        
        prev_dp = curr_dp

    # After processing all K members, find the max value v such that min cost <= T
    # The final min_prev after the loop j=N contains the min cost over all valid positions for the last member
    # Actually, min_prev accumulates min(prev_dp[p]) for p <= N.
    # So min_prev now holds the minimum costs for each value v.
    
    ans = 0
    for v in range(max_val, -1, -1):
        if min_prev[v] <= T:
            ans = v
            break
            
    print(ans)

if __name__ == '__main__':
    solve()