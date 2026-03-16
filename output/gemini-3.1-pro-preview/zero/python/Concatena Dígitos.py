
import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    N = int(input_data[0])
    Q = int(input_data[1])
    
    A = [int(x) for x in input_data[2:N+2]]
    
    pref = [0] * (N + 1)
    for i in range(N):
        pref[i+1] = pref[i] + A[i]
        
    out = []
    idx = N + 2
    for _ in range(Q):
        L = int(input_data[idx])
        R = int(input_data[idx+1])
        idx += 2
        
        k = R - L + 1
        S = pref[R] - pref[L-1]
        
        ans = 11 * (k - 1) * S
        out.append(str(ans))
        
    sys.stdout.write('\n'.join(out) + '\n')

if __name__ == '__main__':
    solve()
