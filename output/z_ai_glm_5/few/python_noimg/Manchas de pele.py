import sys
from collections import deque

# Definindo o limite de recursão conforme diretrizes, embora utilizemos BFS iterativo.
sys.setrecursionlimit(200000)

def solve():
    # Leitura rápida de toda a entrada
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return

    # Parse de N e M
    iterator = iter(input_data)
    try:
        n = int(next(iterator))
        m = int(next(iterator))
    except StopIteration:
        return

    # Leitura da grade. Usamos uma lista plana para melhor performance de cache e índices.
    # O tamanho total é N * M.
    total_pixels = n * m
    grid = []
    
    # Lendo os valores P. Podemos ler todos de uma vez.
    # O input_data contém N, M e depois os valores.
    # Uma abordagem mais limpa é fatiar a lista input_data.
    # input_data[0] = N, input_data[1] = M, o resto são os pixels.
    
    # Reiniciando a leitura dos pixels a partir do índice 2
    # Convertendo para inteiros
    # Verificamos se o tamanho corresponde, mas confiamos no input formatado.
    raw_values = input_data[2:]
    
    # Se por acaso houver menos valores que o esperado (caso de borda de input quebrado),
    # preenchemos com 0 para evitar crash, embora o problema garanta o formato.
    while len(raw_values) < total_pixels:
        raw_values.append('0')
        
    grid = list(map(int, raw_values[:total_pixels]))

    count = 0
    
    # Direções: cima, baixo, esquerda, direita
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    
    # Iterando sobre cada pixel
    for r in range(n):
        for c in range(m):
            idx = r * m + c
            
            # Se encontrarmos um pixel preto (1), é uma nova mancha
            if grid[idx] == 1:
                count += 1
                
                # BFS para marcar toda a mancha como visitada (setando para 0)
                # Usamos deque para performance O(1) nas pontas
                queue = deque([(r, c)])
                grid[idx] = 0 # Marca como visitado imediatamente
                
                while queue:
                    curr_r, curr_c = queue.popleft()
                    
                    # Explora vizinhos ortogonais
                    for i in range(4):
                        nr = curr_r + dr[i]
                        nc = curr_c + dc[i]
                        
                        # Verifica limites
                        if 0 <= nr < n and 0 <= nc < m:
                            n_idx = nr * m + nc
                            
                            # Se vizinho é preto, adiciona na fila e marca
                            if grid[n_idx] == 1:
                                grid[n_idx] = 0
                                queue.append((nr, nc))
                                
    print(count)

if __name__ == "__main__":
    solve()