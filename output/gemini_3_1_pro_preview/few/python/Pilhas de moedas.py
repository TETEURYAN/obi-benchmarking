import sys
from collections import deque

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    N = int(input_data[0])
    K = int(input_data[1])
    P = [int(x) for x in input_data[2:N+2]]
    
    if len(set(P)) <= K:
        print(0)
        return
        
    P.sort()
    
    P = [0] + P
    S = [0] * (N + 1)
    for i in range(1, N + 1):
        S[i] = S[i-1] + P[i]
        
    dp = [0] * (N + 1)
    for i in range(1, N + 1):
        dp[i] = i * P[i] - S[i]
        
    for k in range(2, K + 1):
        new_dp = [0] * (N + 1)
        lines = deque()
        
        for i in range(k, N + 1):
            j = i - 1
            m = -j
            c = dp[j] + S[j]
            
            while len(lines) >= 2:
                m1, c1 = lines[-2]
                m2, c2 = lines[-1]
                m3, c3 = m, c
                if (c3 - c2) * (m1 - m2) <= (c2 - c1) * (m2 - m3):
                    lines.pop()
                else:
                    break
            lines.append((m, c))
            
            x = P[i]
            while len(lines) >= 2:
                m1, c1 = lines[0]
                m2, c2 = lines[1]
                if m1 * x + c1 >= m2 * x + c2:
                    lines.popleft()
                else:
                    break
            
            best_m, best_c = lines[0]
            val = best_m * x + best_c
            new_dp[i] = val + i * x - S[i]
            
        dp = new_dp
        
    print(dp[N])

if __name__ == '__main__':
    solve()