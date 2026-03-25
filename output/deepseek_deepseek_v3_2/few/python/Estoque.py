import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    
    idx = 0
    M = int(data[idx]); idx += 1
    N = int(data[idx]); idx += 1
    
    estoque = []
    for _ in range(M):
        linha = list(map(int, data[idx:idx+N]))
        idx += N
        estoque.append(linha)
    
    P = int(data[idx]); idx += 1
    vendas = 0
    
    for _ in range(P):
        I = int(data[idx]) - 1
        J = int(data[idx+1]) - 1
        idx += 2
        if estoque[I][J] > 0:
            estoque[I][J] -= 1
            vendas += 1
    
    print(vendas)

if __name__ == "__main__":
    main()