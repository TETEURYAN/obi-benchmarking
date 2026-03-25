import sys

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    
    idx = 0
    N = int(data[idx]); idx += 1
    C = int(data[idx]); idx += 1
    M = int(data[idx]); idx += 1
    
    carimbadas = set()
    for _ in range(C):
        carimbadas.add(int(data[idx])); idx += 1
    
    compradas = set()
    for _ in range(M):
        compradas.add(int(data[idx])); idx += 1
    
    faltam = 0
    for fig in carimbadas:
        if fig not in compradas:
            faltam += 1
    
    print(faltam)

if __name__ == "__main__":
    main()