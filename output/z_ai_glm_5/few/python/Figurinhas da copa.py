import sys

def solve():
    # Lê todos os dados de entrada de uma vez para garantir velocidade
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return

    # Converte a entrada para inteiros
    data = list(map(int, input_data))
    
    # Extrai N, C e M
    # N = data[0] # N não é estritamente necessário para a lógica dos conjuntos
    C = data[1]
    M = data[2]
    
    # Ponteiros para separar as listas no array de dados
    # As figurinhas carimbadas começam no índice 3
    start_carimbadas = 3
    end_carimbadas = 3 + C
    
    # As figurinhas compradas começam logo após as carimbadas
    start_compradas = end_carimbadas
    end_compradas = start_compradas + M
    
    # Cria um conjunto com as figurinhas carimbadas
    carimbadas = set(data[start_carimbadas:end_carimbadas])
    
    # Cria um conjunto com as figurinhas compradas
    # O uso de set remove duplicatas automaticamente
    compradas = set(data[start_compradas:end_compradas])
    
    # Calcula a diferença: carimbadas que não foram compradas
    faltam = carimbadas.difference(compradas)
    
    # Imprime o resultado
    print(len(faltam))

if __name__ == "__main__":
    solve()