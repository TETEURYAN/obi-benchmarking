import sys
sys.setrecursionlimit(200000)
MOD = 1_000_000_007

def solve() -> None:
    data = sys.stdin.read().split()
    if not data:
        return
    N_str = data[0]
    S = data[1]
    len_S = len(S)

    # Preprocess N: we only need its length and numeric value for comparisons
    N_len = len(N_str)
    N_int = int(N_str)  # N < 10^100, but Python handles big integers

    # DP array: dp[i] = number of ways to split S[i:]
    dp = [0] * (len_S + 1)
    dp[len_S] = 1  # base case: empty suffix has one way (do nothing)

    # Precompute powers of 10 for fast substring to int conversion
    # We only need up to N_len digits
    pow10 = [1] * (N_len + 1)
    for i in range(1, N_len + 1):
        pow10[i] = pow10[i-1] * 10

    # Helper to convert substring S[l:r] to int quickly
    # We'll use incremental computation while iterating
    # We'll store the numeric value of the substring starting at i with length L
    # But since N can be up to 10^100, we must compare as strings for lengths > 19
    # (since 10^19 > 2^63, but Python big ints are fine, but for performance we avoid big ints when possible)

    # We'll compare lexicographically when lengths differ, numerically when same length
    # Precompute the integer value of each digit
    digits = [int(ch) for ch in S]

    # Iterate from end to start
    for i in range(len_S - 1, -1, -1):
        total = 0
        # Try all possible substring lengths from 1 to min(N_len, len_S - i)
        # But also, the substring must not have leading zero
        if digits[i] == 0:
            dp[i] = 0
            continue

        # Build the substring value incrementally
        curr_val = 0
        max_len = min(N_len, len_S - i)
        for length in range(1, max_len + 1):
            # Append next digit
            curr_val = curr_val * 10 + digits[i + length - 1]
            # Check if curr_val <= N_int
            if curr_val <= N_int:
                total = (total + dp[i + length]) % MOD
            else:
                # Since digits are processed in increasing length,
                # once curr_val > N, longer lengths will also be > N (because no leading zeros)
                break
        dp[i] = total % MOD

    print(dp[0] % MOD)

if __name__ == "__main__":
    solve()