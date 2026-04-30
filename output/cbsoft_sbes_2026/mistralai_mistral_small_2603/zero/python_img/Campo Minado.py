
def main():
    n = int(input().strip())
    tabuleiro = []
    for _ in range(n):
        tabuleiro.append(int(input().strip()))
    
    resultado = []
    for i in range(n):
        count = 0
        if tabuleiro[i] == 1:
            count += 1
        if i > 0 and tabuleiro[i-1] == 1:
            count += 1
        if i < n-1 and tabuleiro[i+1] == 1:
            count += 1
        resultado.append(str(count))
    
    print('\n'.join(resultado))

if __name__ == '__main__':
    main()
