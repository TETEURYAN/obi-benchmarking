Looking at this problem, I need to split N buildings into two groups to minimize the maximum Manhattan distance between any two buildings in the same group.

Key insight: The Manhattan distance |Xi-Xj| + |Yi-Yj| can be transformed. Using the rotation trick: let u = x+y, v = x-y. Then Manhattan distance = max(|ui-uj|, |vi-vj|) ... wait, that's Chebyshev. Actually |xi-xj|+|yi-yj| = max(|(ui-uj)|, |(vi-vj)|) in Chebyshev after rotation... Let me reconsider.

Actually, the Manhattan distance between two points equals the Chebyshev distance after the 45-degree rotation: if we set u=x+y, v=x-y, then Chebyshev distance max(|u1-u2|, |v1-v2|) = Manhattan distance.

So the maximum Manhattan distance in a set = max over all pairs of max(|ui-uj|, |vi-vj|) = max(range of u, range of v) where range = max - min.

So for a group, the maximum pairwise Manhattan distance = max(u_max - u_min, v_max - v_min).

We want to split points into two groups A and B to minimize max(diameter(A), diameter(B)) where diameter is measured as max(range_u, range_v).

Binary search on the answer D. For a given D, can we split points into two groups each with diameter ≤ D?

For a group to have diameter ≤ D: range_u ≤ D AND range_v ≤ D.

So each group must fit in a "box" of size D×D in (u,v) space.

This is a 2-coloring problem: can we partition points into two axis-aligned squares of side D in (u,v) space?

For binary search on D: sort points by u. The first group's u-range must be ≤ D. 

Key observation: In an optimal split, one group contains the point with minimum u. That point's group has u in [u_min, u_min+D]. Points outside this u-range must go to the other group. Points inside can go to either.

So: points with u > u_min+D must all be in group B. Group B must have u-range ≤ D and v-range ≤ D.

For the remaining points (u ≤ u_min+D), we need to assign them such that group A (containing u_min point) has v-range ≤ D, and group B constraints are maintained.

Let me think of a cleaner approach: sort by u. The point with smallest u goes to group A. Group A's u spans [u_min, u_min+D]. Points with u > u_min+D go to group B. 

For group B to be valid: u_range of B ≤ D (automatically if we also consider the point with max u), and v_range ≤ D.

For the "middle" points (u in [u_min, u_min+D]), we can assign to A or B. We want to minimize v-ranges.

This suggests: binary search on D, then check feasibility. The check: sort by u. Points with u outside [u_min, u_min+D] go to B. For remaining, greedily assign to A if possible (v fits), else to B.

But this is complex. Let me implement binary search + feasibility check based on the observation that optimal groups are intervals in u after sorting, or we split by some u threshold.

After research, the key insight: sort by u+v. The optimal split is a contiguous partition in some sorted order. We can try all O(N) splits by u-coordinate and v-coordinate boundaries.

Given complexity constraints, I'll binary search on D and for each D, check if we can cover all points with two rectangles of side D in (u,v) space.

