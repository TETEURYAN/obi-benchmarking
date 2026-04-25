import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    N = int(next(it)); K = int(next(it)); C = int(next(it))
    A = [int(next(it)) for _ in range(N)]
    
    total_sum = sum(A)
    
    M = N - C + 1
    if M <= 0:
        print(total_sum)
        return
    
    if C == 1:
        A.sort()
        min_sum = sum(A[:K])
        result = total_sum - min_sum
        print(result)
        return
    
    P = [0] * (N+1)
    for i in range(N):
        P[i+1] = P[i] + A[i]
    
    B = [0] * M
    for i in range(M):
        B[i] = P[i+C] - P[i]
    
    INF = 10**18
    
    dp0 = B[:]
    
    if K == 1:
        min_sum = min(dp0)
    else:
        dp1 = [INF] * M
        for j in range(2, K+1):
            min_so_far = INF
            start_i = (j-1) * C
            for i in range(start_i):
                dp1[i] = INF
            for i in range(start_i, M):
                val = dp0[i-C]
                if val < min_so_far:
                    min_so_far = val
                if min_so_far != INF:
                    dp1[i] = B[i] + min_so_far
                else:
                    dp1[i] = INF
            dp0, dp1 = dp1, dp0
        min_sum = min(dp0)
    
    result = total_sum - min_sum
    print(result)

if __name__ == "__main__":
    main()