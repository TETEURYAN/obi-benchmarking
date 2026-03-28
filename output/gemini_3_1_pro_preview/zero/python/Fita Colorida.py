import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    N = int(input_data[0])
    fita = list(map(int, input_data[1:N+1]))
    
    dist = [float('inf')] * N
    
    last_zero = float('-inf')
    for i in range(N):
        if fita[i] == 0:
            last_zero = i
        if last_zero != float('-inf'):
            dist[i] = i - last_zero
            
    last_zero = float('inf')
    for i in range(N - 1, -1, -1):
        if fita[i] == 0:
            last_zero = i
        if last_zero != float('inf'):
            dist[i] = min(dist[i], last_zero - i)
            
    for i in range(N):
        if dist[i] >= 9:
            dist[i] = 9
            
    print(*(dist))

if __name__ == '__main__':
    solve()