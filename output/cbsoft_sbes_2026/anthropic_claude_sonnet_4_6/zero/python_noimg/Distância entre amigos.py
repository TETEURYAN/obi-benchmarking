import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    
    # Distance between apartment at floor a[i] in building i and floor a[j] in building j
    # = a[i] + |i - j| + a[j]
    # We want to maximize a[i] + a[j] + |i - j|
    # 
    # Case 1: i < j => maximize a[i] - i + a[j] + j
    # Case 2: i > j => maximize a[i] + i + a[j] - j
    # Both cases are symmetric, so we just need case 1:
    # maximize (a[j] + j) + (a[i] - i) for i < j
    
    # For case 1: max over all pairs i < j of (a[i] - i) + (a[j] + j)
    # We can scan left to right, keeping track of max(a[i] - i) seen so far
    
    max_dist = 0
    
    # Case 1: j > i, distance = a[i] + (j - i) + a[j] = (a[i] - i) + (a[j] + j)
    max_ai_minus_i = a[0] - 0
    for j in range(1, n):
        val = max_ai_minus_i + a[j] + j
        if val > max_dist:
            max_dist = val
        if a[j] - j > max_ai_minus_i:
            max_ai_minus_i = a[j] - j
    
    # Case 2: i > j, distance = a[j] + (i - j) + a[i] = (a[j] - j) + (a[i] + i)
    # This is symmetric to case 1, same result
    # But let's verify by also computing it
    max_aj_minus_j = a[0] - 0
    for i in range(1, n):
        val = max_aj_minus_j + a[i] + i
        if val > max_dist:
            max_dist = val
        if a[i] - i > max_aj_minus_j:
            max_aj_minus_j = a[i] - i
    
    print(max_dist)

solve()