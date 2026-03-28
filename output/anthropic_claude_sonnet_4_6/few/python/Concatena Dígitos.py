import sys

def main():
    data = sys.stdin.buffer.read().split()
    idx = 0
    N = int(data[idx]); idx += 1
    Q = int(data[idx]); idx += 1
    
    D = [int(data[idx + i]) for i in range(N)]
    idx += N
    
    # Potential of interval [L, R] (0-indexed: l to r)
    # For each pair (i, j) with i != j in [l, r]:
    # concatenation = D[i] * 10 + D[j]
    # Sum over all ordered pairs (i,j), i!=j:
    # = sum_{i!=j} (D[i]*10 + D[j])
    # = 10 * sum_{i!=j} D[i] + sum_{i!=j} D[j]
    # = 10 * (n-1) * S + (n-1) * S   where S = sum of D in range, n = count
    # = 11 * (n-1) * S
    # Wait let me verify:
    # sum_{i!=j} D[i] = sum_i D[i] * (n-1) = (n-1)*S
    # sum_{i!=j} D[j] = sum_j D[j] * (n-1) = (n-1)*S
    # Total = 10*(n-1)*S + (n-1)*S = 11*(n-1)*S
    
    # Verify with example: list [1,1,2], S=4, n=3
    # 11 * 2 * 4 = 88. Correct!
    
    # list [1,1,2,3,9], S=16, n=5
    # 11 * 4 * 16 = 704. Correct!
    
    # So we just need prefix sums
    prefix = [0] * (N + 1)
    for i in range(N):
        prefix[i+1] = prefix[i] + D[i]
    
    out = []
    for _ in range(Q):
        L = int(data[idx]); idx += 1
        R = int(data[idx]); idx += 1
        # 1-indexed to 0-indexed: l=L-1, r=R-1
        n = R - L + 1
        S = prefix[R] - prefix[L-1]
        if n <= 1:
            out.append('0')
        else:
            out.append(str(11 * (n - 1) * S))
    
    print('\n'.join(out))

main()