import sys

def solve():
    N = int(sys.stdin.read().strip())
    
    # For a grid of x rows and y columns (x <= y):
    # - oaks (carvalhos) = x * y
    # - eucalyptus = (x-1) * (y-1)
    # - total = x*y + (x-1)*(y-1) = x*y + x*y - x - y + 1 = 2*x*y - x - y + 1
    # So N = 2*x*y - x - y + 1
    # N - 1 = 2*x*y - x - y = x*(2y-1) - y
    # N - 1 = x*(2y-1) - y
    # 2*(N-1) = 2x*(2y-1) - 2y = 2x*(2y-1) - (2y-1) - 1
    # 2*(N-1) + 1 = (2x-1)*(2y-1)
    # 2N - 1 = (2x-1)*(2y-1)
    
    # So we need to find pairs (a, b) where a = 2x-1, b = 2y-1, a*b = 2N-1
    # a and b must be odd positive integers, a <= b
    # x = (a+1)/2 >= 1 => a >= 1 (always true for positive odd)
    # y = (b+1)/2 >= 1 => b >= 1
    # Also x <= y means a <= b
    # Also at least one eucalyptus: (x-1)*(y-1) >= 1 => x >= 2 and y >= 2
    # x >= 2 => a = 2x-1 >= 3
    # y >= 2 => b = 2y-1 >= 3
    
    target = 2 * N - 1
    count = 0
    
    i = 1
    while i * i <= target:
        if target % i == 0:
            a = i
            b = target // i
            # both must be odd - since target = 2N-1 is always odd,
            # if a is odd and a*b=odd, then b is odd too
            # check a >= 3 and b >= 3
            if a >= 3 and b >= 3:
                count += 1
        i += 2  # only odd divisors since target is odd
    
    print(count)

solve()