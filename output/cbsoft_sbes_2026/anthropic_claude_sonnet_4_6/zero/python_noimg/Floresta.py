import sys

def solve():
    N = int(sys.stdin.readline())
    
    # For a grid of x columns and y rows (x <= y) of oaks:
    # Number of oaks = x * y
    # Number of eucalyptus = (x-1) * (y-1)
    # Total = x*y + (x-1)*(y-1) = x*y + x*y - x - y + 1 = 2*x*y - x - y + 1
    # We need 2*x*y - x - y + 1 = N
    # Also x >= 1, y >= 1, and at least one eucalyptus means (x-1)*(y-1) >= 1, so x >= 2, y >= 2
    
    # 2*x*y - x - y + 1 = N
    # 2*x*y - x - y = N - 1
    # x*(2y - 1) - y = N - 1
    # x*(2y - 1) - y = N - 1
    # Multiply both sides by 2:
    # 2x*(2y-1) - 2y = 2*(N-1)
    # 2x*(2y-1) - (2y-1) - 1 = 2*(N-1)
    # (2x-1)*(2y-1) = 2*(N-1) + 1 = 2N - 1
    
    # So we need (2x-1)*(2y-1) = 2N - 1
    # Let a = 2x-1, b = 2y-1, both odd positive integers, a <= b
    # a*b = 2N - 1
    # x = (a+1)/2, y = (b+1)/2
    # Need x >= 2 => a >= 3
    # Need y >= 2 => b >= 3
    # So both a >= 3 and b >= 3
    
    M = 2 * N - 1
    count = 0
    
    # Find all factor pairs (a, b) with a <= b, a*b = M, both odd, a >= 3, b >= 3
    # Since M = 2N-1 is always odd, all factors of M are odd
    
    i = 1
    while i * i <= M:
        if M % i == 0:
            a = i
            b = M // i
            # both are odd (guaranteed since M is odd)
            if a >= 3 and b >= 3:
                count += 1
        i += 1
    
    print(count)

solve()