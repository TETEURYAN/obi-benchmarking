
import sys

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    n = int(data[0])
    fita = list(map(int, data[1:1+n]))
    
    INF = 10**9
    dist = [INF] * n
    
    # Passo da esquerda para a direita
    last_zero = -INF
    for i in range(n):
        if fita[i] == 0:
            last_zero = i
        dist[i] = min(dist[i], i - last_zero)
    
    # Passo da direita para a esquerda
    last_zero = INF
    for i in range(n-1, -1, -1):
        if fita[i] == 0:
            last_zero = i
        dist[i] = min(dist[i], last_zero - i)
    
    # Colorir a fita
    for i in range(n):
        if fita[i] == 0:
            fita[i] = 0
        else:
            d = dist[i]
            if d >= 9:
                fita[i] = 9
            else:
                fita[i] = d
    
    print(' '.join(map(str, fita)))

if __name__ == "__main__":
    main()
