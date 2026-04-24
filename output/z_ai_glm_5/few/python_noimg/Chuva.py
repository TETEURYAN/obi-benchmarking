import sys

# Aumentar o limite de recursão, embora não seja estritamente necessário para esta solução iterativa.
sys.setrecursionlimit(200000)

def solve():
    # Leitura rápida de toda a entrada padrão
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return

    # Usar um iterador para consumir os tokens sequencialmente
    iterator = iter(input_data)
    
    try:
        # O primeiro token é N
        n_str = next(iterator)
        n = int(n_str)
    except StopIteration:
        return

    # Leitura das alturas
    heights = []
    for _ in range(n):
        try:
            h_str = next(iterator)
            heights.append(int(h_str))
        except StopIteration:
            break
            
    # Caso trivial: se houver menos de 3 seções, é impossível acumular água (precisa de paredes laterais)
    if n < 3:
        print(0)
        return

    # Pré-cálculo do vetor max_right
    # max_right[i] armazena a altura máxima da seção i até a última seção N-1
    max_right = [0] * n
    max_right[n-1] = heights[n-1]
    
    # Preenche max_right de trás para frente
    for i in range(n-2, -1, -1):
        if heights[i] > max_right[i+1]:
            max_right[i] = heights[i]
        else:
            max_right[i] = max_right[i+1]
    
    count = 0
    max_left = heights[0]
    
    # Itera sobre as seções para calcular a profundidade da água
    # A primeira e a última seção nunca acumulam água (são as "bordas" da piscina)
    for i in range(n):
        # Atualiza a altura máxima à esquerda (incluindo a seção atual)
        if heights[i] > max_left:
            max_left = heights[i]
        
        # O nível da água é limitado pela menor das duas "paredes" máximas (esquerda e direita)
        water_level = max_left
        if max_right[i] < water_level:
            water_level = max_right[i]
        
        # A profundidade é o nível da água menos a altura do chão
        depth = water_level - heights[i]
        
        # Se a profundidade for de pelo menos 1 metro, a seção está coberta
        if depth >= 1:
            count += 1
            
    print(count)

if __name__ == '__main__':
    solve()