Looking at this problem, I need to:

1. Maintain N buckets, each with a list of balls
2. Support two operations:
   - Add a ball to bucket i
   - Query the maximum absolute difference between balls from **distinct** buckets in range [a, b]

For the query, I need the maximum and minimum values across all buckets in [a,b], BUT they must come from distinct buckets. The answer is max_val - min_val, UNLESS max and min are in the same bucket. In that case, I need to consider alternatives.

Wait, let me think more carefully. The maximum absolute difference between two balls from distinct buckets is:
- Either (global_max - global_min) if they're in different buckets
- Or if they're in the same bucket, I need to consider:
  - (global_max - second_min) where second_min is min from a different bucket than global_max
  - (second_max - global_min) where second_max is max from a different bucket than global_min

So for each bucket, I need to track its local max and local min. Then for the range query, I need the top-2 maxes (from different buckets) and top-2 mins (from different buckets).

Actually, let me think with segment tree where each node stores:
- `max1`, `max1_bucket`: the maximum value and which bucket it's from
- `max2`, `max2_bucket`: second maximum from a different bucket
- `min1`, `min1_bucket`: the minimum value and which bucket it's from  
- `min2`, `min2_bucket`: second minimum from a different bucket

Each bucket's contribution: its local max and local min.

For the segment tree, each leaf stores the bucket's current max and min. Internal nodes merge these.

Given N, M ≤ 10^5, a segment tree with O(log N) per query/update should work.

For updates: when a ball is added to bucket i, update the leaf for bucket i (update its local max/min if needed), then propagate up.

For queries: query range [a,b] to get the structure, then compute the answer.

The merge needs to track top-2 maxes and top-2 mins by bucket identity.

```python
import sys
from math import inf

def main():
    input_data = sys.stdin.buffer.read().split()
    idx = 0
    N = int(input_data[idx]); idx+=1
    M = int(input_data[idx]); idx+=1
    
    # Each bucket: store local max and min
    bucket_max = [0]*(N+1)
    bucket_min = [0]*(N+1)
    
    for i in range(1, N+1):
        v = int(input_data[idx]); idx+=1
        bucket_max[i] = v
        bucket_min[i] = v
    
    # Segment tree: each node stores (max1_val, max1_bkt, max2_val, max2_bkt, min1_val, min1_bkt, min2_val, min2_bkt)
    # ... build and query
```

Let me implement this fully:

import sys

def main():
    data = sys.stdin.buffer.read().split()
    idx = 0
    N = int(data[idx]); idx+=1
    M = int(data[idx]); idx+=1
    
    INF = float('inf')
    bmax = [0]*(N+1)
    bmin = [0]*(N+1)
    for i in range(1,N+1):
        v=int(data[idx]);idx+=1
        bmax[i]=v;bmin[i]=v
    
    # seg tree nodes: arrays for speed
    size=1
    while size<N: size<<=1
    # store per node: mx1,mx1b,mx2,mx2b,mn1,mn1b,mn2,mn2b
    NONE=-1
    mx1=[0]*(2*size);mx1b=[NONE]*(2*size);mx2=[-INF]*(2*size);mx2b=[NONE]*(2*size)
    mn1=[0]*(2*size);mn1b=[NONE]*(2*size);mn2=[INF]*(2*size);mn2b=[NONE]*(2*size)

    # ... (full implementation below)

Let me write the complete solution:

import sys

