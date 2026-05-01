import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    
    # Distance between apartment in building i (floor ai) and building j (floor aj)
    # is a[i] + |i - j| + a[j]
    # We want to maximize a[i] + a[j] + |i - j|
    # 
    # Case 1: i < j => maximize (a[i] - i) + (a[j] + j)
    # Case 2: i > j => maximize (a[i] + i) + (a[j] - j)
    # Both cases are symmetric, so we just need:
    # max over i < j of (a[i] - i) + (a[j] + j)
    
    # For case i < j:
    # max of (a[j] + j) + max of (a[i] - i) for i < j
    
    max_dist = 0
    
    # Sweep left to right, track max of (a[i] - i)
    max_ai_minus_i = a[0] - 0
    for j in range(1, n):
        val = max_ai_minus_i + a[j] + j
        if val > max_dist:
            max_dist = val
        cur = a[j] - j
        if cur > max_ai_minus_i:
            max_ai_minus_i = cur
    
    # Sweep right to left, track max of (a[i] + i)
    max_ai_plus_i = a[n-1] + (n-1)
    for j in range(n-2, -1, -1):
        val = max_ai_plus_i + a[j] - j
        if val > max_dist:
            max_dist = val
        cur = a[j] + j
        if cur > max_ai_plus_i:
            max_ai_plus_i = cur
    
    print(max_dist)

solve()