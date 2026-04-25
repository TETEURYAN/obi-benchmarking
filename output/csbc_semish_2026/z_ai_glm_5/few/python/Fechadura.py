import sys

def solve():
    # Lê todos os dados de entrada de uma vez para maior velocidade
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return

    # Converte os dados para inteiros
    data_iterator = iter(input_data)
    
    try:
        n = int(next(data_iterator))
        m = int(next(data_iterator))
    except StopIteration:
        return

    heights = []
    for _ in range(n):
        try:
            heights.append(int(next(data_iterator)))
        except StopIteration:
            break
            
    # O algoritmo greedy funciona da seguinte maneira:
    # Para alinhar o pino i com a altura M, somos obrigados a usar o par (i, i+1).
    # Isso porque o par (i-1, i) já foi processado e fixado.
    # Assim, propagamos a diferença do pino atual para o próximo.
    # A soma total de movimentos é a soma dos valores absolutos dessas diferenças propagadas.
    
    moves = 0
    # Calcula a diferença inicial do primeiro pino
    current_diff = heights[0] - m
    
    for i in range(n - 1):
        moves += abs(current_diff)
        
        # A diferença a ser corrigida no próximo pino é a diferença original dele
        # menos a correção que aplicamos no pino atual.
        # Se empurramos o pino atual para baixo para corrigir, empurramos o próximo junto.
        next_raw_diff = heights[i+1] - m
        current_diff = next_raw_diff - current_diff
        
    print(moves)

if __name__ == '__main__':
    solve()