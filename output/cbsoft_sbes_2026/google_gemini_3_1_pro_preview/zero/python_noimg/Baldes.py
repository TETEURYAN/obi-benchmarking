
import sys

sys.setrecursionlimit(200005)

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    N = int(input_data[0])
    M = int(input_data[1])
    
    initial_weights = [0] * (N + 1)
    idx = 2
    for i in range(1, N + 1):
        initial_weights[i] = int(input_data[idx])
        idx += 1
        
    MAX_NODES = 4 * N + 1
    INF = 10**15
    
    max1_w = [0] * MAX_NODES
    max1_i = [0] * MAX_NODES
    max2_w = [0] * MAX_NODES
    max2_i = [0] * MAX_NODES
    min1_w = [0] * MAX_NODES
    min1_i = [0] * MAX_NODES
    min2_w = [0] * MAX_NODES
    min2_i = [0] * MAX_NODES
    ans = [0] * MAX_NODES
    
    def merge(node, lc, rc):
        l_max1_w, l_max1_i = max1_w[lc], max1_i[lc]
        l_max2_w, l_max2_i = max2_w[lc], max2_i[lc]
        r_max1_w, r_max1_i = max1_w[rc], max1_i[rc]
        r_max2_w, r_max2_i = max2_w[rc], max2_i[rc]
        
        if l_max1_w > r_max1_w:
            max1_w[node], max1_i[node] = l_max1_w, l_max1_i
            c1w, c1i = l_max1_w, l_max1_i
            c2w, c2i = l_max2_w, l_max2_i
            c3w, c3i = r_max1_w, r_max1_i
            c4w, c4i = r_max2_w, r_max2_i
        else:
            max1_w[node], max1_i[node] = r_max1_w, r_max1_i
            c1w, c1i = r_max1_w, r_max1_i
            c2w, c2i = r_max2_w, r_max2_i
            c3w, c3i = l_max1_w, l_max1_i
            c4w, c4i = l_max2_w, l_max2_i
            
        n_max2_w, n_max2_i = -1, -1
        if c2i != -1 and c2i != c1i and c2w > n_max2_w: n_max2_w, n_max2_i = c2w, c2i
        if c3i != -1 and c3i != c1i and c3w > n_max2_w: n_max2_w, n_max2_i = c3w, c3i
        if c4i != -1 and c4i != c1i and c4w > n_max2_w: n_max2_w, n_max2_i = c4w, c4i
        max2_w[node], max2_i[node] = n_max2_w, n_max2_i

        l_min1_w, l_min1_i = min1_w[lc], min1_i[lc]
        l_min2_w, l_min2_i = min2_w[lc], min2_i[lc]
        r_min1_w, r_min1_i = min1_w[rc], min1_i[rc]
        r_min2_w, r_min2_i = min2_w[rc], min2_i[rc]

        if l_min1_w < r_min1_w:
            min1_w[node], min1_i[node] = l_min1_w, l_min1_i
            c1w, c1i = l_min1_w, l_min1_i
            c2w, c2i = l_min2_w, l_min2_i
            c3w, c3i = r_min1_w, r_min1_i
            c4w, c4i = r_min2_w, r_min2_i
        else:
            min1_w[node], min1_i[node] = r_min1_w, r_min1_i
            c1w, c1i = r_min1_w, r_min1_i
            c2w, c2i = r_min2_w, r_min2_i
            c3w, c3i = l_min1_w, l_min1_i
            c4w, c4i = l_min2_w, l_min2_i
            
        n_min2_w, n_min2_i = INF, -1
        if c2i != -1 and c2i != c1i and c2w < n_min2_w: n_min2_w, n_min2_i = c2w, c2i
        if c3i != -1 and c3i != c1i and c3w < n_min2_w: n_min2_w, n_min2_i = c3w, c3i
        if c4i != -1 and c4i != c1i and c4w < n_min2_w: n_min2_w, n_min2_i = c4w, c4i
        min2_w[node], min2_i[node] = n_min2_w, n_min2_i

        n_ans = ans[lc] if ans[lc] > ans[rc] else ans[rc]
        
        if l_max1_i != -1 and r_min1_i != -1 and l_max1_i != r_min1_i:
            if l_max1_w - r_min1_w > n_ans: n_ans = l_max1_w - r_min1_w
        if l_max1_i != -1 and r_min2_i != -1 and l_max1_i != r_min2_i:
            if l_max1_w - r_min2_w > n_ans: n_ans = l_max1_w - r_min2_w
        if l_max2_i != -1 and r_min1_i != -1 and l_max2_i != r_min1_i:
            if l_max2_w - r_min1_w > n_ans: n_ans = l_max2_w - r_min1_w
            
        if r_max1_i != -1 and l_min1_i != -1 and r_max1_i != l_min1_i:
            if r_max1_w - l_min1_w > n_ans: n_ans = r_max1_w - l_min1_w
        if r_max1_i != -1 and l_min2_i != -1 and r_max1_i != l_min2_i:
            if r_max1_w - l_min2_w > n_ans: n_ans = r_max1_w - l_min2_w
        if r_max2_i != -1 and l_min1_i != -1 and r_max2_i != l_min1_i:
            if r_max2_w - l_min1_w > n_ans: n_ans = r_max2_w - l_min1_w
            
        ans[node] = n_ans

    def build(node, l, r):
        if l == r:
            w = initial_weights[l]
            max1_w[node] = w
            max1_i[node] = l
            max2_w[node] = -1
            max2_i[node] = -1
            min1_w[node] = w
            min1_i[node] = l
            min2_w[node] = INF
            min2_i[node] = -1
            ans[node] = -1
            return
        mid = (l + r) // 2
        build(2 * node, l, mid)
        build(2 * node + 1, mid + 1, r)
        merge(node, 2 * node, 2 * node + 1)

    def update(node, l, r, pos, p):
        if l == r:
            if p > max1_w[node]:
                max1_w[node] = p
            if p < min1_w[node]:
                min1_w[node] = p
            return
        mid = (l + r) // 2
        if pos <= mid:
            update(2 * node, l, mid, pos, p)
        else:
            update(2 * node + 1, mid + 1, r, pos, p)
        merge(node, 2 * node, 2 * node + 1)

    def merge_tuples(L, R):
        if not L: return R
        if not R: return L
        
        l_max1_w, l_max1_i, l_max2_w, l_max2_i, l_min1_w, l_min1_i, l_min2_w, l_min2_i, l_ans = L
        r_max1_w, r_max1_i, r_max2_w, r_max2_i, r_min1_w, r_min1_i, r_min2_w, r_min2_i, r_ans = R
        
        if l_max1_w > r_max1_w:
            n_max1_w, n_max1_i = l_max1_w, l_max1_i
            c1w, c1i = l_max1_w, l_max1_i
            c2w, c2i = l_max2_w, l_max2_i
            c3w, c3i = r_max1_w, r_max1_i
            c4w, c4i = r_max2_w, r_max2_i
        else:
            n_max1_w, n_max1_i = r_max1_w, r_max1_i
            c1w, c1i = r_max1_w, r_max1_i
            c2w, c2i = r_max2_w, r_max2_i
            c3w, c3i = l_max1_w, l_max1_i
            c4w, c4i = l_max2_w, l_max2_i
            
        n_max2_w, n_max2_i = -1, -1
        if c2i != -1 and c2i != c1i and c2w > n_max2_w: n_max2_w, n_max2_i = c2w, c2i
        if c3i != -1 and c3i != c1i and c3w > n_max2_w: n_max2_w, n_max2_i = c3w, c3i
        if c4i != -1 and c4i != c1i and c4w > n_max2_w: n_max2_w, n_max2_i = c4w, c4i

        if l_min1_w < r_min1_w:
            n_min1_w, n_min1_i = l_min1_w, l_min1_i
            c1w, c1i = l_min1_w, l_min1_i
            c2w, c2i = l_min2_w, l_min2_i
            c3w, c3i = r_min1_w, r_min1_i
            c4w, c4i = r_min2_w, r_min2_i
        else:
            n_min1_w, n_min1_i = r_min1_w, r_min1_i
            c1w, c1i = r_min1_w, r_min1_i
            c2w, c2i = r_min2_w, r_min2_i
            c3w, c3i = l_min1_w, l_min1_i
            c4w, c4i = l_min2_w, l_min2_i
            
        n_min2_w, n_min2_i = INF, -1
        if c2i != -1 and c2i != c1i and c2w < n_min2_w: n_min2_w, n_min2_i = c2w, c2i
        if c3i != -1 and c3i != c1i and c3w < n_min2_w: n_min2_w, n_min2_i = c3w, c3i
        if c4i != -1 and c4i != c1i and c4w < n_min2_w: n_min2_w, n_min2_i = c4w, c4i

        n_ans = l_ans if l_ans > r_ans else r_ans
        
        if l_max1_i != -1 and r_min1_i != -1 and l_max1_i != r_min1_i:
            if l_max1_w - r_min1_w > n_ans: n_ans = l_max1_w - r_min1_w
        if l_max1_i != -1 and r_min2_i != -1 and l_max1_i != r_min2_i:
            if l_max1_w - r_min2_w > n_ans: n_ans = l_max1_w - r_min2_w
        if l_max2_i != -1 and r_min1_i != -1 and l_max2_i != r_min1_i:
            if l_max2_w - r_min1_w > n_ans: n_ans = l_max2_w - r_min1_w
            
        if r_max1_i != -1 and l_min1_i != -1 and r_max1_i != l_min1_i:
            if r_max1_w - l_min1_w > n_ans: n_ans = r_max1_w - l_min1_w
        if r_max1_i != -1 and l_min2_i != -1 and r_max1_i != l_min2_i:
            if r_max1_w - l_min2_w > n_ans: n_ans = r_max1_w - l_min2_w
        if r_max2_i != -1 and l_min1_i != -1 and r_max2_i != l_min1_i:
            if r_max2_w - l_min1_w > n_ans: n_ans = r_max2_w - l_min1_w
            
        return (n_max1_w, n_max1_i, n_max2_w, n_max2_i, n_min1_w, n_min1_i, n_min2_w, n_min2_i, n_ans)

    def query(node, l, r, ql, qr):
        if ql <= l and r <= qr:
            return (max1_w[node], max1_i[node], max2_w[node], max2_i[node],
                    min1_w[node], min1_i[node], min2_w[node], min2_i[node], ans[node])
        mid = (l + r) // 2
        if qr <= mid:
            return query(2 * node, l, mid, ql, qr)
        elif ql > mid:
            return query(2 * node + 1, mid + 1, r, ql, qr)
        else:
            return merge_tuples(
                query(2 * node, l, mid, ql, qr),
                query(2 * node + 1, mid + 1, r, ql, qr)
            )

    build(1, 1, N)
    
    out = []
    for _ in range(M):
        op = int(input_data[idx])
        if op == 1:
            p = int(input_data[idx+1])
            i = int(input_data[idx+2])
            update(1, 1, N, i, p)
            idx += 3
        else:
            a = int(input_data[idx+1])
            b = int(input_data[idx+2])
            res = query(1, 1, N, a, b)
            out.append(str(res[8]))
            idx += 3
            
    sys.stdout.write('\n'.join(out) + '\n')

if __name__ == '__main__':
    solve()
