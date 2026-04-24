import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    N = int(input_data[0])
    K = int(input_data[1])
    T = int(input_data[2])
    
    P = [int(x) for x in input_data[3:3+N]]
    G = [int(x) for x in input_data[3+N:3+2*N]]
    
    A = []
    for i in range(N):
        if G[i] == 1:
            A.append(i + 1)
            
    INF = float('inf')
    max_possible_v = 9 * K
    dp = [[INF] * (max_possible_v + 1) for _ in range(K + 1)]
    dp[0][0] = 0
    
    max_v = [-1] * (K + 1)
    max_v[0] = 0
    
    for i in range(1, N + 1):
        p = P[i - 1]
        for j in range(min(i, K), 0, -1):
            if max_v[j - 1] == -1:
                continue
            
            cost = abs(A[j - 1] - i)
            dp_j = dp[j]
            dp_j_minus_1 = dp[j - 1]
            
            limit = max_v[j - 1]
            new_max_v = max_v[j]
            
            for prev_v in range(limit, -1, -1):
                c = dp_j_minus_1[prev_v]
                if c != INF:
                    new_cost = c + cost
                    if new_cost <= T:
                        v = prev_v + p
                        if new_cost < dp_j[v]:
                            dp_j[v] = new_cost
                            if v > new_max_v:
                                new_max_v = v
            max_v[j] = new_max_v
            
    ans = 0
    for v in range(max_v[K], -1, -1):
        if dp[K][v] <= T:
            ans = v
            break
            
    print(ans)

if __name__ == '__main__':
    solve()