def main():
    data = sys.stdin.buffer.read().split()
    idx = 0
    N = int(data[idx]); idx += 1
    M = int(data[idx]); idx += 1
    INF = float('inf')
    bmax = [0]*(N+1)
    bmin = [0]*(N+1)
    for i in range(1, N+1):
        v = int(data[idx]); idx += 1
        bmax[i] = v; bmin[i] = v

    size = 1
    while size < N: size <<= 1
    mx1 = [-INF]*(2*size); mx1b = [-1]*(2*size)
    mx2 = [-INF]*(2*size); mx2b = [-1]*(2*size)
    mn1 = [INF]*(2*size); mn1b = [-1]*(2*size)
    mn2 = [INF]*(2*size); mn2b = [-1]*(2*size)

    def merge(node, l, r):
        # merge max
        vals = []
        for src in [l, r]:
            if mx1b[src] != -1:
                vals.append((mx1[src], mx1b[src]))
            if mx2b[src] != -1:
                vals.append((mx2[src], mx2b[src]))
        vals.sort(key=lambda x: -x[0])
        mx1[node] = -INF; mx1b[node] = -1; mx2[node] = -INF; mx2b[node] = -1
        for v, b in vals:
            if mx1b[node] == -1:
                mx1[node] = v; mx1b[node] = b
            elif b != mx1b[node]:
                mx2[node] = v; mx2b[node] = b
                break
        # merge min
        vals = []
        for src in [l, r]:
            if mn1b[src] != -1:
                vals.append((mn1[src], mn1b[src]))
            if mn2b[src] != -1:
                vals.append((mn2[src], mn2b[src]))
        vals.sort(key=lambda x: x[0])
        mn1[node] = INF; mn1b[node] = -1; mn2[node] = INF; mn2b[node] = -1
        for v, b in vals:
            if mn1b[node] == -1:
                mn1[node] = v; mn1b[node] = b
            elif b != mn1b[node]:
                mn2[node] = v; mn2b[node] = b
                break

    # build
    for i in range(1, N+1):
        pos = size + i - 1
        mx1[pos] = bmax[i]; mx1b[pos] = i
        mn1[pos] = bmin[i]; mn1b[pos] = i
    for i in range(size-1, 0, -1):
        merge(i, 2*i, 2*i+1)

    def update(i):
        pos = size + i - 1
        mx1[pos] = bmax[i]; mx1b[pos] = i
        mn1[pos] = bmin[i]; mn1b[pos] = i
        pos >>= 1
        while pos >= 1:
            merge(pos, 2*pos, 2*pos+1)
            pos >>= 1

    def query(l, r):
        # returns (mx1,mx1b,mx2,mx2b,mn1,mn1b,mn2,mn2b)
        res_mx1=-INF;res_mx1b=-1;res_mx2=-INF;res_mx2b=-1
        res_mn1=INF;res_mn1b=-1;res_mn2=INF;res_mn2b=-1
        l += size-1; r += size-1
        stack=[]
        lo,hi=l,r
        while lo<=hi:
            if lo%2==1:
                stack.append(lo); lo+=1
            if hi%2==0:
                stack.append(hi); hi-=1
            lo>>=1; hi>>=1
        for node in stack:
            # merge into result max
            for v,b in [(mx1[node],mx1b[node]),(mx2[node],mx2b[node])]:
                if b==-1: continue
                if res_mx1b==-1:
                    res_mx1=v;res_mx1b=b
                elif v>res_mx1:
                    if b!=res_mx1b:
                        res_mx2=res_mx1;res_mx2b=res_mx1b
                    res_mx1=v;res_mx1b=b
                elif b!=res_mx1b and v>res_mx2:
                    res_mx2=v;res_mx2b=b
            # merge into result min
            for v,b in [(mn1[node],mn1b[node]),(mn2[node],mn2b[node])]:
                if b==-1: continue
                if res_mn1b==-1:
                    res_mn1=v;res_mn1b=b
                elif v<res_mn1:
                    if b!=res_mn1b:
                        res_mn2=res_mn1;res_mn2b=res_mn1b
                    res_mn1=v;res_mn1b=b
                elif b!=res_mn1b and v<res_mn2:
                    res_mn2=v;res_mn2b=b
        return res_mx1,res_mx1b,res_mx2,res_mx2b,res_mn1,res_mn1b,res_mn2,res_mn2b

    out=[]
    for _ in range(M):
        op=int(data[idx]);idx+=1
        x=int(data[idx]);idx+=1
        y=int(data[idx]);idx+=1
        if op==1:
            p=x;i=y
            if p>bmax[i]: bmax[i]=p
            if p<bmin[i]: bmin[i]=p
            update(i)
        else:
            a=x;b=y
            r=query(a,b)
            mx1v,mx1bk,mx2v,mx2bk,mn1v,mn1bk,mn2v,mn2bk=r
            # answer: max - min from distinct buckets
            best=0
            if mx1bk!=mn1bk:
                best=mx1v-mn1v
            else:
                c1=mx1v-mn2v if mn2bk!=-1 else -INF
                c2=mx2v-mn1v if mx2bk!=-1 else -INF
                best=max(c1,c2)
            out.append(best)
    print('\n'.join(map(str,out)))

main()