```python
import sys
input = sys.stdin.readline

def solve():
    N = int(input())
    X = list(map(int, input().split()))
    Y = list(map(int, input().split()))
    
    u = [X[i]+Y[i] for i in range(N)]
    v = [X[i]-Y[i] for i in range(N)]
    
    points = sorted(zip(u, v))
    us = [p[0] for p in points]
    vs = [p[1] for p in points]
    
    def check(D):
        # Try all ways to split: group A has u in [us[0], us[0]+D]
        # points beyond go to B
        # Also try group B has the min-u point... symmetric
        # Actually try: for each prefix/suffix split in u
        n = len(points)
        # suffix min/max v
        suf_minv = [0]*n; suf_maxv = [0]*n
        suf_minv[n-1]=vs[n-1]; suf_maxv[n-1]=vs[n-1]
        for i in range(n-2,-1,-1):
            suf_minv[i]=min(suf_minv[i+1],vs[i])
            suf_maxv[i]=max(suf_maxv[i+1],vs[i])
        pre_minv=[0]*n; pre_maxv=[0]*n
        pre_minv[0]=vs[0]; pre_maxv[0]=vs[0]
        for i in range(1,n):
            pre_minv[i]=min(pre_minv[i-1],vs[i])
            pre_maxv[i]=max(pre_maxv[i-1],vs[i])
        # Split: A=points[0..i], B=points[i+1..n-1]
        # Check A: us[i]-us[0]<=D and pre_maxv[i]-pre_minv[i]<=D
        # Check B: us[n-1]-us[i+1]<=D and suf_maxv[i+1]-suf_minv[i+1]<=D
        for i in range(n-1):
            if us[i]-us[0]>D: break
            if pre_maxv[i]-pre_minv[i]>D: continue
            if us[n-1]-us[i+1]<=D and suf_maxv[i+1]-suf_minv[i+1]<=D:
                return True
        # Also check all in one group (if N points fit in D)
        if us[n-1]-us[0]<=D and (pre_maxv[n-1]-pre_minv[n-1])<=D:
            return True
        # Also need to handle: A gets suffix, B gets prefix
        # (already covered by symmetry if we also try reversed)
        return False
    
    # But this misses cases where split isn't a u-prefix/suffix
    # Need more cases: split by v as well
    # Actually the optimal split must be: one group is a "rectangle" in u,v space
    # Let me also try sorting by v
    
    def check2(D):
        n = len(points)
        pv = sorted(zip(v,u))
        vs2=[p[0] for p in pv]; us2=[p[1] for p in pv]
        suf_minu=[0]*n; suf_maxu=[0]*n
        suf_minu[n-1]=us2[n-1]; suf_maxu[n-1]=us2[n-1]
        for i in range(n-2,-1,-1):
            suf_minu[i]=min(suf_minu[i+1],us2[i])
            suf_maxu[i]=max(suf_maxu[i+1],us2[i])
        pre_minu=[0]*n; pre_maxu=[0]*n
        pre_minu[0]=us2[0]; pre_maxu[0]=us2[0]
        for i in range(1,n):
            pre_minu[i]=min(pre_minu[i-1],us2[i])
            pre_maxu[i]=max(pre_maxu[i-1],us2[i])
        for i in range(n-1):
            if vs2[i]-vs2[0]>D: break
            if pre_maxu[i]-pre_minu[i]>D: continue
            if vs2[n-1]-vs2[i+1]<=D and suf_maxu[i+1]-suf_minu[i+1]<=D:
                return True
        if vs2[n-1]-vs2[0]<=D and pre_maxu[n-1]-pre_minu[n-1]<=D:
            return True
        return False
    
    lo, hi = 0, 2*10**9
    while lo < hi:
        mid = (lo+hi)//2
        if check(mid) or check2(mid):
            hi = mid
        else:
            lo = mid+1
    print(lo)

solve()
```

Wait, I'm not sure this covers all cases. The split might not be a simple prefix in u or v. Let me think more carefully.

The two groups each need to fit in a D×D box in (u,v) space. The 4 extreme points (min_u, max_u, min_v, max_v) must each be in one of the two boxes. There are limited cases based on which box each extreme point goes to.

The point with min_u must be in some box. That box covers u in [min_u, min_u+D]. All points with u > min_u+D go to the other box. This is the prefix split by u. Similarly for max_u, min_v, max_v. So checking prefix splits in both u and v should cover all cases.

Let me finalize:

