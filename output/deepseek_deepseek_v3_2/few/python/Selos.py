import sys

def main():
    data = sys.stdin.read().strip()
    if not data:
        return
    N = int(data)
    
    if N <= 2:
        print('N')
        return
    
    # Verifica se N tem algum divisor d tal que 1 < d < N
    # e N/d também é inteiro e maior que 1.
    # Basta verificar até sqrt(N)
    i = 2
    while i * i <= N:
        if N % i == 0:
            # i é divisor, então N/i também é divisor
            # ambos são > 1 e < N (pois i >= 2 e N/i >= 2)
            print('S')
            return
        i += 1
    
    print('N')

if __name__ == "__main__":
    main()