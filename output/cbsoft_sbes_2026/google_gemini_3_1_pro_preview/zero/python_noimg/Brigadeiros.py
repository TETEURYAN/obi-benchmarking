
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
    
    A = [i + 1 for i, g in enumerate(G) if g == 1]
    
    INF = 10**15
    MAX_V = 9 * K + 1
    dp = [[INF] * MAX_V for _ in range(K + 1)]
    dp[0][0] = 0
    
    max_v = [0] * (K + 1)
    
    for i in range(1, N + 1):
        p = P[i - 1]
        for j in range(min(i, K), 0, -1):
            cost_add = abs(A[j - 1] - i)
            limit = max_v[j - 1]
            dp_j = dp[j]
            dp_prev = dp[j - 1]
            
            new_max = max_v[j]
            for v in range(limit, -1, -1):
                c = dp_prev[v] + cost_add
                if c <= T:
                    vp = v + p
                    if c < dp_j[vp]:
                        dp_j[vp] = c
                    if vp > new_max:
                        new_max = vp
            max_v[j] = new_max

    ans = 0
    for v in range(MAX_V - 1, -1, -1):
        if dp[K][v] <= T:
            ans = v
            break
            
    print(ans)

if __name__ == '__main__':
    solve()
