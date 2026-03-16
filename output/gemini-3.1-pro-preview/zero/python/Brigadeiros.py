
import sys

def solve():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    
    N = int(data[0])
    K = int(data[1])
    T = int(data[2])
    
    P = [int(x) for x in data[3:3+N]]
    G = [int(x) for x in data[3+N:3+2*N]]
    
    S = []
    for i in range(N):
        if G[i] == 1:
            S.append(i + 1)
            
    inf = float('inf')
    max_possible_v = sum(sorted(P, reverse=True)[:K])
    
    dp = [[inf] * (max_possible_v + 1) for _ in range(K + 1)]
    dp[0][0] = 0
    
    max_reach = [-1] * (K + 1)
    max_reach[0] = 0
    
    for i in range(1, N + 1):
        p = P[i-1]
        min_j = max(1, K - N + i)
        max_j = min(i, K)
        
        for j in range(max_j, min_j - 1, -1):
            if max_reach[j-1] == -1:
                continue
            
            cost = abs(i - S[j-1])
            prev = dp[j-1]
            curr = dp[j]
            
            limit = max_reach[j-1]
            for v_minus_p in range(limit + 1):
                val = prev[v_minus_p]
                if val != inf:
                    c = val + cost
                    if c < curr[v_minus_p + p]:
                        curr[v_minus_p + p] = c
            
            if limit + p > max_reach[j]:
                max_reach[j] = limit + p
                
    ans = 0
    for v in range(max_possible_v, -1, -1):
        if dp[K][v] <= T:
            ans = v
            break
            
    print(ans)

if __name__ == '__main__':
    solve()
