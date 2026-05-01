import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    N = int(input_data[0])
    M = int(input_data[1])
    
    bar = [int(x) for x in input_data[2:N+2]]
    seq = [int(x) for x in input_data[N+2:N+2+M]]
    
    diff = [0] * (N + 2)
    
    diff[seq[0]] += 1
    diff[seq[0] + 1] -= 1
    
    for i in range(M - 1):
        A = seq[i]
        B = seq[i+1]
        if A < B:
            L = A + 1
            R = B
        else:
            L = B
            R = A - 1
        diff[L] += 1
        diff[R + 1] -= 1
        
    freq = 0
    ans = [0] * 10
    for i in range(1, N + 1):
        freq += diff[i]
        ans[bar[i-1]] += freq
        
    print(*(ans))

if __name__ == '__main__':
    solve()