```python
import sys

def solve():
    data = sys.stdin.buffer.read().split()
    idx = 0
    N = int(data[idx]); idx+=1
    X = [int(data[idx+i]) for i in range(N)]; idx+=N
    Y = [int(data[idx+i]) for i in range(N)]; idx+=N
    
    u = [X[i]+Y[i] for i in range(N)]
    v = [X[i]-Y[i] for i in range(N)]
    
    # Sort by u
    pts_u = sorted(zip(u,v))
    us = [p[0] for p in pts_u]
    vs_u = [p[1] for p in pts_u]
    
    # Sort by v
    pts_v = sorted(zip(v,u))
    vs = [p[0] for p in pts_v]
    us_v = [p[1] for p in pts_v]
    
    n = N
    
    # Precompute prefix/suffix min/max for vs_u
    pre_minv = [0]*n; pre_maxv = [0]*n
    pre_minv[0]=vs_u[0]; pre_maxv[0]=vs_u[0]
    for i in range(1,n):
        pre_minv[i]=min(pre_minv[i-1],vs_u[i])
        pre_maxv[i]=max(pre_maxv[i-1],vs_u[i])
    suf_minv = [0]*n; suf_maxv = [0]*n
    suf_minv[n-1]=vs_u[n-1]; suf_maxv[n-1]=vs_u[n-1]
    for i in range(n-2,-1,-1):
        suf_minv[i]=min(suf_minv[i+1],vs_u[i])
        suf_maxv[i]=max(suf_maxv[i+1],vs_u[i])
    
    # Precompute prefix/suffix min/max for us_v
    pre_minu = [0]*n; pre_maxu = [0]*n
    pre_minu[0]=us_v[0]; pre_maxu[0]=us_v[0]
    for i in range(1,n):
        pre_minu[i]=min(pre_minu[i-1],us_v[i])
        pre_maxu[i]=max(pre_maxu[i-1],us_v[i])
    suf_minu = [0]*n; suf_maxu = [0]*n
    suf_minu[n-1]=us_v[n-1]; suf_maxu[n-1]=us_v[n-1]
    for i in range(n-2,-1,-1):
        suf_minu[i]=min(suf_minu[i+1],us_v[i])
        suf_maxu[i]=max(suf_maxu[i+1],us_v[i])
    
    def check(D):
        # Split by u: prefix [0..i] and suffix [i+1..n-1]
        for i in range(n-1):
            if us[i]-us[0]>D: break
            if pre_maxv[i]-pre_minv[i]<=D:
                if us[n-1]-us[i+1]<=D and suf_maxv[i+1]-suf_minv[i+1]<=D:
                    return True
        # All in one group (u-sorted)
        if us[n-1]-us[0]<=D and pre_maxv[n-1]-pre_minv[n-1]<=D:
            return True
        # Split by v: prefix [0..i] and suffix [i+1..n-1]
        for i in range(n-1):
            if vs[i]-vs[0]>D: break
            if pre_maxu[i]-pre_minu[i]<=D:
                if vs[n-1]-vs[i+1]<=D and suf_maxu[i+1]-suf_minu[i+1]<=D:
                    return True
        # All in one group (v-sorted)
        if vs[n-1]-vs[0]<=D and pre_maxu[n-1]-pre_minu[n-1]<=D:
            return True
        return False
    
    lo, hi = 0, 2*10**9
    while lo < hi:
        mid = (lo+hi)//2
        if check(mid):
            hi = mid
        else:
            lo = mid+1
    print(lo)

solve()
```

Let me verify with the example:
- N=7, points: (2,4),(10,6),(7,1),(13,5),(5,7),(13,3),(15,5)
- u = x+y: 6,16,8,18,12,16,20
- v = x-y: -2,4,6,8,-2,10,10

Sorted by u: (6,-2),(8,6),(12,-2),(16,16),(16,4),(18,8),(20,10)
us=[6,8,12,16,16,18,20], vs_u=[-2,6,-2,16,4,8,10]

For D=8:
- i=0: us[0]-us[0]=0≤8, pre_maxv[0]-pre_minv[0]=0≤8. Check suffix [1..6]: us[6]-us[1]=12>8. No.
- i=1: us[1]-us[0]=2≤8, pre_maxv[1]-pre_minv[1]=6-(-2)=8≤8. Check suffix [2..6]: us[6]-us[2]=12>8. No.
- i=2: us[2]-us[0]=6≤8, pre_maxv[2]-pre_minv[2]=6-(-2)=8≤8. Check suffix [3..6]: us[6]-us[3]=4≤8, suf_maxv[3]-suf_minv[3]=max(16,4,8,10)-min(16,4,8,10)=16-4=12>8. No.
- i=3: us[3]-us[0]=10>8. Break.

