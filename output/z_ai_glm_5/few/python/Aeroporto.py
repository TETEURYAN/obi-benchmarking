import sys

def solve():
    # Leitura rápida de toda a entrada
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return

    iterator = iter(input_data)
    test_case_num = 1
    results = []
    
    while True:
        try:
            # Leitura de A e V
            A = int(next(iterator))
            V = int(next(iterator))
        except StopIteration:
            break
        
        # Condição de parada
        if A == 0 and V == 0:
            break
        
        # Inicialização do vetor de tráfego
        # Índices de 1 a A. traffic[0] é inutilizado.
        traffic = [0] * (A + 1)
        
        # Processamento dos voos
        for _ in range(V):
            X = int(next(iterator))
            Y = int(next(iterator))
            traffic[X] += 1
            traffic[Y] += 1
        
        # Encontrar o valor máximo de tráfego
        max_traffic = max(traffic)
        
        # Coletar aeroportos com tráfego máximo
        # Já iteramos em ordem crescente (1 a A), então a lista estará ordenada
        busiest_airports = [str(i) for i in range(1, A + 1) if traffic[i] == max_traffic]
        
        # Formatação da saída
        results.append(f"Teste {test_case_num}")
        results.append(" ".join(busiest_airports))
        results.append("")  # Linha em branco após cada teste
        
        test_case_num += 1
    
    # Adicionar um elemento vazio final para garantir a última quebra de linha
    # O join colocará um \n entre o último "" e o penúltimo elemento,
    # resultando em uma linha em branco final correta.
    results.append("")
    
    sys.stdout.write("\n".join(results))

if __name__ == "__main__":
    solve()