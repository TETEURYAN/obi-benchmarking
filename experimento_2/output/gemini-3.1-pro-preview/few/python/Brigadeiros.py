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
    
    x = []
    for i in range(N):
        if G[i] == 1:
            x.append(i + 1)
            
    INF = float('inf')
    prev_dp = [[0] for _ in range(N - K + 1)]
    
    for i in range(1, K + 1):
        xi = x[i-1]
        max_v = 9 * i
        curr_dp = []
        curr_dp_1d = [INF] * (max_v + 1)
        
        for idx in range(N - K + 1):
            j = i + idx
            pj = P[j-1]
            cost = abs(xi - j)
            
            for prev_v, prev_cost in enumerate(prev_dp[idx]):
                if prev_cost != INF:
                    new_cost = prev_cost + cost
                    nxt_v = prev_v + pj
                    if new_cost < curr_dp_1d[nxt_v]:
                        curr_dp_1d[nxt_v] = new_cost
                        
            curr_dp.append(curr_dp_1d[:])
            
        prev_dp = curr_dp
        
    ans = 0
    for v in range(len(prev_dp[-1]) - 1, -1, -1):
        if prev_dp[-1][v] <= T:
            ans = v
            break
            
    print(ans)

if __name__ == '__main__':
    solve()