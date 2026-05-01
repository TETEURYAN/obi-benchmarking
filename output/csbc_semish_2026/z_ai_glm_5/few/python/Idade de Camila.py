import sys

def main():
    # Lê todas as entradas de uma vez
    data = sys.stdin.read().split()
    
    # Converte para inteiros
    ages = [int(x) for x in data]
    
    # Ordena as idades
    ages.sort()
    
    # A idade de Camila é a mediana (elemento do meio)
    print(ages[1])

if __name__ == "__main__":
    main()