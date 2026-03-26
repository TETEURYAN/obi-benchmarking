import sys

# Set recursion limit just in case, though not needed for iterative DP
sys.setrecursionlimit(200000)

def solve():
    # Read all input from stdin
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return

    # First token is N (as a string to handle large values)
    N_str = input_data[0]
    # Second token is the sequence S
    S = input_data[1]
    
    MOD = 1000000007
    
    # D is the number of digits in N
    D = len(N_str)
    # L is the length of the sequence S
    L = len(S)
    
    # dp[i] stores the number of valid ways to parse the prefix S[0...i-1]
    # We need an array of size L + 1
    dp = [0] * (L + 1)
    dp[0] = 1  # Empty prefix has 1 way (base case)
    
    # sum_short maintains the sum of dp[j] for the window of indices j that
    # result in a substring length strictly less than D.
    # Specifically, for current i, valid j's are in [i - D + 1, i - 1].
    # Since length < D, the value is automatically <= N (as N has D digits).
    # We only include dp[j] if S[j] != '0' (no leading zeros).
    sum_short = 0
    
    # Initialize sum_short for the first iteration (i=1)
    # The valid range for i=1 is j in [1-D+1, 0]. Since j >= 0, only j=0 is possible.
    # This is only relevant if D > 1 (since if D=1, length < 1 is impossible).
    if D > 1:
        # If S[0] is not '0', dp[0] contributes to sum_short
        if S[0] != '0':
            sum_short = dp[0]
            
    # Iterate through the string to compute dp values
    for i in range(1, L + 1):
        res = 0
        
        # 1. Add contributions from substrings of length < D
        # These are handled by sum_short
        res = sum_short
        
        # 2. Check contribution from substring of length exactly D
        # The substring would be S[j...i-1] where j = i - D
        if i >= D:
            j = i - D
            # Check for leading zero
            if S[j] != '0':
                # Extract substring for comparison
                # Since D <= 100, slicing is efficient enough
                sub = S[j:i]
                # Check if sub <= N_str
                # Lengths are equal, so lexicographical comparison works for numerical value
                if sub <= N_str:
                    res = (res + dp[j]) % MOD
        
        # Store the result
        dp[i] = res % MOD
        
        # Update sum_short for the next iteration (i + 1)
        # The window of valid j's slides forward.
        # We need to remove j = i - D + 1 (if it exists and was valid)
        # and add j = i (if it is valid)
        
        # The index to remove from the left of the window
        remove_idx = i - D + 1
        if remove_idx >= 0:
            # If S[remove_idx] was not '0', it was part of the sum
            if S[remove_idx] != '0':
                sum_short = (sum_short - dp[remove_idx]) % MOD
        
        # The index to add to the right of the window
        # For the next step i+1, the new rightmost j is i.
        # This j corresponds to a substring of length 1 (S[i]), which is < D if D > 1.
        # We only add if i < L (since we access S[i]) and S[i] != '0'
        if i < L:
            if S[i] != '0':
                sum_short = (sum_short + dp[i]) % MOD
                
    print(dp[L])

if __name__ == '__main__':
    solve()