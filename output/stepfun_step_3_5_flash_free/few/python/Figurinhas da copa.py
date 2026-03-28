import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    
    n = int(data[0])
    c = int(data[1])
    m = int(data[2])
    
    idx = 3
    carimbadas = list(map(int, data[idx:idx+c]))
    idx += c
    
    compradas = list(map(int, data[idx:idx+m]))
    
    set_compradas = set(compradas)
    
    faltam = 0
    for fig in carimbadas:
        if fig not in set_compradas:
            faltam += 1
    
    print(faltam)

if __name__ == "__main__":
    main()