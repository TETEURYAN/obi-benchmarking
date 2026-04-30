import sys
from bisect import bisect_left

def solve():
    input_data = sys.stdin.read().split()
    n = int(input_data[0])
    a = list(map(int, input_data[1:n+1]))
    
    a.sort()
    
    count = 0
    
    # For each pair (i, j) with i < j, count k > j such that a[i] + a[j] > a[k]
    # Since array is sorted, a[i] <= a[j] <= a[k]
    # The only condition that can fail is a[i] + a[j] <= a[k]
    # So we need a[k] < a[i] + a[j]
    # Using binary search: find the largest index where a[k] < a[i] + a[j]
    
    for i in range(n):
        for j in range(i+1, n):
            # Find number of k in (j, n-1] such that a[k] < a[i] + a[j]
            target = a[i] + a[j]
            # bisect_left finds first index >= target
            pos = bisect_left(a, target, j+1, n)
            count += pos - (j+1)
    
    print(count)

solve()