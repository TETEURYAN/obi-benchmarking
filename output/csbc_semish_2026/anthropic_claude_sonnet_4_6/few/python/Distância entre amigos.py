import sys

def solve():
    data = sys.stdin.read().split()
    n = int(data[0])
    a = [int(data[i+1]) for i in range(n)]
    
    # Distance between building i and building j (i < j) is:
    # a[i] + (j - i) + a[j]
    # = a[i] - i + a[j] + j
    # So we want to maximize (a[i] - i) + (a[j] + j) for i < j
    # OR equivalently consider all pairs, but since i < j:
    # max over all i < j of (a[i] - i) + (a[j] + j)
    
    # We can also write it as:
    # For each j, we want max(a[i] - i) for i < j, then add a[j] + j
    
    # But wait, we should also consider the symmetric case:
    # a[j] - j + a[i] + i for i < j (if we go from j to i, distance is same)
    # Actually distance is symmetric: a[i] + (j-i) + a[j] = a[j] + (j-i) + a[i]
    # So it's the same formula regardless of direction.
    
    # So maximize: a[i] + a[j] + (j - i) for i < j
    # = (a[j] + j) + (a[i] - i) for i < j
    
    max_ans = 0
    max_left = a[0] - 0  # a[i] - i for i=0
    
    for j in range(1, n):
        val = max_left + a[j] + j
        if val > max_ans:
            max_ans = val
        cur = a[j] - j
        if cur > max_left:
            max_left = cur
    
    print(max_ans)

solve()