Try v-sorted: vs=[-2,-2,4,6,8,10,10], us_v=[6,12,16,8,18,16,20]
- i=0: vs[0]-vs[0]=0≤8, pre_maxu[0]-pre_minu[0]=0≤8. Suffix [1..6]: vs[6]-vs[1]=12>8. No.
- i=1: vs[1]-vs[0]=0≤8, pre_maxu[1]-pre_minu[1]=12-6=6≤8. Suffix [2..6]: vs[6]-vs[2]=6≤8, suf_maxu[2]-suf_minu[2]=max(16,8,18,16,20)-min(...)=20-8=12>8. No.
- i=2: vs[2]-vs[0]=6≤8, pre_maxu[2]-pre_minu[2]=16-6=10>8. Skip.
- i=3: vs[3]-vs[0]=8≤8, pre_maxu[3]-pre_minu[3]=16-6=10>8. Skip.
- i=4: vs[4]-vs[0]=10>8. Break.

Hmm, not finding D=8. Let me recheck.

The optimal split is (1,3,5) and (2,4,6,8) - but there are only 7 buildings indexed 1-7 in the problem. Let me re-read.

Buildings: (2,4),(10,6),(7,1),(13,5),(5,7),(13,3),(15,5) - indices 1-7.
Group A: buildings 1,3,5 = (2,4),(7,1),(5,7)
Group B: buildings 2,4,6,7 = (10,6),(13,5),(13,3),(15,5)

For group A: u values = 6,8,12; v values = -2,6,-2
Max Manhattan = max(12-6, 6-(-2)) = max(6,8) = 8 ✓

For group B: u values = 16,18,16,20; v values = 4,8,10,10
Max Manhattan = max(20-16, 10-4) = max(4,6) = 6 ✓

So D=8 works. In u-sorted order: (6,-2),(8,6),(12,-2),(16,16),(16,4),(18,8),(20,10)

Group A = {(6,-2),(8,6),(12,-2)} = prefix of 3 in u-sorted.
Group B = {(16,16),(16,4),(18,8),(20,10)} = suffix.

For i=2 (prefix [0..2]): us[2]-us[0]=6≤8, pre_maxv[2]-pre_minv[2]=6-(-2)=8≤8. ✓
Suffix [3..6]: us[6]-us[3]=4≤8, suf_maxv[3]-suf_minv[3]=max(16,4,8,10)-min(16,4,8,10)=16-4=12>8. ✗

But wait, (16,16) corresponds to which building? u=16,v=16 means x+y=16, x-y=16, so x=16, y=0. But no building has those coords!

Let me recompute: building 4 is (13,5): u=18, v=8. Building 2 is (10,6): u=16, v=4. Building 6 is (13,3): u=16, v=10. Building 7 is (15,5): u=20, v=10.

So u values: 
1:(2,4)->u=6,v=-2
2:(10,6)->u=16,v=4
3:(7,1)->u=8,v=6
4:(13,5)->u=18,v=8
5:(5,7)->u=12,v=-2
6:(13,3)->u=16,v=10
7:(15,5)->u=20,v=10

Sorted by u: (6,-2),(8,6),(12,-2),(16,4),(16,10),(18,8),(20,10)
us=[6,8,12,16,16,18,20], vs_u=[-2,6,-2,4,10,8,10]

pre_minv: -2,-2,-2,-2,-2,-2,-2
pre_maxv: -2,6,6,6,10,10,10

