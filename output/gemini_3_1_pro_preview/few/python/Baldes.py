import sys

sys.setrecursionlimit(200005)

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    N = int(input_data[0])
    M = int(input_data[1])
    
    W = [0] * (N + 1)
    for i in range(1, N + 1):
        W[i] = int(input_data[1 + i])
        
    INF = 10**18
    
    max1 = [0] * (4 * N + 1)
    id_max1 = [0] * (4 * N + 1)
    max2 = [0] * (4 * N + 1)
    id_max2 = [0] * (4 * N + 1)
    min1 = [0] * (4 * N + 1)
    id_min1 = [0] * (4 * N + 1)
    min2 = [0] * (4 * N + 1)
    id_min2 = [0] * (4 * N + 1)
    
    def build(node, l, r):
        if l == r:
            max1[node] = W[l]
            id_max1[node] = l
            max2[node] = -INF
            id_max2[node] = -1
            min1[node] = W[l]
            id_min1[node] = l
            min2[node] = INF
            id_min2[node] = -1
            return
        mid = (l + r) // 2
        build(2 * node, l, mid)
        build(2 * node + 1, mid + 1, r)
        
        left = 2 * node
        right = 2 * node + 1
        
        if max1[left] > max1[right]:
            max1[node] = max1[left]
            id_max1[node] = id_max1[left]
            if max2[left] > max1[right]:
                max2[node] = max2[left]
                id_max2[node] = id_max2[left]
            else:
                max2[node] = max1[right]
                id_max2[node] = id_max1[right]
        else:
            max1[node] = max1[right]
            id_max1[node] = id_max1[right]
            if max1[left] > max2[right]:
                max2[node] = max1[left]
                id_max2[node] = id_max1[left]
            else:
                max2[node] = max2[right]
                id_max2[node] = id_max2[right]
                
        if min1[left] < min1[right]:
            min1[node] = min1[left]
            id_min1[node] = id_min1[left]
            if min2[left] < min1[right]:
                min2[node] = min2[left]
                id_min2[node] = id_min2[left]
            else:
                min2[node] = min1[right]
                id_min2[node] = id_min1[right]
        else:
            min1[node] = min1[right]
            id_min1[node] = id_min1[right]
            if min1[left] < min2[right]:
                min2[node] = min1[left]
                id_min2[node] = id_min1[left]
            else:
                min2[node] = min2[right]
                id_min2[node] = id_min2[right]

    build(1, 1, N)
    
    def update(node, l, r, idx, val):
        if l == r:
            if val > max1[node]: max1[node] = val
            if val < min1[node]: min1[node] = val
            return
        mid = (l + r) // 2
        if idx <= mid:
            update(2 * node, l, mid, idx, val)
        else:
            update(2 * node + 1, mid + 1, r, idx, val)
            
        left = 2 * node
        right = 2 * node + 1
        
        if max1[left] > max1[right]:
            max1[node] = max1[left]
            id_max1[node] = id_max1[left]
            if max2[left] > max1[right]:
                max2[node] = max2[left]
                id_max2[node] = id_max2[left]
            else:
                max2[node] = max1[right]
                id_max2[node] = id_max1[right]
        else:
            max1[node] = max1[right]
            id_max1[node] = id_max1[right]
            if max1[left] > max2[right]:
                max2[node] = max1[left]
                id_max2[node] = id_max1[left]
            else:
                max2[node] = max2[right]
                id_max2[node] = id_max2[right]
                
        if min1[left] < min1[right]:
            min1[node] = min1[left]
            id_min1[node] = id_min1[left]
            if min2[left] < min1[right]:
                min2[node] = min2[left]
                id_min2[node] = id_min2[left]
            else:
                min2[node] = min1[right]
                id_min2[node] = id_min1[right]
        else:
            min1[node] = min1[right]
            id_min1[node] = id_min1[right]
            if min1[left] < min2[right]:
                min2[node] = min1[left]
                id_min2[node] = id_min1[left]
            else:
                min2[node] = min2[right]
                id_min2[node] = id_min2[right]

    def merge_tuples(A, B):
        if A is None: return B
        if B is None: return A
        
        a_max1, a_id_max1, a_max2, a_id_max2, a_min1, a_id_min1, a_min2, a_id_min2 = A
        b_max1, b_id_max1, b_max2, b_id_max2, b_min1, b_id_min1, b_min2, b_id_min2 = B
        
        if a_max1 > b_max1:
            r_max1, r_id_max1 = a_max1, a_id_max1
            if a_max2 > b_max1:
                r_max2, r_id_max2 = a_max2, a_id_max2
            else:
                r_max2, r_id_max2 = b_max1, b_id_max1
        else:
            r_max1, r_id_max1 = b_max1, b_id_max1
            if a_max1 > b_max2:
                r_max2, r_id_max2 = a_max1, a_id_max1
            else:
                r_max2, r_id_max2 = b_max2, b_id_max2
                
        if a_min1 < b_min1:
            r_min1, r_id_min1 = a_min1, a_id_min1
            if a_min2 < b_min1:
                r_min2, r_id_min2 = a_min2, a_id_min2
            else:
                r_min2, r_id_min2 = b_min1, b_id_min1
        else:
            r_min1, r_id_min1 = b_min1, b_id_min1
            if a_min1 < b_min2:
                r_min2, r_id_min2 = a_min1, a_id_min1
            else:
                r_min2, r_id_min2 = b_min2, b_id_min2
                
        return (r_max1, r_id_max1, r_max2, r_id_max2, r_min1, r_id_min1, r_min2, r_id_min2)

    def query(node, l, r, ql, qr):
        if ql <= l and r <= qr:
            return (max1[node], id_max1[node], max2[node], id_max2[node],
                    min1[node], id_min1[node], min2[node], id_min2[node])
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

    idx = 1 + N + 1
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
            q_max1, q_id_max1, q_max2, q_id_max2, q_min1, q_id_min1, q_min2, q_id_min2 = res
            
            ans = -1
            if q_id_max1 != q_id_min1:
                if q_max1 - q_min1 > ans: ans = q_max1 - q_min1
            if q_id_max1 != q_id_min2 and q_id_min2 != -1:
                if q_max1 - q_min2 > ans: ans = q_max1 - q_min2
            if q_id_max2 != q_id_min1 and q_id_max2 != -1:
                if q_max2 - q_min1 > ans: ans = q_max2 - q_min1
            if q_id_max2 != q_id_min2 and q_id_max2 != -1 and q_id_min2 != -1:
                if q_max2 - q_min2 > ans: ans = q_max2 - q_min2
                
            out.append(str(ans))
            idx += 3
            
    if out:
        print('\n'.join(out))

solve()