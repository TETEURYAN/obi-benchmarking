import sys

def main():
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return

    # Lê as três pontuações
    # As restrições garantem que são 3 inteiros distintos
    scores = list(map(int, input_data[:3]))
    
    # Ordena as pontuações em ordem crescente
    scores.sort()
    
    # O vice-campeão é o elemento do meio (índice 1)
    print(scores[1])

if __name__ == "__main__":
    main()