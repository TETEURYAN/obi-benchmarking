import sys

def solve():
    data = sys.stdin.read().split()
    n = int(data[0])
    a = list(map(int, data[1:n+1]))
    
    target = max(a)
    
    # We need to find minimum number of phases to make all buildings equal to target
    # Each phase: pick L,R where all buildings in [L,R] have same height a, then increment all by 1
    # This is equivalent to: we need to raise each building from a[i] to target
    # The number of phases needed is computed by thinking of it as:
    # We process level by level. At each level, we look at which buildings need to be raised.
    # The minimum number of operations is similar to the "minimum number of increments" problem.
    
    # Think of it this way: the difference array d[i] = target - a[i] >= 0
    # We need to cover these differences using intervals where all elements in the interval
    # have the same current height (which changes as we apply operations).
    
    # Actually, this problem is equivalent to:
    # Given array of heights, find minimum operations where each operation increments
    # a contiguous subarray that is currently uniform (all same value).
    
    # Key insight: Think of the "work" needed at each position as (target - a[i]).
    # The minimum number of phases equals the sum of positive differences when we look at
    # consecutive elements in the difference array.
    
    # Let d[i] = target - a[i]. We need to perform operations to reduce all d[i] to 0.
    # Each operation selects a contiguous range where all d[i] are equal (same remaining work)
    # and decrements them by 1... wait, let me think differently.
    
    # Actually the answer is: consider the array of differences d[i] = target - a[i].
    # The minimum number of operations to "paint" these differences using horizontal strokes
    # on a histogram is: d[0] + sum(max(0, d[i] - d[i-1]) for i in 1..n-1)
    # But we also need the constraint that operations must be on uniform-height buildings.
    
    # Let me reconsider. The problem is equivalent to painting a histogram with minimum
    # horizontal brush strokes, where each stroke must be at the same level and contiguous.
    # This is the classic "minimum number of horizontal lines to paint histogram" problem.
    
    # The answer for that is: sum of max(0, d[i] - d[i-1]) for i from 0 to n-1
    # where d[-1] = 0 (boundary).
    
    # For test 1: a = [3,1,1,2], target=3, d=[0,2,2,1]
    # answer = max(0,0) + max(0,2-0) + max(0,2-2) + max(0,1-2) = 0+2+0+0 = 2 ✓
    
    # For test 2: a=[5,4,4,4,5,4,4,7], target=7, d=[2,3,3,3,2,3,3,0]
    # answer = 2 + max(0,3-2) + 0 + 0 + max(0,2-3)=0 + max(0,3-2)=1 + 0 + max(0,0-3)=0
    # = 2+1+0+0+0+1+0+0 = 4 ✓
    
    # For test 3: a=[100,100,100], target=100, d=[0,0,0]
    # answer = 0 ✓
    
    d = [target - x for x in a]
    
    ans = d[0]
    for i in range(1, n):
        if d[i] > d[i-1]:
            ans += d[i] - d[i-1]
    
    print(ans)

solve()