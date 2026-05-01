import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    N = int(input_data[0])
    M = int(input_data[1])
    
    bar = [0] * (N + 1)
    for i in range(N):
        bar[i+1] = int(input_data[2+i])
        
    P = [0] * M
    for i in range(M):
        P[i] = int(input_data[2+N+i])
        
    freq = [0] * (N + 2)
    
    freq[P[0]] += 1
    freq[P[0] + 1] -= 1
    
    for i in range(M - 1):
        A = P[i]
        B = P[i+1]
        if A < B:
            freq[A + 1] += 1
            freq[B + 1] -= 1
        else:
            freq[B] += 1
            freq[A] -= 1
            
    ans = [0] * 10
    current_freq = 0
    for i in range(1, N + 1):
        current_freq += freq[i]
        ans[bar[i]] += current_freq
        
    print(*(ans))

if __name__ == '__main__':
    solve()