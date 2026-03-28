import sys
import collections

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    N = int(next(it)); D = int(next(it)); W = int(next(it))
    p = [int(next(it)) for _ in range(N)]
    
    P = [0] * (N + 1)
    for i in range(1, N + 1):
        P[i] = P[i - 1] + p[i - 1]
    
    M = N - D + 1
    if M <= 0:
        print(D)
        return
    
    S = [0] * M
    for i in range(M):
        S[i] = P[i + D] - P[i]
    
    def feasible(T):
        if T < D:
            return False
        ws = T - D + 1
        dq = collections.deque()
        for i in range(M):
            while dq and S[dq[-1]] <= S[i]:
                dq.pop()
            dq.append(i)
            if dq[0] < i - ws + 1:
                dq.popleft()
            if i >= ws - 1:
                L = i - ws + 1
                R = L + T - 1
                total = P[R + 1] - P[L]
                if total - S[dq[0]] <= W:
                    return True
        return False
    
    low, high = D, N
    ans = D
    while low <= high:
        mid = (low + high) // 2
        if feasible(mid):
            ans = mid
            low = mid + 1
        else:
            high = mid - 1
    print(ans)

if __name__ == "__main__":
    solve()