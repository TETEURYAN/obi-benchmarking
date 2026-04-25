import sys

def solve():
    # Leitura rápida da entrada
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    
    # A lógica do problema se resume à contagem de pontos em uma grade.
    # Inicialmente (passo 0), temos um quadrado 2x2 (2 pontos por lado).
    # A cada passo, subdividimos os quadrados.
    # Após N passos, a resolução da grade é 2^N + 1 pontos por lado.
    # O número total de pontos únicos é (2^N + 1)^2.
    
    side_points = (1 << n) + 1
    total_points = side_points * side_points
    
    print(total_points)

if __name__ == '__main__':
    solve()