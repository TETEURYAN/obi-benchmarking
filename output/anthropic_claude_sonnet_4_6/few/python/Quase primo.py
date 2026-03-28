import sys

def solve():
    data = sys.stdin.read().split()
    N = int(data[0])
    K = int(data[1])
    primes = [int(data[2 + i]) for i in range(K)]
    
    # Inclusion-exclusion principle
    # Count numbers in [1, N] not divisible by any prime in the list
    
    total = 0
    # Iterate over all subsets of primes
    for mask in range(1 << K):
        bits = bin(mask).count('1')
        product = 1
        overflow = False
        for i in range(K):
            if mask & (1 << i):
                product *= primes[i]
                if product > N:
                    overflow = True
                    break
        
        if overflow:
            count = 0
        else:
            count = N // product
        
        if bits % 2 == 0:
            total += count
        else:
            total -= count
    
    print(total)

solve()