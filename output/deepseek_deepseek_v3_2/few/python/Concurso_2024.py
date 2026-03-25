import sys

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    N = int(next(it))
    K = int(next(it))
    notas = [int(next(it)) for _ in range(N)]
    
    notas.sort(reverse=True)
    corte = notas[K-1]
    print(corte)

if __name__ == "__main__":
    main()