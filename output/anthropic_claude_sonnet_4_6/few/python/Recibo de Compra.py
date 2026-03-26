import sys

def solve():
    data = sys.stdin.read().split()
    R = int(data[0])
    K = int(data[1])
    
    # Count partitions of R into exactly K distinct positive integers
    # dp[k][s] = number of ways to choose k distinct positive integers summing to s
    # We use dp with items chosen in increasing order to avoid duplicates
    
    # dp[k][s] = number of combinations of k distinct positive integers (all >= 1) summing to s
    # We can think of it as: choose k distinct positive integers
    # To enumerate without repetition, we pick them in strictly increasing order
    
    # Let's use recursion with memoization
    # count(k, s, min_val) = number of ways to pick k distinct integers all >= min_val summing to s
    
    from functools import lru_cache
    
    @lru_cache(maxsize=None)
    def count(k, s, min_val):
        if k == 0:
            return 1 if s == 0 else 0
        if s <= 0:
            return 0
        # minimum sum with k elements starting from min_val: min_val + (min_val+1) + ... + (min_val+k-1)
        min_sum = k * min_val + k * (k - 1) // 2
        if s < min_sum:
            return 0
        total = 0
        # first element ranges from min_val to s - (sum of remaining k-1 elements minimum)
        # remaining k-1 elements start from first+1, minimum sum = (first+1) + ... + (first+k-1)
        # = (k-1)*first + (k-1)*k//2... wait let me just iterate
        for v in range(min_val, s + 1):
            # remaining k-1 elements must sum to s-v, all > v
            remaining = s - v
            if remaining <= 0 and k > 1:
                break
            total += count(k - 1, remaining, v + 1)
        return total
    
    print(count(K, R, 1))

solve()