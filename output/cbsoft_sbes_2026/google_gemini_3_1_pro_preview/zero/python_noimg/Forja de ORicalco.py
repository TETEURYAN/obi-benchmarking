import sys

def solve():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    
    N = int(data[0])
    K = int(data[1])
    A = [int(x) for x in data[2:N+2]]
    
    mod_K = K - 1
    
    tree_n = [max(1, (N - m) // mod_K + 1) for m in range(mod_K)]
    trees = [[10**18] * (2 * sz) for sz in tree_n]
    
    m = 0
    pos = 0
    tree = trees[m]
    idx = pos + tree_n[m]
    tree[idx] = 0
    idx >>= 1
    while idx > 0:
        left_node = idx << 1
        right_node = left_node | 1
        tree[idx] = tree[left_node] if tree[left_node] < tree[right_node] else tree[right_node]
        idx >>= 1
        
    current_ors = []
    INF = 10**18
    ans = 0
    
    for i in range(1, N + 1):
        a_i = A[i - 1]
        
        next_ors = []
        for val, left, right in current_ors:
            next_ors.append([val | a_i, left, right])
        next_ors.append([a_i, i, i])
        
        current_ors = []
        for val, left, right in next_ors:
            if current_ors and current_ors[-1][0] == val:
                current_ors[-1][2] = right
            else:
                current_ors.append([val, left, right])
                
        r = (i - 1) % mod_K
        ans = INF
        
        tree_r = trees[r]
        n_r = tree_n[r]
        
        for val, left, right in current_ors:
            rem_L = (left - 1) % mod_K
            pos_L = (left - 1) if rem_L == r else (left - 1) + (r - rem_L) % mod_K
            pos_L //= mod_K
            
            rem_R = (right - 1) % mod_K
            pos_R = (right - 1) if rem_R == r else (right - 1) - (rem_R - r) % mod_K
            pos_R //= mod_K
            
            if pos_L <= pos_R:
                l = pos_L + n_r
                rg = pos_R + n_r
                res = INF
                while l <= rg:
                    if l & 1:
                        if tree_r[l] < res: res = tree_r[l]
                        l += 1
                    if (rg & 1) == 0:
                        if tree_r[rg] < res: res = tree_r[rg]
                        rg -= 1
                    l >>= 1
                    rg >>= 1
                
                if res + val < ans:
                    ans = res + val
                    
        m = i % mod_K
        pos = i // mod_K
        
        tree_m = trees[m]
        idx = pos + tree_n[m]
        tree_m[idx] = ans
        idx >>= 1
        while idx > 0:
            left_node = idx << 1
            right_node = left_node | 1
            tree_m[idx] = tree_m[left_node] if tree_m[left_node] < tree_m[right_node] else tree_m[right_node]
            idx >>= 1

    print(ans)

if __name__ == '__main__':
    solve()