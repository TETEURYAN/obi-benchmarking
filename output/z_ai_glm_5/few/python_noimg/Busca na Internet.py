import sys

def main():
    # Lê todo o conteúdo da entrada padrão
    input_data = sys.stdin.read().split()
    
    # Se não houver dados, encerra
    if not input_data:
        return

    results = []
    
    # Processa cada token como um caso de teste t
    for token in input_data:
        t = int(token)
        
        # Lógica do problema:
        # C3 = t
        # C2 = 2 * C3 = 2t
        # C1 = 2 * C2 = 4t
        results.append(str(4 * t))
    
    # Imprime os resultados
    sys.stdout.write('\n'.join(results) + '\n')

if __name__ == "__main__":
    main()