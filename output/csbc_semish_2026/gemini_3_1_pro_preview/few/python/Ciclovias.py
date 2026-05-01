import sys

sys.setrecursionlimit(200000)

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    N = int(input_data[0])
    M = int(input_data[1])
    
    buckets = [[] for _ in range(2 * N + 1)]
    
    idx = 2
    for _ in range(M):
        u = int(input_data[idx])
        v = int(input_data[idx+1])
        idx += 2
        
        s = u + v
        buckets[s].append((u, v))
        buckets[s].append((v, u))
        
    max_dp = [0] * (N + 1)
    
    for s in range(2 * N, 2, -1):
        bucket = buckets[s]
        if not bucket:
            continue
            
        new_vals = [1 + max_dp[v] for u, v in bucket]
        
        for i in range(len(bucket)):
            u = bucket[i][0]
            if new_vals[i] > max_dp[u]:
                max_dp[u] = new_vals[i]
                
    ans = [str(max_dp[i] + 1) for i in range(1, N + 1)]
    print(" ".join(ans))

if __name__ == '__main__':
    solve()