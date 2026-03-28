import sys

def main():
    # Leitura rápida de toda a entrada
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return

    # Parse dos dados de entrada
    # O primeiro elemento é N
    n = int(input_data[0])
    # O segundo elemento é a posição inicial
    start_pos_char = input_data[1]
    
    # Mapeamento de caracteres para índices (0, 1, 2)
    # A -> 0, B -> 1, C -> 2
    char_to_idx = {'A': 0, 'B': 1, 'C': 2}
    idx_to_char = {0: 'A', 1: 'B', 2: 'C'}
    
    current_pos = char_to_idx[start_pos_char]
    
    # Definição dos movimentos como permutações
    # Cada lista representa o novo índice para a moeda dependendo de onde ela estava
    # Se a moeda estava em i, vai para permutation[i]
    
    # Movimento 1: Troca A e B
    # Se em A (0) -> vai para B (1)
    # Se em B (1) -> vai para A (0)
    # Se em C (2) -> fica em C (2)
    move_1 = [1, 0, 2]
    
    # Movimento 2: Troca B e C
    # Se em A (0) -> fica em A (0)
    # Se em B (1) -> vai para C (2)
    # Se em C (2) -> vai para B (1)
    move_2 = [0, 2, 1]
    
    # Movimento 3: Troca A e C
    # Se em A (0) -> vai para C (2)
    # Se em B (1) -> fica em B (1)
    # Se em C (2) -> vai para A (0)
    move_3 = [2, 1, 0]
    
    moves_map = {
        1: move_1,
        2: move_2,
        3: move_3
    }
    
    # Processar os N movimentos
    # Os movimentos começam no índice 2 do input_data
    for i in range(n):
        move_type = int(input_data[2 + i])
        permutation = moves_map[move_type]
        current_pos = permutation[current_pos]
        
    # Imprimir o resultado
    print(idx_to_char[current_pos])

if __name__ == '__main__':
    main()