import sys
from math import inf

def main():
    input_data = sys.stdin.buffer.read().split()
    idx = 0
    
    N = int(input_data[idx]); idx += 1
    M = int(input_data[idx]); idx += 1
    
    # Each bucket stores min and max ball weight
    bucket_min = [0] * (N + 1)
    bucket_max = [0] * (N + 1)
    
    for i in range(1, N + 1):
        w = int(input_data[idx]); idx += 1
        bucket_min[i] = w
        bucket_max[i] = w
    
    # Segment tree storing (global_min, global_max, best_answer)
    # best_answer = max absolute difference between balls from distinct buckets
    # For a node covering range [l, r]:
    #   global_min = min of all balls in all buckets in [l,r]
    #   global_max = max of all balls in all buckets in [l,r]
    #   answer = best difference from distinct buckets
    
    # But we need to be careful: the max difference must come from distinct buckets
    # We need to track: for each segment, the min and max overall, plus the answer
    # When merging two segments L and R:
    #   answer = max(L.answer, R.answer, R.max - L.min, L.max - R.min)
    # This works because R.max and L.min are from different segments (different buckets)
    
    size = 1
    while size < N:
        size <<= 1
    
    # seg stores tuples (min_val, max_val, ans)
    # Initialize with identity
    INF = float('inf')
    seg_min = [INF] * (2 * size)
    seg_max = [-INF] * (2 * size)
    seg_ans = [-INF] * (2 * size)
    
    # Fill leaves
    for i in range(1, N + 1):
        pos = size + i - 1
        seg_min[pos] = bucket_min[i]
        seg_max[pos] = bucket_max[i]
        seg_ans[pos] = -INF  # single bucket, no valid pair from distinct buckets
    
    # Build
    for i in range(size - 1, 0, -1):
        lc = 2 * i
        rc = 2 * i + 1
        lmin, lmax, lans = seg_min[lc], seg_max[lc], seg_ans[lc]
        rmin, rmax, rans = seg_min[rc], seg_max[rc], seg_ans[rc]
        seg_min[i] = min(lmin, rmin)
        seg_max[i] = max(lmax, rmax)
        ans = -INF
        if lans != -INF: ans = max(ans, lans)
        if rans != -INF: ans = max(ans, rans)
        if lmin != INF and rmax != -INF: ans = max(ans, rmax - lmin)
        if rmin != INF and lmax != -INF: ans = max(ans, lmax - rmin)
        seg_ans[i] = ans
    
    def update(i, new_min, new_max):
        pos = size + i - 1
        seg_min[pos] = new_min
        seg_max[pos] = new_max
        seg_ans[pos] = -INF
        pos >>= 1
        while pos >= 1:
            lc = 2 * pos
            rc = 2 * pos + 1
            lmin, lmax, lans = seg_min[lc], seg_max[lc], seg_ans[lc]
            rmin, rmax, rans = seg_min[rc], seg_max[rc], seg_ans[rc]
            seg_min[pos] = min(lmin, rmin)
            seg_max[pos] = max(lmax, rmax)
            ans = -INF
            if lans != -INF: ans = max(ans, lans)
            if rans != -INF: ans = max(ans, rans)
            if lmin != INF and rmax != -INF: ans = max(ans, rmax - lmin)
            if rmin != INF and lmax != -INF: ans = max(ans, lmax - rmin)
            seg_ans[pos] = ans
            pos >>= 1
    
    def query(l, r):
        # returns (min, max, ans) for range [l, r] (1-indexed)
        res_min, res_max, res_ans = INF, -INF, -INF
        l += size - 1
        r += size - 1
        while l <= r:
            if l % 2 == 1:
                # merge (res) with seg[l]
                nm = min(res_min, seg_min[l])
                nx = max(res_max, seg_max[l])
                na = res_ans
                if seg_ans[l] != -INF: na = max(na, seg_ans[l])
                if res_min != INF and seg_max[l] != -INF: na = max(na, seg_max[l] - res_min)
                if seg_min[l] != INF and res_max != -INF: na = max(na, res_max - seg_min[l])
                res_min, res_max, res_ans = nm, nx, na
                l += 1
            if r % 2 == 0:
                nm = min(res_min, seg_min[r])
                nx = max(res_max, seg_max[r])
                na = res_ans
                if seg_ans[r] != -INF: na = max(na, seg_ans[r])
                if res_min != INF and seg_max[r] != -INF: na = max(na, seg_max[r] - res_min)
                if seg_min[r] != INF and res_max != -INF: na = max(na, res_max - seg_min[r])
                res_min, res_max, res_ans = nm, nx, na
                r -= 1
            l >>= 1
            r >>= 1
        return res_min, res_max, res_ans
    
    out = []
    for _ in range(M):
        op = int(input_data[idx]); idx += 1
        x = int(input_data[idx]); idx += 1
        y = int(input_data[idx]); idx += 1
        if op == 1:
            p, i = x, y
            bucket_min[i] = min(bucket_min[i], p)
            bucket_max[i] = max(bucket_max[i], p)
            update(i, bucket_min[i], bucket_max[i])
        else:
            a, b = x, y
            _, _, ans = query(a, b)
            out.append(ans)
    
    print('\n'.join(map(str, out)))

main()