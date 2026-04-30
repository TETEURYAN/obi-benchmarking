import sys

def solve():
    N = int(sys.stdin.readline())
    
    # For a grid of x columns and y rows (x <= y):
    # Number of oaks (carvalhos) = x * y
    # Number of eucalyptus = (x-1) * (y-1)
    # Total = x*y + (x-1)*(y-1) = x*y + x*y - x - y + 1 = 2*x*y - x - y + 1
    # We need 2*x*y - x - y + 1 = N
    # Also x >= 2, y >= 2 (at least one eucalyptus needed, so both dimensions >= 2)
    # And x <= y
    
    # 2*x*y - x - y + 1 = N
    # 2*x*y - x - y = N - 1
    # Multiply by 2: 4*x*y - 2*x - 2*y = 2*(N-1)
    # (2x-1)(2y-1) = 2*(N-1) + 1 = 2*N - 1
    
    # So we need (2x-1)(2y-1) = 2*N - 1
    # Let a = 2x-1, b = 2y-1, where a and b are odd, a >= 3, b >= 3, a <= b
    # a * b = 2*N - 1
    
    target = 2 * N - 1
    
    count = 0
    
    # Find all factor pairs (a, b) with a <= b, a*b = target, a >= 3, b >= 3, a odd, b odd
    # Since target = 2*N - 1 is always odd, all factors of target are odd
    
    i = 1
    while i * i <= target:
        if target % i == 0:
            a = i
            b = target // i
            # a <= b automatically since i <= sqrt(target)
            if a >= 3 and b >= 3:
                count += 1
        i += 1
    
    print(count)

solve()