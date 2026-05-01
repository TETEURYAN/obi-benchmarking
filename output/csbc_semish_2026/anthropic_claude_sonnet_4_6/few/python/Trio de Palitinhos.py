import sys
from bisect import bisect_left

def solve():
    data = sys.stdin.read().split()
    n = int(data[0])
    a = sorted(int(data[i+1]) for i in range(n))
    
    count = 0
    for i in range(n):
        for j in range(i+1, n):
            # a[i] <= a[j], need a[k] < a[i] + a[j], and k > j
            # since sorted, a[k] >= a[j] >= a[i]
            # only need to check a[i] + a[j] > a[k]
            # find number of k in (j, n) where a[k] < a[i] + a[j]
            limit = a[i] + a[j]
            # bisect_left finds first index where a[k] >= limit
            pos = bisect_left(a, limit, j+1, n)
            count += pos - (j+1)
    
    print(count)

solve()