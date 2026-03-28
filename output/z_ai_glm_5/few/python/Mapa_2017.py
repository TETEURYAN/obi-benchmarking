import sys

def solve():
    # Leitura rápida de toda a entrada
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return

    # Parse das dimensões L e C
    iterator = iter(input_data)
    try:
        L = int(next(iterator))
        C = int(next(iterator))
    except StopIteration:
        return

    # Leitura do grid
    grid = []
    start_r, start_c = -1, -1
    
    for r in range(L):
        try:
            row_str = next(iterator)
            grid.append(row_str)
            # Encontrar a posição inicial 'o' durante a leitura
            if 'o' in row_str:
                start_r = r
                start_c = row_str.index('o')
        except StopIteration:
            break
            
    # Caso não encontre o 'o' (improvável pelas restrições)
    if start_r == -1:
        return

    # Direções: Cima, Baixo, Esquerda, Direita
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    
    # Posição atual e anterior
    curr_r, curr_c = start_r, start_c
    prev_r, prev_c = -1, -1
    
    # Navegação pelo mapa
    while True:
        found_next = False
        next_r, next_c = -1, -1
        
        # Verificar vizinhos
        for i in range(4):
            nr = curr_r + dr[i]
            nc = curr_c + dc[i]
            
            # Verificar limites
            if 0 <= nr < L and 0 <= nc < C:
                # Não voltar para a posição anterior
                if (nr, nc) == (prev_r, prev_c):
                    continue
                
                # Se encontrou um 'H', é o próximo passo do caminho
                if grid[nr][nc] == 'H':
                    next_r, next_c = nr, nc
                    found_next = True
                    break
        
        # Se não encontrou próximo passo, chegamos ao fim do caminho
        if not found_next:
            # Imprimir resultado (1-based indexing)
            print(f"{curr_r + 1} {curr_c + 1}")
            return
        
        # Atualizar posições para a próxima iteração
        prev_r, prev_c = curr_r, curr_c
        curr_r, curr_c = next_r, next_c

if __name__ == '__main__':
    solve()