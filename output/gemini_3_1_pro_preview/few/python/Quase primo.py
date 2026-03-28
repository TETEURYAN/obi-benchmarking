import sys
import bisect

sys.setrecursionlimit(200000)

input_data = sys.stdin.read().split()
if not input_data:
    exit()

N = int(input_data[0])
K = int(input_data[1])
primes = [int(x) for x in input_data[2:K+2]]
primes.sort()

memo = {}

def solve(n, k):
    if n == 0:
        return 0
    if k == 0:
        return n
    
    if primes[k-1] > n:
        k = bisect.bisect_right(primes, n, 0, k)
        if k == 0:
            return n
            
    state = n * 50 + k
    if state in memo:
        return memo[state]
    
    res = solve(n, k - 1) - solve(n // primes[k - 1], k - 1)
    memo[state] = res
    return res

print(solve(N, K))