suf_minv: -2,-2,-2,4,8,8,10... wait let me redo:
suf_minv[6]=-2... no vs_u[6]=10
suf_minv[6]=10, suf_maxv[6]=10
suf_minv[5]=min(8,10)=8, suf_maxv[5]=max(8,10)=10
suf_minv[4]=min(10,8)=8, suf_maxv[4]=max(10,10)=10
suf_minv[3]=min(4,8)=4, suf_maxv[3]=max(4,10)=10
suf_minv[2]=min(-2,4)=-2, suf_maxv[2]=max(-2,10)=10
...

For i=2 (prefix [0..2]): us[2]-us[0]=6≤8, pre_maxv[2]-pre_minv[2]=6-(-2)=8≤8. ✓
Suffix [3..6]: us[6]-us[3]=4≤8, suf_maxv[3]-suf_minv[3]=10-4=6≤8. ✓ 

So it works. I made an arithmetic error earlier. The code should be correct.

```python
import sys

def solve():
    data = sys.stdin.buffer.read().split()
    idx = 0
    N = int(data[idx]); idx+=1
    X = [int(data[idx+i]) for i in range(N)]; idx+=N
    Y = [int(data[idx+i]) for i in range(N)]; idx+=N
    
    u = [X[i]+Y[i] for i in range(N)]
    v = [X[i]-Y[i] for i in range(N)]
    
    pts_u = sorted(zip(u,v))
    us = [p[0] for p in pts_u]
    vs_u = [p[1] for p in pts_u]
    
    pts_v = sorted(zip(v,u))
    vs = [p[0] for p in pts_v]
    us_v = [p[1] for p in pts_v]
    
    n = N
    
    pre_minv = [0]*n; pre_maxv = [0]*n
    pre_minv[0]=vs_u[0]; pre_maxv[0]=vs_u[0]
    for i in range(1,n):
        pre_minv[i]=min(pre_minv[i-1],vs_u[i])
        pre_maxv[i]=max(pre_maxv[i-1],vs_u[i])
    suf_minv = [0]*n; suf_maxv = [0]*n
    suf_minv[n-1]=vs_u[n-1]; suf_maxv[n-1]=vs_u[n-1]
    for i in range(n-2,-1,-1):
        suf_minv[i]=min(suf_minv[i+1],vs_u[i])
        suf_maxv[i]=max(suf_maxv[i+1],vs_u[i])
    
    pre_minu = [0]*n; pre_maxu = [0]*n
    pre_minu[0]=us_v[0]; pre_maxu[0]=us_v[0]
    for i in range(1,n):
        pre_minu[i]=min(pre_minu[i-1],us_v[i])
        pre_maxu[i]=max(pre_maxu[i-1],us_v[i])
    suf_minu = [0]*n; suf_maxu = [0]*n
    suf_minu[n-1]=us_v[n-1]; suf_maxu[n-1]=us_v[n-1]
    for i in range(n-2,-1,-1):
        suf_minu[i]=min(suf_minu[i+1],us_v[i])
        suf_maxu[i]=max(suf_maxu[i+1],us_v[i])
    
    def check(D):
        for i in range(n-1):
            if us[i]-us[0]>D: break
            if pre_maxv[i]-pre_minv[i]<=D:
                if us[n-1]-us[i+1]<=D and suf_maxv[i+1]-suf_minv[i+1]<=D:
                    return True
        if us[n-1]-us[0]<=D and pre_maxv[n-1]-pre_minv[n-1]<=D:
            return True
        for i in range(n-1):
            if vs[i]-vs[0]>D: break
            if pre_maxu[i]-pre_minu[i]<=D:
                if vs[n-1]-vs[i+1]<=D and suf_maxu[i+1]-suf_minu[i+1]<=D:
                    return True
        if vs[n-1]-vs[0]<=D and pre_maxu[n-1]-pre_minu[n-1]<=D:
            return True
        return False
    
    lo, hi = 0, 2*10**9
    while lo < hi:
        mid = (lo+hi)//2
        if check(mid):
            hi = mid
        else:
            lo = mid+1
    print(lo)

solve()
```