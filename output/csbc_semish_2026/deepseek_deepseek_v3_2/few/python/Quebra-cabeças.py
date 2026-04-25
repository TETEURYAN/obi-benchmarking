import sys

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return

    N = int(data[0])
    M1_line = data[1]
    M1 = int(M1_line)
    X1 = list(map(int, data[2:2+M1]))
    idx = 2+M1
    M2_line = data[idx]
    M2 = int(M2_line)
    X2 = list(map(int, data[idx+1:idx+1+M2]))

    # Add zeros to make lists of length N
    A = [0] * N
    B = [0] * N
    for i, val in enumerate(X1):
        A[i] = val
    for i, val in enumerate(X2):
        B[i] = val

    # DP[i][j] = maximum sum using first i non-zero tokens from A and first j non-zero tokens from B
    non_zero_A = [v for v in A if v != 0]
    non_zero_B = [v for v in B if v != 0]
    kA = len(non_zero_A)
    kB = len(non_zero_B)

    DP = [[0]*(kB+1) for _ in range(kA+1)]
    for i in range(kA+1):
        for j in range(kB+1):
            if i == 0 and j == 0:
                DP[i][j] = 0
                continue
            best = -10**18
            # We can place the i-th token from A (if i>0) somewhere, and match with some token from B
            # Actually, we need to consider all possible placements of tokens in columns 0..N-1
            # But DP over counts of tokens placed is simpler: DP[i][j] = max over placing token i from A and token j from B
            if i > 0:
                # Try to pair token i from A with token j from B (if j>0) in some column
                # The column index is max(i-1, j-1) because tokens are placed left to right
                col = max(i-1, j-1)
                if col < N:
                    if j > 0:
                        best = max(best, DP[i-1][j-1] + non_zero_A[i-1]*non_zero_B[j-1])
                    else:
                        # Token from A placed alone
                        best = max(best, DP[i-1][j] + non_zero_A[i-1]*0)
            if j > 0:
                # Token from B placed alone
                best = max(best, DP[i][j-1] + 0*non_zero_B[j-1])
            DP[i][j] = best

    ans = DP[kA][kB]
    print(ans)

if __name__ == "__main__":
    main()