
import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    N = int(input_data[0])
    S = int(input_data[1])
    
    if N == 1:
        sys.stdout.write(str(S) + '\n')
        return
        
    if N < 13:
        K = 10**5
    else:
        K = 1
        
    S0 = N * (N**2 - 1) // 2
    R0 = S - K * S0
    
    out = []
    row0 = [str(R0 + K * j) for j in range(N)]
    out.append(" ".join(row0))
    
    for i in range(1, N):
        base = K * i * N
        row = [str(base + K * j) for j in range(N)]
        out.append(" ".join(row))
        
    sys.stdout.write('\n'.join(out) + '\n')

if __name__ == '__main__':
    solve()
