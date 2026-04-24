import sys

def solve():
    data = sys.stdin.read().split()
    n = int(data[0])
    digits = list(map(int, data[1:n+1]))
    
    # We need last digit to be 0 or 5 after swap
    # Try all possible swaps and find the maximum valid result
    
    best = None
    
    for i in range(n):
        for j in range(i+1, n):
            # swap i and j
            digits[i], digits[j] = digits[j], digits[i]
            
            # check divisible by 5 (last digit is 0 or 5)
            # also check no leading zero
            if digits[n-1] in (0, 5) and digits[0] != 0:
                if best is None or digits > best:
                    best = digits[:]
            
            # swap back
            digits[i], digits[j] = digits[j], digits[i]
    
    if best is None:
        print(-1)
    else:
        print(*best)

solve()