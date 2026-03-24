import sys
import math

sys.setrecursionlimit(200000)

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    N = int(input_data[0])
    M = int(input_data[1])
    
    S = [0] * (N + 1)
    for i in range(1, N + 1):
        S[i] = int(input_data[1 + i])
        
    tree_ans = [0] * (4 * N + 1)
    tree_tg = [0] * (4 * N + 1)
    tree_pref = [None] * (4 * N + 1)
    tree_suff = [None] * (4 * N + 1)
    
    gcd = math.gcd
    
    def merge(l_ans, l_tg, l_pref, l_suff, r_ans, r_tg, r_pref, r_suff):
        ans = l_ans + r_ans
        for lg, lc in l_suff:
            if lg == 1: continue
            for rg, rc in r_pref:
                if rg == 1: continue
                if gcd(lg, rg) > 1:
                    ans += lc * rc
                    
        tg = gcd(l_tg, r_tg)
        
        pref = list(l_pref)
        if l_tg == 1:
            sum_c = sum(c for g, c in r_pref)
            if pref[-1][0] == 1:
                pref[-1] = (1, pref[-1][1] + sum_c)
            else:
                pref.append((1, sum_c))
        else:
            for g, c in r_pref:
                ng = gcd(l_tg, g)
                if pref[-1][0] == ng:
                    pref[-1] = (ng, pref[-1][1] + c)
                else:
                    pref.append((ng, c))
                    
        suff = list(r_suff)
        if r_tg == 1:
            sum_c = sum(c for g, c in l_suff)
            if suff[-1][0] == 1:
                suff[-1] = (1, suff[-1][1] + sum_c)
            else:
                suff.append((1, sum_c))
        else:
            for g, c in l_suff:
                ng = gcd(r_tg, g)
                if suff[-1][0] == ng:
                    suff[-1] = (ng, suff[-1][1] + c)
                else:
                    suff.append((ng, c))
                    
        return ans, tg, pref, suff

    def build(node, start, end):
        if start == end:
            v = S[start]
            tree_ans[node] = 1 if v > 1 else 0
            tree_tg[node] = v
            tree_pref[node] = [(v, 1)]
            tree_suff[node] = [(v, 1)]
            return
        
        mid = (start + end) // 2
        left = 2 * node
        right = 2 * node + 1
        
        build(left, start, mid)
        build(right, mid + 1, end)
        
        ans, tg, pref, suff = merge(
            tree_ans[left], tree_tg[left], tree_pref[left], tree_suff[left],
            tree_ans[right], tree_tg[right], tree_pref[right], tree_suff[right]
        )
        tree_ans[node] = ans
        tree_tg[node] = tg
        tree_pref[node] = pref
        tree_suff[node] = suff

    def update(node, start, end, idx, val):
        if start == end:
            tree_ans[node] = 1 if val > 1 else 0
            tree_tg[node] = val
            tree_pref[node] = [(val, 1)]
            tree_suff[node] = [(val, 1)]
            return
        
        mid = (start + end) // 2
        left = 2 * node
        right = 2 * node + 1
        
        if idx <= mid:
            update(left, start, mid, idx, val)
        else:
            update(right, mid + 1, end, idx, val)
            
        ans, tg, pref, suff = merge(
            tree_ans[left], tree_tg[left], tree_pref[left], tree_suff[left],
            tree_ans[right], tree_tg[right], tree_pref[right], tree_suff[right]
        )
        tree_ans[node] = ans
        tree_tg[node] = tg
        tree_pref[node] = pref
        tree_suff[node] = suff

    def query(node, start, end, l, r):
        if l <= start and end <= r:
            return tree_ans[node], tree_tg[node], tree_pref[node], tree_suff[node]
        
        mid = (start + end) // 2
        left = 2 * node
        right = 2 * node + 1
        
        if r <= mid:
            return query(left, start, mid, l, r)
        elif l > mid:
            return query(right, mid + 1, end, l, r)
        else:
            l_res = query(left, start, mid, l, r)
            r_res = query(right, mid + 1, end, l, r)
            return merge(
                l_res[0], l_res[1], l_res[2], l_res[3],
                r_res[0], r_res[1], r_res[2], r_res[3]
            )

    build(1, 1, N)
    
    idx = 2 + N
    out = []
    for _ in range(M):
        type_op = int(input_data[idx])
        if type_op == 1:
            I = int(input_data[idx+1])
            V = int(input_data[idx+2])
            update(1, 1, N, I, V)
        else:
            E = int(input_data[idx+1])
            D = int(input_data[idx+2])
            ans, _, _, _ = query(1, 1, N, E, D)
            out.append(str(ans))
        idx += 3
        
    if out:
        print('\n'.join(out))

if __name__ == '__main__':
    solve()