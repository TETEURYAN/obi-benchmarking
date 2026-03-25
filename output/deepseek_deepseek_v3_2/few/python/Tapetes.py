import sys

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    L, N = map(int, data)
    
    # Distribuir o comprimento L entre N tapetes
    # Queremos maximizar a soma dos quadrados dos comprimentos
    # Estratégia: dar o maior possível para (N-1) tapetes de tamanho 1
    # e o restante para o último tapete
    restante = L - (N - 1)
    # O último tapete terá lado restante, os demais lado 1
    soma_areas = (N - 1) * (1 * 1) + restante * restante
    print(soma_areas)

if __name__ == "__main__":
    main()