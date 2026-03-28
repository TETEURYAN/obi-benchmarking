import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    
    it = iter(data)
    M = int(next(it))
    N = int(next(it))
    
    stock = [[0] * N for _ in range(M)]
    for i in range(M):
        for j in range(N):
            stock[i][j] = int(next(it))
    
    P = int(next(it))
    vendas = 0
    for _ in range(P):
        I = int(next(it)) - 1
        J = int(next(it)) - 1
        if stock[I][J] > 0:
            stock[I][J] -= 1
            vendas += 1
    
    print(vendas)

if __name__ == "__main__":
    main()