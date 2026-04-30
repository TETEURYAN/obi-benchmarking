import sys
from bisect import bisect_left

def solve():
    input_data = sys.stdin.read().split()
    n = int(input_data[0])
    a = list(map(int, input_data[1:n+1]))
    
    a.sort()
    
    count = 0
    
    # For each pair (i, j) with i < j, count k > j such that a[i] + a[j] > a[k]
    # Since array is sorted, a[k] < a[i] + a[j]
    # We need a[k] < a[i] + a[j], and k > j
    # The valid k's are from j+1 to some index
    
    for i in range(n):
        k = i + 2
        for j in range(i + 1, n):
            # Find largest k such that a[k] < a[i] + a[j]
            # k must be > j
            # Since array is sorted, as j increases, a[i]+a[j] increases
            # so k can only move right
            while k < n and a[k] < a[i] + a[j]:
                k += 1
            # valid k's are from j+1 to k-1
            count += max(0, k - 1 - j)
    
    print(count)

solve()