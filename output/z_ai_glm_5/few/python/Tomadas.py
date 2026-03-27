import sys

def main():
    # Lê toda a entrada de uma vez para garantir eficiência
    input_data = sys.stdin.read().split()
    
    # Verifica se há dados de entrada
    if not input_data:
        return

    # Converte os valores para inteiros
    # O problema garante que haverá 4 inteiros T1, T2, T3, T4
    tomadas = list(map(int, input_data))
    
    # Lógica:
    # Começamos com 1 tomada na parede.
    # Cada régua i adiciona Ti tomadas, mas consome 1 tomada para se ligar à rede.
    # Total = 1 + (T1 - 1) + (T2 - 1) + (T3 - 1) + (T4 - 1)
    # Total = T1 + T2 + T3 + T4 - 3
    
    resultado = sum(tomadas) - 3
    
    # Imprime o resultado
    print(resultado)

if __name__ == "__main__":
    main()