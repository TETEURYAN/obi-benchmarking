import sys

# Aumentar o limite de recursão é uma boa prática em problemas de OBI/ICPC
sys.setrecursionlimit(200000)

def solve():
    # Leitura rápida de toda a entrada
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return

    # O primeiro inteiro é N, o número de salas
    n = int(input_data[0])
    
    # Os próximos N inteiros são os valores das salas
    # Convertemos para inteiros
    values = list(map(int, input_data[1:n+1]))
    
    # Algoritmo de Kadane para encontrar a soma máxima de subarray contíguo
    # Inicializamos com o primeiro elemento
    max_so_far = values[0]
    current_max = values[0]
    
    # Iteramos do segundo elemento até o fim
    for i in range(1, n):
        val = values[i]
        # current_max armazena a soma máxima do subarray que termina na posição i
        # Decidimos se estendemos o subarray anterior ou começamos um novo em i
        current_max = max(val, current_max + val)
        
        # Atualizamos a soma máxima global encontrada até agora
        max_so_far = max(max_so_far, current_max)
        
    # Imprimimos o resultado
    print(max_so_far)

if __name__ == '__main__':
    solve()