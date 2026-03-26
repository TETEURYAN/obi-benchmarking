import sys

# Aumentar o limite de recursão, embora a solução seja iterativa
sys.setrecursionlimit(200000)

def solve():
    # Leitura rápida de toda a entrada
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return

    # Iterador para processar os tokens sequencialmente
    iterator = iter(input_data)
    
    test_case_num = 1
    output_buffer = []
    
    while True:
        try:
            # Leitura de X, Y e N
            X = int(next(iterator))
            Y = int(next(iterator))
            N = int(next(iterator))
        except StopIteration:
            break
            
        # Condição de parada: X=Y=N=0
        if X == 0 and Y == 0 and N == 0:
            break
            
        # Leitura dos N valores da arca
        chest_items = []
        for _ in range(N):
            chest_items.append(int(next(iterator)))
            
        sum_chest = sum(chest_items)
        total_wealth = X + Y + sum_chest
        
        # Se a riqueza total for ímpar, é impossível dividir igualmente
        if total_wealth % 2 != 0:
            output_buffer.append(f"Teste {test_case_num}\nN\n")
            test_case_num += 1
            continue
            
        # João já tem X. Para ter metade do total (total_wealth // 2),
        # ele precisa pegar (total_wealth // 2 - X) da arca.
        target = total_wealth // 2 - X
        
        # Se o alvo for negativo (João já tem mais que a metade) ou maior que a soma da arca
        if target < 0 or target > sum_chest:
            output_buffer.append(f"Teste {test_case_num}\nN\n")
            test_case_num += 1
            continue
            
        # Problema da Soma de Subconjuntos (Subset Sum) usando Bitset
        # 'bits' é um inteiro onde o k-ésimo bit indica se a soma k é alcançável
        bits = 1
        for v in chest_items:
            bits |= bits << v
            
        # Verifica se o bit correspondente ao valor alvo está definido
        if (bits >> target) & 1:
            output_buffer.append(f"Teste {test_case_num}\nS\n")
        else:
            output_buffer.append(f"Teste {test_case_num}\nN\n")
            
        test_case_num += 1
        
    # Imprime todos os resultados de uma vez para eficiência
    sys.stdout.write("".join(output_buffer))

if __name__ == "__main__":
    solve()