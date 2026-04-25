import sys
from bisect import bisect_left

def main():
    # Leitura rápida de todos os dados de entrada
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return

    # Iterador para processar os dados sequencialmente
    iterator = iter(input_data)
    
    try:
        C = int(next(iterator))
        T = int(next(iterator))
    except StopIteration:
        return

    # Pré-calcula o quadrado dos raios para evitar sqrt e problemas de precisão com float.
    # Como os raios são dados em ordem crescente, a lista de quadrados também estará ordenada.
    radii_sq = []
    for _ in range(C):
        r = int(next(iterator))
        radii_sq.append(r * r)
    
    total_points = 0
    
    # Processa cada tiro
    for _ in range(T):
        x = int(next(iterator))
        y = int(next(iterator))
        
        # Calcula a distância ao quadrado do tiro até a origem (0,0)
        dist_sq = x * x + y * y
        
        # Busca binária para encontrar o primeiro círculo que contém o tiro.
        # bisect_left retorna o índice do primeiro raio^2 >= dist_sq.
        # Isso funciona porque a lista radii_sq está ordenada.
        idx = bisect_left(radii_sq, dist_sq)
        
        # O número de círculos que contêm o ponto é o total de círculos (C)
        # menos o índice do primeiro círculo que contém o ponto.
        # Se idx == C, o ponto está fora de todos os círculos (0 pontos).
        # Se idx == 0, o ponto está dentro de todos os círculos (C pontos).
        total_points += (C - idx)
        
    print(total_points)

if __name__ == '__main__':
    main()