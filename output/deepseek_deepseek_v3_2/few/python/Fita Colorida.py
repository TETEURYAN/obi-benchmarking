import sys

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    n = int(data[0])
    fita = list(map(int, data[1:1+n]))
    
    INF = 10**9
    dist_left = [INF] * n
    dist_right = [INF] * n
    
    # da esquerda para direita
    last_zero = -INF
    for i in range(n):
        if fita[i] == 0:
            last_zero = i
        dist_left[i] = i - last_zero
    
    # da direita para esquerda
    last_zero = INF
    for i in range(n-1, -1, -1):
        if fita[i] == 0:
            last_zero = i
        dist_right[i] = last_zero - i
    
    # resultado: menor distância, limitada a 9
    res = []
    for i in range(n):
        d = min(dist_left[i], dist_right[i])
        if d > 9:
            d = 9
        res.append(str(d))
    
    print(" ".join(res))

if __name__ == "__main__":
    main()