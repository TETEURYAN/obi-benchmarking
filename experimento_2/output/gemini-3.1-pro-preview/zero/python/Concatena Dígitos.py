import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    N = int(input_data[0])
    Q = int(input_data[1])
    
    prefix_sum = [0] * (N + 1)
    for i in range(N):
        prefix_sum[i+1] = prefix_sum[i] + int(input_data[2+i])
        
    out = []
    idx = 2 + N
    for _ in range(Q):
        L = int(input_data[idx])
        R = int(input_data[idx+1])
        idx += 2
        
        K = R - L + 1
        S = prefix_sum[R] - prefix_sum[L-1]
        ans = 11 * (K - 1) * S
        out.append(str(ans))
        
    sys.stdout.write('\n'.join(out) + '\n')

if __name__ == '__main__':
    solve()