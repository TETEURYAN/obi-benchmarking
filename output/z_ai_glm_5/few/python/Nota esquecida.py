import sys

def main():
    # Leitura rápida de toda a entrada
    data = sys.stdin.read().split()
    
    if not data:
        return

    # Extraindo os valores de A e M
    # Restrições: 0 <= A <= 100, 0 <= M <= 100
    A = int(data[0])
    M = int(data[1])
    
    # Cálculo da nota esquecida B
    # Fórmula da média: M = (A + B) / 2
    # Isolando B: 2*M = A + B => B = 2*M - A
    B = 2 * M - A
    
    # Imprimindo o resultado
    print(B)

if __name__ == "__main__":
    main()