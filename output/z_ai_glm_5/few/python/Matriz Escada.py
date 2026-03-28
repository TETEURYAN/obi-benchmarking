import sys

def solve():
    # Leitura rápida de todos os dados de entrada
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    iterator = iter(input_data)
    
    try:
        n = int(next(iterator))
        m = int(next(iterator))
    except StopIteration:
        return

    prev_pivot_col = -1
    zero_row_found = False
    
    for _ in range(n):
        current_pivot_col = -1
        
        # Processar a linha atual procurando o pivô (primeiro elemento não nulo)
        for c in range(m):
            val = int(next(iterator))
            if val != 0 and current_pivot_col == -1:
                current_pivot_col = c
        
        if current_pivot_col == -1:
            # Linha de zeros
            zero_row_found = True
        else:
            # Linha com elementos não nulos
            if zero_row_found:
                # Violação: encontrou linha não nula após uma linha de zeros
                print('N')
                return
            
            if current_pivot_col <= prev_pivot_col:
                # Violação: pivô não avançou estritamente para a direita
                print('N')
                return
            
            prev_pivot_col = current_pivot_col
            
    print('S')

if __name__ == '__main__':
    solve()