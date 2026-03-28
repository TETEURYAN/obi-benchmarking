import sys
sys.setrecursionlimit(200000)

def main():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    M = int(next(it))
    N = int(next(it))
    
    saldo = [0] * (N + 1)
    total_original = 0
    
    for _ in range(M):
        X = int(next(it))
        V = int(next(it))
        Y = int(next(it))
        saldo[X] -= V
        saldo[Y] += V
        total_original += V
    
    positivos = []
    negativos = []
    for i in range(1, N + 1):
        if saldo[i] > 0:
            positivos.append(saldo[i])
        elif saldo[i] < 0:
            negativos.append(-saldo[i])
    
    if len(positivos) <= 1 or len(negativos) <= 1:
        print("N")
        print(total_original)
        return
    
    print("S")
    
    positivos.sort(reverse=True)
    negativos.sort(reverse=True)
    i = j = 0
    total_minimo = 0
    
    while i < len(positivos) and j < len(negativos):
        if positivos[i] > negativos[j]:
            total_minimo += negativos[j]
            positivos[i] -= negativos[j]
            j += 1
        else:
            total_minimo += positivos[i]
            negativos[j] -= positivos[i]
            i += 1
    
    print(total_minimo)

if __name__ == "__main__":
    main()