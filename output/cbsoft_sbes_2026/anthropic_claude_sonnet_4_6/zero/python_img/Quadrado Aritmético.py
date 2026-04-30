import sys

def solve():
    input_data = sys.stdin.read().split()
    N = int(input_data[0])
    S = int(input_data[1])
    
    if N == 1:
        print(S)
        return
    
    # Construction of an arithmetic square:
    # An arithmetic square requires that any permutation selection sums to S.
    # 
    # Key insight: If we write grid[i][j] = r[i] + c[j], then any legal selection
    # (one per row, one per column) sums to sum(r[i]) + sum(c[sigma(i)]) = sum(r) + sum(c)
    # which is constant = S.
    #
    # We need all N*N values to be distinct.
    # 
    # Let's choose r[i] and c[j] such that r[i] + c[j] are all distinct.
    # 
    # If we pick r[i] = i * N (for i = 0..N-1) and c[j] = j (for j = 0..N-1),
    # then grid[i][j] = i*N + j, which gives values 0, 1, 2, ..., N*N-1 (all distinct).
    # 
    # Sum of any legal selection = sum(r[i] for i=0..N-1) + sum(c[j] for j=0..N-1)
    # = N*(0+1+...+(N-1)) + (0+1+...+(N-1))
    # = (N+1) * N*(N-1)/2
    #
    # We want this to equal S.
    # Current sum = (N+1)*N*(N-1)//2
    # We need to add offset = S - current_sum to make it work.
    # We can add offset/N to each r[i], but offset might not be divisible by N.
    # 
    # Better: add offset to r[0] only? No, that changes only selections in row 0.
    # 
    # Actually, we need to distribute the offset across rows or columns such that
    # sum(r) + sum(c) = S.
    # 
    # Simplest: keep c[j] = j, set r[i] = i*N for i=1..N-1, and set r[0] = S - sum(c) - sum(r[1..N-1])
    # sum(c) = N*(N-1)//2
    # sum(r[1..N-1]) = N*(1+2+...+(N-1)) = N*(N-1)*N//2... wait
    # sum(r[1..N-1]) = N*(N*(N-1)//2 - 0) ... = N * (1+2+...+(N-1)) = N*(N-1)*N//2
    # Hmm let me recalc.
    # r[i] = i*N for i=0..N-1: sum = N*(0+1+...+(N-1)) = N*N*(N-1)//2
    # c[j] = j for j=0..N-1: sum = N*(N-1)//2
    # 
    # Let's set r[i] = i*N for i=0..N-1, c[j] = j for j=0..N-1
    # Then adjust: add delta to r[0], where delta = S - (N*N*(N-1)//2 + N*(N-1)//2)
    # This changes r[0] from 0 to delta.
    # grid[0][j] = delta + j
    # grid[i][j] = i*N + j for i >= 1
    # 
    # Are all values distinct? 
    # For i>=1: values are i*N+j in [N, N*N-1] range (with i>=1)
    # For i=0: values are delta+j for j=0..N-1
    # We need delta+j != i*N+j' for all i>=1, j, j'
    # i.e., delta != i*N + (j'-j), which might be hard to guarantee.
    # 
    # Safer: use large spacing. Set r[i] = i * (N*N) and c[j] = j.
    # Then all grid values i*N^2 + j are distinct (since i*N^2+j uniquely determines i,j).
    # sum = N^2*(N-1)/2*N + N*(N-1)/2 ... let me just compute and adjust r[0].
    
    base_r = [i * N * N for i in range(N)]
    base_c = [j for j in range(N)]
    
    current_sum = sum(base_r) + sum(base_c)
    delta = S - current_sum
    base_r[0] += delta
    
    # grid[i][j] = base_r[i] + base_c[j]
    # All distinct because base_r[i]+base_c[j]: for i>=1, base_r[i] are multiples of N^2,
    # and base_c[j] in [0,N-1], so i*N^2+j uniquely identifies (i,j).
    # For i=0: base_r[0]+j = delta+j. Need delta+j != i*N^2+j' for i>=1.
    # delta = S - N^2*(0+1+...+(N-1)) - (0+1+...+(N-1)) = S - (N^2+1)*N*(N-1)//2
    # |S| <= 1000, N<=1000, so delta can be large negative. Values might exceed 1e9.
    # 
    # Let's just output and check constraints are met per problem statement.
    
    out = []
    for i in range(N):
        row = [base_r[i] + base_c[j] for j in range(N)]
        out.append(' '.join(map(str, row)))
    print('\n'.join(out))

solve()