import sys
import bisect

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    iterator = iter(input_data)
    
    try:
        N = int(next(iterator))
        L = int(next(iterator))
        R = int(next(iterator))
    except StopIteration:
        return

    A = []
    for _ in range(N):
        try:
            A.append(int(next(iterator)))
        except StopIteration:
            break
            
    A.sort()
    
    # Function to calculate the minimum distance from x to any point in A
    def get_min_dist(x):
        # Find the insertion point for x in A
        idx = bisect.bisect_left(A, x)
        
        min_dist = float('inf')
        
        # Check the element at the insertion point (if it exists)
        if idx < N:
            min_dist = min(min_dist, A[idx] - x)
            
        # Check the element just before the insertion point (if it exists)
        if idx > 0:
            min_dist = min(min_dist, x - A[idx-1])
            
        return min_dist

    # Maximin wants to maximize the minimum distance.
    # The optimal x is either at the boundaries L, R, or at the midpoints between consecutive numbers in A.
    
    ans = 0
    
    # Check boundaries
    ans = max(ans, get_min_dist(L))
    ans = max(ans, get_min_dist(R))
    
    # Check midpoints of gaps
    for i in range(N - 1):
        u = A[i]
        v = A[i+1]
        
        # If u == v, the gap is 0, so distance is 0. 
        # Since we want to maximize distance, we can skip.
        if u == v:
            continue
            
        # The optimal integer points in the gap [u, v] are around the midpoint.
        m1 = (u + v) // 2
        m2 = m1 + 1
        
        # Check m1
        if L <= m1 <= R:
            # Since m1 is between u and v, the closest points are u and v.
            # We don't need a binary search here.
            dist = min(m1 - u, v - m1)
            if dist > ans:
                ans = dist
                
        # Check m2
        if L <= m2 <= R:
            dist = min(m2 - u, v - m2)
            if dist > ans:
                ans = dist
                
    print(ans)

if __name__ == '__main__':
    solve()