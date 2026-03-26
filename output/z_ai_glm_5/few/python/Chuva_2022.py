import sys

def solve():
    # Leitura rápida de todos os dados de entrada
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return

    # Extração de N e S
    # O formato de entrada garante que temos pelo menos 2 inteiros iniciais
    iterator = iter(input_data)
    n = int(next(iterator))
    s = int(next(iterator))
    
    # Otimização: Pré-alocar dicionário não é necessário em Python, mas a lógica é O(N)
    # Dicionário para armazenar a frequência das somas de prefixo
    # Inicializa com 0:1 para considerar subarrays que começam no índice 0
    prefix_counts = {0: 1}
    current_sum = 0
    count = 0
    
    # Processar as medições
    # Os valores começam a partir do terceiro elemento da lista input_data
    # Usamos o iterator para consumir os valores restantes
    try:
        for _ in range(n):
            x = int(next(iterator))
            current_sum += x
            
            # Verificamos se existe um prefixo anterior tal que current_sum - previous_sum = s
            # Ou seja, previous_sum = current_sum - s
            target = current_sum - s
            if target in prefix_counts:
                count += prefix_counts[target]
            
            # Atualizamos a contagem do prefixo atual
            if current_sum in prefix_counts:
                prefix_counts[current_sum] += 1
            else:
                prefix_counts[current_sum] = 1
    except StopIteration:
        pass

    print(count)

if __name__ == '__main__':
    solve()