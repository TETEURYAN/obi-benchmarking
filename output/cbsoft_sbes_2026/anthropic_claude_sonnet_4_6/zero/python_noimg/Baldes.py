
import sys
from math import inf

input = sys.stdin.readline

def main():
    import sys
    from sys import stdin
    
    data = stdin.read().split()
    idx = 0
    
    N, M = int(data[idx]), int(data[idx+1])
    idx += 2
    
    # Each bucket stores list of balls
    # For segment tree, each node stores (max_val, min_val, max_of_second_max, min_of_second_min)
    # Actually we need: for a range of buckets, the maximum ball weight and minimum ball weight
    # BUT they must come from DISTINCT buckets
    # 
    # For each node we store:
    # - global_max: maximum ball weight in range
    # - global_min: minimum ball weight in range
    # - best_diff: best answer for this range (max diff from distinct buckets)
    # - max_bucket: which bucket has the global_max (if tie, any)
    # - min_bucket: which bucket has the global_min
    # - second_max: max ball weight from a bucket different from max_bucket
    # - second_min: min ball weight from a bucket different from min_bucket
    #
    # Actually simpler: store (max1, max1_bucket, max2_from_diff_bucket, min1, min1_bucket, min2_from_diff_bucket)
    # best_diff = max(max1 - min from diff bucket than max1, max from diff bucket than min1 - min1)
    
    # For each bucket, store max and min
    bucket_max = [0] * (N + 1)
    bucket_min = [0] * (N + 1)
    
    for i in range(1, N + 1):
        v = int(data[idx]); idx += 1
        bucket_max[i] = v
        bucket_min[i] = v
    
    # Segment tree node: (max_val, max_bucket, min_val, min_bucket, best_diff)
    # best_diff requires knowing max from one bucket and min from another
    
    size = 1
    while size < N:
        size <<= 1
    
    # Store for each node: max_val, max_bkt, second_max (from diff bkt), min_val, min_bkt, second_min (from diff bkt)
    INF = float('inf')
    
    seg_max = [-INF] * (2 * size)
    seg_max_bkt = [-1] * (2 * size)
    seg_smax = [-INF] * (2 * size)  # second max from different bucket
    seg_min = [INF] * (2 * size)
    seg_min_bkt = [-1] * (2 * size)
    seg_smin = [INF] * (2 * size)   # second min from different bucket
    
    def merge(lmx, lmb, lsmx, lmn, lmb2, lsmn, rmx, rmb, rsmx, rmn, rmb2, rsmn):
        # Compute merged node
        if lmx >= rmx:
            nmx, nmb = lmx, lmb
            nsmx = max(lsmx, rmx) if lmb != rmb else max(lsmx, rsmx if rmb != lmb else -INF)
            # simpler: second max from bucket != nmb
            nsmx = max(lsmx, rmx if rmb != nmb else rsmx)
        else:
            nmx, nmb = rmx, rmb
            nsmx = max(rmx if lmb != nmb else -INF, lmx if lmb != nmb else lsmx, rsmx)
            nsmx = max(lmx if lmb != nmb else lsmx, rsmx)
        
        if lmn <= rmn:
            nmn, nmb2 = lmn, lmb2
            nsmn = min(lsmn, rmn if rmb2 != nmb2 else rsmn)
        else:
            nmn, nmb2 = rmn, rmb2
            nsmn = min(rmn if lmb2 != nmb2 else rsmn, lsmn)
        
        return nmx, nmb, nsmx, nmn, nmb2, nsmn
    
    # Build
    for i in range(1, N + 1):
        pos = size + i - 1
        seg_max[pos] = bucket_max[i]
        seg_max_bkt[pos] = i
        seg_smax[pos] = -INF
        seg_min[pos] = bucket_min[i]
        seg_min_bkt[pos] = i
        seg_smin[pos] = INF
    
    for i in range(size - 1, 0, -1):
        l, r = 2*i, 2*i+1
        res = merge(seg_max[l],seg_max_bkt[l],seg_smax[l],seg_min[l],seg_min_bkt[l],seg_smin[l],
                    seg_max[r],seg_max_bkt[r],seg_smax[r],seg_min[r],seg_min_bkt[r],seg_smin[r])
        seg_max[i],seg_max_bkt[i],seg_smax[i],seg_min[i],seg_min_bkt[i],seg_smin[i] = res
    
    def update(bkt):
        pos = size + bkt - 1
        seg_max[pos] = bucket_max[bkt]
        seg_min[pos] = bucket_min[bkt]
        pos >>= 1
        while pos >= 1:
            l, r = 2*pos, 2*pos+1
            res = merge(seg_max[l],seg_max_bkt[l],seg_smax[l],seg_min[l],seg_min_bkt[l],seg_smin[l],
                        seg_max[r],seg_max_bkt[r],seg_smax[r],seg_min[r],seg_min_bkt[r],seg_smin[r])
            seg_max[pos],seg_max_bkt[pos],seg_smax[pos],seg_min[pos],seg_min_bkt[pos],seg_smin[pos] = res
            pos >>= 1
    
    def query(ql, qr):
        # returns (max_val, max_bkt, smax, min_val, min_bkt, smin)
        ql += size - 1
        qr += size - 1
        
        left_res = None
        right_res = None
        
        l, r = ql, qr
        while l <= r:
            if l & 1:
                node = (seg_max[l],seg_max_bkt[l],seg_smax[l],seg_min[l],seg_min_bkt[l],seg_smin[l])
                if left_res is None:
                    left_res = node
                else:
                    left_res = merge(*left_res, *node)
                l += 1
            if not (r & 1):
                node = (seg_max[r],seg_max_bkt[r],seg_smax[r],seg_min[r],seg_min_bkt[r],seg_smin[r])
                if right_res is None:
                    right_res = node
                else:
                    right_res = merge(*node, *right_res)
                r -= 1
            l >>= 1
            r >>= 1
        
        if left_res is None:
            return right_res
        if right_res is None:
            return left_res
        return merge(*left_res, *right_res)
    
    out = []
    for _ in range(M):
        op = int(data[idx]); idx += 1
        x, y = int(data[idx]), int(data[idx+1]); idx += 2
        
        if op == 1:
            p, i = x, y
            if p > bucket_max[i]:
                bucket_max[i] = p
            if p < bucket_min[i]:
                bucket_min[i] = p
            update(i)
        else:
            a, b = x, y
            res = query(a, b)
            mx, mb, smx, mn, mb2, smn = res
            # best diff: max - min from different buckets
            # if mb != mb2: mx - mn
            # else: max(mx - smn, smx - mn)
            if mb != mb2:
                out.append(mx - mn)
            else:
                out.append(max(mx - smn, smx - mn))
    
    print('\n'.join(map(str, out)))

main()