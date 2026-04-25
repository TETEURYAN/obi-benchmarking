Looking at this problem, I need to count pairs (A, B) where the slope (Ya - Yb) / (Xa - Xb) >= P/Q.

Key insight: The condition (Ya - Yb) / (Xa - Xb) >= P/Q can be rewritten. If I sort points by X, then for points i < j (Xi < Xj), the slope is (Yj - Yi) / (Xj - Xi) >= P/Q.

This means: Q*(Yj - Yi) >= P*(Xj - Xi) (careful with sign of Q).

Let me think of a transformation. If I define for each point a value: consider the line y = (P/Q)*x. The slope condition (Yb - Ya)/(Xb - Xa) >= P/Q means the point B is "above" the line through A with slope P/Q.

Transform: Let's define for each point a new coordinate. If we subtract the line y = (P/Q)*x, define Yi' = Yi - (P/Q)*Xi = (Q*Yi - P*Xi)/Q.

After sorting by X, for i < j: slope >= P/Q iff (Yj - Yi)/(Xj - Xi) >= P/Q iff Q*(Yj-Yi) >= P*(Xj-Xi) (if Q>0) or Q*(Yj-Yi) <= P*(Xj-Xi) (if Q<0).

This simplifies to: Q*Yj - P*Xj >= Q*Yi - P*Xi (if Q>0), i.e., Vj >= Vi where V = Q*Y - P*X.

So define V_i = Q*Yi - P*Xi. Sort by X. For Q > 0: count pairs (i,j) with i<j (in X order) where Vj >= Vi. For Q < 0: count pairs where Vj <= Vi.

Wait, but the pair (A,B) is unordered. The slope between A and B is the same regardless of direction. So I just need to count unordered pairs where the slope >= P/Q.

After sorting by X (all X distinct), for pair (i,j) with Xi < Xj:
- slope = (Yj - Yi)/(Xj - Xi) >= P/Q
- If Q > 0: Q*(Yj-Yi) >= P*(Xj-Xi) → Q*Yj - P*Xj >= Q*Yi - P*Xi → Vj >= Vi
- If Q < 0: Q*(Yj-Yi) <= P*(Xj-Xi) → Vj <= Vi (inequality flips)

So for Q > 0: count pairs (i < j in X-sorted order) where V[j] >= V[i] → count non-inversions (pairs where V is non-decreasing).
For Q < 0: count pairs where V[j] <= V[i] → count non-inversions in the reversed sense (pairs where V is non-increasing).

Total pairs = N*(N-1)/2. 
- For Q > 0: answer = total - (number of pairs where V[j] < V[i]) = total - inversions_strict
- For Q < 0: answer = total - (number of pairs where V[j] > V[i]) = total - strict_inversions_in_other_direction

Actually: for Q > 0, count pairs i<j where V[j] >= V[i] = total - count(V[j] < V[i]).
For Q < 0, count pairs i<j where V[j] <= V[i] = total - count(V[j] > V[i]).

I'll use a merge sort / BIT (Fenwick tree) to count inversions.

```python
import sys
from sortedcontainers import SortedList

def solve():
    data = sys.stdin.buffer.read().split()
    idx = 0
    N = int(data[idx]); idx+=1
    P = int(data[idx]); idx+=1
    Q = int(data[idx]); idx+=1
    
    points = []
    for _ in range(N):
        x = int(data[idx]); idx+=1
        y = int(data[idx]); idx+=1
        points.append((x, y))
    
    points.sort(key=lambda p: p[0])
    
    V = [Q * y - P * x for x, y in points]
    
    total = N * (N - 1) // 2
    
    # Count pairs i < j where V[j] < V[i] (strict inversions) for Q > 0
    # Count pairs i < j where V[j] > V[i] for Q < 0
    
    sl = SortedList()
    count_bad = 0
    
    if Q > 0:
        for v in V:
            # count elements in sl that are > v
            count_bad += len(sl) - sl.bisect_right(v)
            sl.add(v)
    else:
        for v in V:
            # count elements in sl that are < v
            count_bad += sl.bisect_left(v)
            sl.add(v)
    
    print(total - count_bad)

solve()
```