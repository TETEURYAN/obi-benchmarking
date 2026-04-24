import sys

def solve():
    n = int(sys.stdin.readline())
    fita = list(map(int, sys.stdin.readline().split()))
    
    dist = [float('inf')] * n
    
    ultimo_zero = -float('inf')
    for i in range(n):
        if fita[i] == 0:
            ultimo_zero = i
        dist[i] = min(dist[i], i - ultimo_zero)
        
    ultimo_zero = float('inf')
    for i in range(n - 1, -1, -1):
        if fita[i] == 0:
            ultimo_zero = i
        dist[i] = min(dist[i], ultimo_zero - i)
        
    resultado = [min(d, 9) for d in dist]
    print(*(resultado))

if __name__ == '__main__':
    solve()