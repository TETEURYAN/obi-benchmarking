
def main():
    import sys
    input = sys.stdin.read().split()
    ptr = 0
    N, M = map(int, input[ptr:ptr+2])
    ptr += 2
    barra = list(map(int, input[ptr:ptr+N]))
    ptr += N
    sequencia = list(map(int, input[ptr:ptr+M]))

    freq = [0] * 10
    for i in range(M-1):
        inicio = sequencia[i] - 1
        fim = sequencia[i+1] - 1
        if inicio > fim:
            inicio, fim = fim, inicio
        for j in range(inicio, fim + 1):
            num = barra[j]
            freq[num] += 1

    print(' '.join(map(str, freq)))

if __name__ == '__main__':
    main()
