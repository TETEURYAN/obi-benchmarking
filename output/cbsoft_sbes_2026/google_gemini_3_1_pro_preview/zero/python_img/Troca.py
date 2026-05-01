
import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    N = int(input_data[0])
    T = int(input_data[1])
    
    up = input_data[2:N+2]
    down = input_data[N+2:2*N+2]
    
    diff = [0] * (N + 2)
    
    idx = 2 * N + 2
    for _ in range(T):
        I = int(input_data[idx])
        J = int(input_data[idx+1])
        diff[I] += 1
        diff[J+1] -= 1
        idx += 2
        
    current_flips = 0
    result = []
    for i in range(1, N + 1):
        current_flips += diff[i]
        if current_flips % 2 == 0:
            result.append(up[i-1])
        else:
            result.append(down[i-1])
            
    print(" ".join(result))

if __name__ == '__main__':
    solve()
