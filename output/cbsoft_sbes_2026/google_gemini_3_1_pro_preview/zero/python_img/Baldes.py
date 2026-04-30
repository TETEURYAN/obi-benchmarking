
import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    N = int(input_data[0])
    M = int(input_data[1])
    
    initial_weights = [int(x) for x in input_data[2:N+2]]
    
    N_pow = 1
    while N_pow < N:
        N_pow *= 2
        
    INF = 10**15
    MAX = [-INF] * (2 * N_pow)
    MIN = [INF] * (2 * N_pow)
    DIFF = [-INF] * (2 * N_pow)
    
    for i in range(N):
        MAX[N_pow + i] = initial_weights[i]
        MIN[N_pow + i] = initial_weights[i]
        
    for i in range(N_pow - 1, 0, -1):
        MAX[i] = max(MAX[2*i], MAX[2*i+1])
        MIN[i] = min(MIN[2*i], MIN[2*i+1])
        DIFF[i] = max(
            DIFF[2*i],
            DIFF[2*i+1],
            MAX[2*i] - MIN[2*i+1],
            MAX[2*i+1] - MIN[2*i]
        )
        
    out = []
    idx = N + 2
    for _ in range(M):
        op = int(input_data[idx])
        if op == 1:
            p = int(input_data[idx+1])
            i = int(input_data[idx+2])
            
            pos = N_pow + i - 1
            MAX[pos] = max(MAX[pos], p)
            MIN[pos] = min(MIN[pos], p)
            pos //= 2
            while pos > 0:
                MAX[pos] = max(MAX[2*pos], MAX[2*pos+1])
                MIN[pos] = min(MIN[2*pos], MIN[2*pos+1])
                DIFF[pos] = max(
                    DIFF[2*pos],
                    DIFF[2*pos+1],
                    MAX[2*pos] - MIN[2*pos+1],
                    MAX[2*pos+1] - MIN[2*pos]
                )
                pos //= 2
            idx += 3
        else:
            a = int(input_data[idx+1])
            b = int(input_data[idx+2])
            
            ql = N_pow + a - 1
            qr = N_pow + b - 1
            
            res_max = -INF
            res_min = INF
            res_diff = -INF
            
            while ql <= qr:
                if ql % 2 == 1:
                    res_diff = max(res_diff, DIFF[ql], res_max - MIN[ql], MAX[ql] - res_min)
                    res_max = max(res_max, MAX[ql])
                    res_min = min(res_min, MIN[ql])
                    ql += 1
                if qr % 2 == 0:
                    res_diff = max(res_diff, DIFF[qr], res_max - MIN[qr], MAX[qr] - res_min)
                    res_max = max(res_max, MAX[qr])
                    res_min = min(res_min, MIN[qr])
                    qr -= 1
                ql //= 2
                qr //= 2
                
            out.append(str(res_diff))
            idx += 3
            
    print('\n'.join(out))

if __name__ == '__main__':
    solve()
