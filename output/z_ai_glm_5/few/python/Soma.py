import sys

def main():
    # Leitura rápida de toda a entrada
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return

    # Cria um iterador para processar os tokens sequencialmente
    iterator = iter(input_data)
    
    try:
        n = int(next(iterator))
        k = int(next(iterator))
    except StopIteration:
        return

    # Dicionário para armazenar a frequência das somas de prefixo
    # Inicializa com {0: 1} representando a soma do prefixo vazio
    prefix_counts = {0: 1}
    current_sum = 0
    total_rectangles = 0

    # Processa os N números
    for _ in range(n):
        try:
            x = int(next(iterator))
        except StopIteration:
            break
        
        current_sum += x
        
        # Verifica quantas vezes a soma (current_sum - k) já apareceu
        target = current_sum - k
        if target in prefix_counts:
            total_rectangles += prefix_counts[target]
        
        # Atualiza a contagem da soma de prefixo atual
        # Usar get é seguro e conciso
        prefix_counts[current_sum] = prefix_counts.get(current_sum, 0) + 1

    print(total_rectangles)

if __name__ == "__main__":
    main()