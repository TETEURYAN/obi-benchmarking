import sys

# Increase recursion depth just in case, though we use iterative DP here.
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
    except StopIteration:
        return

    dolls = []
    for _ in range(N):
        try:
            dolls.append(int(next(iterator)))
        except StopIteration:
            break
            
    # Sort the doll sizes
    dolls.sort()
    
    # DP initialization
    # We use a rolling array (modulo 3) to save space
    # dp[i % 3][j] stores the min cost to form j triples using dolls from index i to N-1
    # Initialize with infinity
    INF = float('inf')
    
    # We only need 3 rows: current i, i+1, i+2
    # Initialize all with infinity
    dp = [[INF] * (K + 1) for _ in range(3)]
    
    # Base case: forming 0 triples costs 0
    # For any index i, dp[i][0] = 0
    # Since we iterate backwards, we set dp[i%3][0] = 0 at each step
    # Also, for i = N (empty suffix), cost is 0 for 0 triples, inf otherwise.
    # This is naturally handled if we initialize dp arrays correctly.
    
    # Initialize the state for i = N and i = N+1
    # These are needed for the transitions from i = N-1 and i = N-2
    # dp[N % 3] corresponds to i = N
    for x in range(3):
        dp[x][0] = 0
        
    # Iterate backwards from N-1 down to 0
    for i in range(N - 1, -1, -1):
        curr = i % 3
        nxt = (i + 1) % 3
        nnxt = (i + 2) % 3
        
        # Reset current row for new calculation
        # We need to reset because we are reusing the array index
        # dp[curr][0] should be 0, others INF initially
        for j in range(K + 1):
            dp[curr][j] = INF
        dp[curr][0] = 0
        
        # Calculate the maximum number of triples possible with remaining dolls
        # remaining_dolls = N - i
        # max_k_possible = remaining_dolls // 3
        # We only need to calculate up to K
        limit = (N - i) // 3
        
        # Iterate j from 1 to min(K, limit)
        upper_bound = min(K, limit)
        
        for j in range(1, upper_bound + 1):
            # Option 1: Skip the current doll i
            # It can be used as a third doll for a triple to the left, or unused.
            # We look for solution for j triples starting from i+1
            # This is valid only if (N - (i+1)) >= 3j  => N - i - 1 >= 3j
            # Since we are in loop j <= (N-i)//3, let's check strict validity
            # If N - i == 3j, then N - i - 1 < 3j, so skip is not possible (not enough dolls).
            # However, dp[nxt][j] would be INF in that case, so min() handles it.
            res = dp[nxt][j]
            
            # Option 2: Pair doll i with doll i+1
            # Valid if i+1 < N
            if i + 1 < N:
                cost_pair = (dolls[i+1] - dolls[i])**2
                prev_cost = dp[nnxt][j-1]
                
                # Check if prev_cost is not INF to avoid overflow/incorrect addition
                if prev_cost != INF:
                    # We need to ensure that we can assign a third doll to this pair.
                    # The third doll must be from indices > i+1.
                    # The number of available dolls in suffix i+2...N-1 is N - (i+2).
                    # We need to form j-1 triples from that suffix.
                    # Total dolls used in suffix: 3*(j-1).
                    # Remaining dolls in suffix: (N - i - 2) - 3*(j-1).
                    # We need at least 1 remaining doll to serve as the third for current pair.
                    # Condition: N - i - 2 - 3j + 3 >= 1  => N - i >= 3j.
                    # This matches our loop limit condition.
                    # So if we are here, a third doll is theoretically available.
                    res = min(res, cost_pair + prev_cost)
            
            dp[curr][j] = res

    # The result is stored in dp[0][K]
    print(dp[0][K])

if __name__ == '__main__':
    solve()