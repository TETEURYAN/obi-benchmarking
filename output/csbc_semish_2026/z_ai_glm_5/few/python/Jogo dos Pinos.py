import sys

def solve():
    # Lê todas as linhas da entrada padrão
    # sys.stdin.read().split() lida com espaços em branco e quebras de linha automaticamente
    # Retorna uma lista de strings, onde cada string é uma linha do tabuleiro
    grid = sys.stdin.read().split()
    
    # O problema garante 7 linhas, mas podemos verificar se lemos algo para evitar erros
    if not grid:
        return

    count = 0
    n = 7
    
    # Itera sobre cada célula do tabuleiro
    for r in range(n):
        for c in range(n):
            # Verifica se a posição atual contém um pino (pivô potencial)
            if grid[r][c] == 'o':
                # Verifica as 4 direções: (dr, dc)
                # Cima: (-1, 0), Baixo: (1, 0), Esquerda: (0, -1), Direita: (0, 1)
                # Para um movimento ser válido:
                # 1. O vizinho imediato (alvo) deve estar dentro do tabuleiro e ser 'o'
                # 2. O vizinho do vizinho (destino) deve estar dentro do tabuleiro e ser '.'
                
                # Cima
                if r >= 2:
                    if grid[r-1][c] == 'o' and grid[r-2][c] == '.':
                        count += 1
                
                # Baixo
                if r <= 4:
                    if grid[r+1][c] == 'o' and grid[r+2][c] == '.':
                        count += 1
                
                # Esquerda
                if c >= 2:
                    if grid[r][c-1] == 'o' and grid[r][c-2] == '.':
                        count += 1
                
                # Direita
                if c <= 4:
                    if grid[r][c+1] == 'o' and grid[r][c+2] == '.':
                        count += 1
                        
    print(count)

if __name__ == "__main__":
    solve()