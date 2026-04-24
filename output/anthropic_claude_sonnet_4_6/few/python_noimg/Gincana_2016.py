import sys
from math import gcd

def solve():
    data = sys.stdin.read().split()
    N = int(data[0])
    M = int(data[1])
    
    # We need gcd(N, X) = 1, and X <= M, maximize X
    # Find largest X in [1, M] such that gcd(N, X) = 1
    
    # If gcd(N, M) == 1, answer is M
    if gcd(N, M) == 1:
        print(M)
        return
    
    # Otherwise search from M downward
    # But M can be up to 10^18, so we need a smarter approach
    # 
    # Key insight: we need X coprime to N, X <= M
    # The prime factors of N determine which X are invalid
    # We can use inclusion-exclusion over prime factors of N
    # But N can be up to 10^18...
    #
    # Alternative: iterate from M downward, but that could be slow
    # However, the density of numbers coprime to N is phi(N)/N > 0
    # The gap between consecutive numbers coprime to N is at most
    # the product of distinct prime factors of N (primorial)
    # For N up to 10^18, the number of distinct primes is at most ~15
    # (2*3*5*7*11*13*17*19*23*29*31*37*41*43*47 > 10^18)
    # So worst case gap is bounded, but could still be large
    #
    # Better: factorize N, then use inclusion-exclusion to count
    # numbers <= X coprime to N, then binary search for the answer
    
    # Factorize N
    def factorize(n):
        factors = set()
        d = 2
        while d * d <= n:
            if n % d == 0:
                factors.add(d)
                while n % d == 0:
                    n //= d
            d += 1
        if n > 1:
            factors.add(n)
        return list(factors)
    
    primes = factorize(N)
    k = len(primes)
    
    # Count numbers in [1, x] coprime to N using inclusion-exclusion
    def count_coprime(x):
        if x <= 0:
            return 0
        total = 0
        for mask in range(1 << k):
            prod = 1
            bits = 0
            for i in range(k):
                if mask & (1 << i):
                    prod *= primes[i]
                    bits += 1
                    if prod > x:
                        break
            else:
                if bits % 2 == 0:
                    total += x // prod
                else:
                    total -= x // prod
        return total
    
    # Binary search: find largest X <= M with count_coprime(X) >= count_coprime(X-1)+1
    # i.e., X itself is coprime to N
    # We want the largest X <= M that is coprime to N
    # 
    # We know count_coprime(M) >= 1 (since gcd(N,1)=1 always)
    # Binary search for largest X where count_coprime(X) == count_coprime(M)
    # but that's the last coprime number <= M
    
    target = count_coprime(M)
    # Binary search for smallest X such that count_coprime(X) == target
    lo, hi = 1, M
    while lo < hi:
        mid = (lo + hi) // 2
        if count_coprime(mid) >= target:
            hi = mid
        else:
            lo = mid + 1
    
    print(lo)

solve()