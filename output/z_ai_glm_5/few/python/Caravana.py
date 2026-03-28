import sys

def main():
    # Leitura rápida de todos os dados de entrada
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return

    # O primeiro elemento é o número de camelos (N)
    n = int(input_data[0])
    
    # Os próximos N elementos são os pesos
    # Convertemos para inteiros
    weights = list(map(int, input_data[1:n+1]))
    
    # Calculamos o peso total e o peso alvo por camelo
    total_weight = sum(weights)
    target_weight = total_weight // n
    
    # Calculamos a diferença para cada camelo
    output = []
    for w in weights:
        output.append(str(target_weight - w))
    
    # Imprimimos o resultado
    print('\n'.join(output))

if __name__ == '__main__':
    main()