import sys

# Increase recursion limit as per guidelines, though not strictly needed for this iterative solution
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
        C = int(next(iterator))
        A = [int(next(iterator)) for _ in range(N)]
    except StopIteration:
        return

    total_sum = sum(A)

    # Optimization for C=1:
    # We simply need to pick the K smallest elements to cover (minimize covered sum).
    if C == 1:
        A.sort()
        min_covered_sum = sum(A[:K])
        print(total_sum - min_covered_sum)
        return

    # DP Approach for C > 1
    # dp[k] will store the minimum sum of covered squares using exactly k labels
    # processed up to the current position.
    # We use a circular buffer 'history' to store dp states to handle the non-overlapping constraint.
    # history[i % C] stores the dp state at index i.
    
    # Prefix sums for efficient range sum calculation
    P = [0] * (N + 1)
    for i in range(N):
        P[i+1] = P[i] + A[i]

    # Initialize DP table with infinity
    inf = float('inf')
    
    # current_dp represents the state at the previous index (i-1)
    current_dp = [inf] * (K + 1)
    current_dp[0] = 0
    
    # history buffer
    history = [None] * C
    history[0] = current_dp
    
    # Iterate through the tape
    for i in range(1, N + 1):
        # Initialize new_dp with the state from i-1 (case where we don't cover A[i-1])
        new_dp = list(current_dp)
        
        # If we can place a label ending at i-1
        if i >= C:
            # Calculate sum of the segment A[i-C ... i-1]
            seg_sum = P[i] - P[i-C]
            
            # Retrieve the state from i-C
            prev_dp = history[(i - C) % C]
            
            # Update new_dp by considering placing a label ending here
            # We can add this segment to any solution from prev_dp with k-1 labels
            # Optimization: limit the loop to the maximum possible labels at index i
            limit = K
            if i // C < K:
                limit = i // C
                
            # Local variables for speed
            pd = prev_dp
            nd = new_dp
            ss = seg_sum
            
            for k in range(1, limit + 1):
                # If prev_dp[k-1] is reachable
                if pd[k-1] != inf:
                    val = pd[k-1] + ss
                    if val < nd[k]:
                        nd[k] = val
        
        # Store the current state in history
        history[i % C] = new_dp
        
        # Update current_dp for the next iteration
        current_dp = new_dp

    # The result is Total Sum - Min Covered Sum
    print(total_sum - current_dp[K])

if __name__ == '__main__':
    solve()