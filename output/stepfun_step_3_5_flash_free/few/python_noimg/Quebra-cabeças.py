import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    N = int(next(it))
    M1 = int(next(it))
    A = [int(next(it)) for _ in range(M1)]
    M2 = int(next(it))
    B = [int(next(it)) for _ in range(M2)]
    
    L = M1 + M2 - N
    if L < 0:
        L = 0
    
    INF_NEG = -10**18
    
    dp_prev = [[INF_NEG] * (M2+1) for _ in range(M2+1)]
    for j in range(M2+1):
        dp_prev[j][0] = 0
    
    for i in range(1, M1+1):
        dp_curr = [[INF_NEG] * (M2+1) for _ in range(M2+1)]
        a_val = A[i-1]
        dp_curr[0][0] = dp_prev[0][0]
        for j in range(1, M2+1):
            max_x = min(i, j)
            b_val = B[j-1]
            prod = a_val * b_val
            for x in range(0, max_x+1):
                best = dp_prev[j][x]
                v2 = dp_curr[j-1][x]
                if v2 > best:
                    best = v2
                if x > 0:
                    v3 = dp_prev[j-1][x-1] + prod
                    if v3 > best:
                        best = v3
                dp_curr[j][x] = best
        dp_prev = dp_curr
    
    ans = INF_NEG
    max_x_final = min(M1, M2)
    for x in range(L, max_x_final+1):
        if dp_prev[M2][x] > ans:
            ans = dp_prev[M2][x]
    print(ans)

if __name__ == "__main__":
    main()