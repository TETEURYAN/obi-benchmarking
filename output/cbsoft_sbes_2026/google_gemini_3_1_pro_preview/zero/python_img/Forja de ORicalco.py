
import sys

def solve():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    
    N = int(data[0])
    K = int(data[1])
    A = [int(x) for x in data[2:N+2]]
    
    K_minus_1 = K - 1
    
    counts = [0] * K_minus_1
    for r in range(K_minus_1):
        counts[r] = max(1, (N - r) // K_minus_1 + 1)
        
    INF = 10**18
    trees = [ [INF] * (2 * counts[r]) for r in range(K_minus_1) ]
    
    trees[0][counts[0]] = 0
    idx = counts[0] >> 1
    while idx > 0:
        left = trees[0][idx << 1]
        right = trees[0][(idx << 1) | 1]
        trees[0][idx] = left if left < right else right
        idx >>= 1
        
    intervals = []
    dp = [INF] * (N + 1)
    dp[0] = 0
    
    for i in range(1, N + 1):
        val_i = A[i-1]
        
        new_intervals = []
        for interval in intervals:
            new_val = interval[0] | val_i
            if not new_intervals or new_intervals[-1][0] != new_val:
                new_intervals.append([new_val, interval[1], interval[2]])
            else:
                new_intervals[-1][2] = interval[2]
                
        if not new_intervals or new_intervals[-1][0] != val_i:
            new_intervals.append([val_i, i - 1, i - 1])
        else:
            new_intervals[-1][2] = i - 1
            
        intervals = new_intervals
        
        r = (i - 1) % K_minus_1
        t = trees[r]
        n = counts[r]
        
        min_dp = INF
        for val, L, R in intervals:
            start_p = L + (r - L) % K_minus_1
            if start_p > R:
                continue
            
            l = (start_p // K_minus_1) + n
            right_idx = (R - (R - r) % K_minus_1) // K_minus_1 + 1 + n
            
            res = INF
            while l < right_idx:
                if l & 1:
                    if t[l] < res: res = t[l]
                    l += 1
                if right_idx & 1:
                    right_idx -= 1
                    if t[right_idx] < res: res = t[right_idx]
                l >>= 1
                right_idx >>= 1
            
            if res != INF:
                cand = res + val
                if cand < min_dp:
                    min_dp = cand
                    
        dp[i] = min_dp
        
        rem = i % K_minus_1
        idx = (i // K_minus_1) + counts[rem]
        t_upd = trees[rem]
        if min_dp < t_upd[idx]:
            t_upd[idx] = min_dp
            idx >>= 1
            while idx > 0:
                left = t_upd[idx << 1]
                right = t_upd[(idx << 1) | 1]
                t_upd[idx] = left if left < right else right
                idx >>= 1
                
    print(dp[N])

if __name__ == '__main__':
    solve()
