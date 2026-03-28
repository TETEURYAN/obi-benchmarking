import sys

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    D = int(data[0])
    A = int(data[1])
    N = int(data[2])
    
    # Número de diárias
    diarias = 31 - (N - 1)
    
    # Dia de chegada ajustado para o aumento
    if N >= 16:
        aumento = 14  # máximo de aumentos (do dia 2 ao 15)
    else:
        aumento = N - 1
    
    valor_diaria = D + aumento * A
    total = diarias * valor_diaria
    
    print(total)

if __name__ == "__main__":
    main()