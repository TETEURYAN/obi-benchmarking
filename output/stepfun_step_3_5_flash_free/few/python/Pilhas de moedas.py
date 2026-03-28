
import sys
from collections import deque

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    N = int(next(it))
    K = int(next(it))
    alturas = [int(next(it)) for _ in range(N)]
    
    distinct = len(set(alturas))
    if distinct <= K:
        print(0)
        return
        
    alturas.sort()
    A = [0] + alturas  # 1-indexado
    prefix_sum = [0] * (N + 1)
    for i in range(1, N + 1):
        prefix_sum[i] = prefix_sum[i - 1] + A[i]
        
    INF = 10**18
    dp = [INF] * (N + 1)
    dp[0] = 0
    
    for _ in range(1, K + 1):
        nova_dp = [INF] * (N + 1)
        val = [INF] * (N + 1)
        for j in range(N + 1):
            if dp[j] < INF:
                val[j] = dp[j] + prefix_sum[j]
        dq = deque()
        for i in range(1, N + 1):
            j = i - 1
            if val[j] < INF:
                while len(dq) >= 2:
                    j1 = dq[-2]
                    j2 = dq[-1]
                    if (val[j2] - val[j1]) * (j2 - j) <= (val[j] - val[j2]) * (j2 - j1):
                        dq.pop()
                    else:
                        break
                dq.append(j)
            while len(dq) >= 2:
                j1 = dq[0]
                j2 = dq[1]
                if val[j1] - j1 * A[i] >= val[j2] - j2 * A[i]:
                    dq.popleft()
                else:
                    break
            if dq:
                j_best = dq[0]
                nova_dp[i] = val[j_best] - j_best * A[i] + A[i] * i - prefix_sum[i]
            else:
                nova_dp[i] = INF
        dp = nova_dp
        
    print(dp[N])

if __name__ == "__main__":
    main()
