import sys

def solve():
    N, M = map(int, input().split())
    
    # We need to count the number of ways to write N = a + b + c
    # where 1 <= a, b, c <= M
    # Substitute a' = a-1, b' = b-1, c' = c-1
    # Then a' + b' + c' = N - 3, where 0 <= a', b', c' <= M-1
    
    # Using inclusion-exclusion:
    # Total without upper bound: C(N-3+2, 2) = C(N-1, 2)
    # Subtract cases where at least one variable >= M (i.e., >= M, so a' >= M means a >= M+1)
    # If a' >= M, let a'' = a' - M, then a'' + b' + c' = N - 3 - M
    # Number of solutions: C(N-3-M+2, 2) = C(N-M-1, 2) if N-3-M >= 0
    # There are 3 such cases (for each variable)
    # Add back cases where two variables >= M:
    # a'' + b'' + c' = N - 3 - 2M, solutions: C(N-3-2M+2, 2) = C(N-2M-1, 2) if N-3-2M >= 0
    # There are 3 such cases
    # Subtract cases where all three >= M:
    # N - 3 - 3M >= 0 needed
    
    def C2(n):
        # C(n, 2) = n*(n-1)//2 for n >= 2, else 0
        if n < 2:
            return 0
        return n * (n - 1) // 2
    
    n3 = N - 3  # a' + b' + c' = n3, 0 <= each <= M-1
    
    # Stars and bars without upper bound: C(n3 + 2, 2)
    total = C2(n3 + 2)
    
    # Subtract: at least one >= M
    # a' >= M: a'' + b' + c' = n3 - M
    r1 = n3 - M
    if r1 >= 0:
        total -= 3 * C2(r1 + 2)
    
    # Add back: at least two >= M
    r2 = n3 - 2 * M
    if r2 >= 0:
        total += 3 * C2(r2 + 2)
    
    # Subtract: all three >= M
    r3 = n3 - 3 * M
    if r3 >= 0:
        total -= C2(r3 + 2)
    
    print(total)

solve()