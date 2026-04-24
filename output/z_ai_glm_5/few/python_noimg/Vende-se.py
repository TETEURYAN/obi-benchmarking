import sys

def main():
    # Leitura rápida de toda a entrada
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return

    # Iterador para processar os tokens sequencialmente
    iterator = iter(input_data)
    
    try:
        n = int(next(iterator))
        k = int(next(iterator))
    except StopIteration:
        return

    positions = []
    for _ in range(n):
        try:
            positions.append(int(next(iterator)))
        except StopIteration:
            break
            
    # Ordenar as posições para permitir a técnica de janela deslizante
    positions.sort()
    
    # Número de prédios que restarão
    remaining = n - k
    
    # Inicializar a distância mínima com um valor grande
    min_distance = float('inf')
    
    # Janela deslizante: encontrar o intervalo de tamanho 'remaining' com menor diferença
    # entre o primeiro e o último elemento
    for i in range(n - remaining + 1):
        current_distance = positions[i + remaining - 1] - positions[i]
        if current_distance < min_distance:
            min_distance = current_distance
            
    print(min_distance)

if __name__ == "__main__":
    main()