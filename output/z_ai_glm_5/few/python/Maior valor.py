import sys

def main():
    # Leitura rápida de toda a entrada
    input_data = sys.stdin.read().split()
    
    # Verificação de segurança caso a entrada esteja vazia
    if not input_data:
        return

    # Extraindo os valores de N, M e S
    # A entrada possui 3 inteiros, um por linha ou separados por espaço
    n = int(input_data[0])
    m = int(input_data[1])
    s = int(input_data[2])
    
    # Iteramos de M até N (decrescente) para encontrar o maior valor imediatamente
    # range(start, stop, step) -> vai de M até N (inclusive), decrementando
    for i in range(m, n - 1, -1):
        # Calcula a soma dos dígitos de i
        # Converter para string e somar os caracteres convertidos para int é pythônico e rápido para inteiros pequenos
        soma_digitos = sum(int(d) for d in str(i))
        
        # Se a soma for igual a S, encontramos o maior I
        if soma_digitos == s:
            print(i)
            return # Encerra o programa imediatamente após encontrar

    # Se o loop terminar sem encontrar, imprimimos -1
    print(-1)

if __name__ == "__main__":
    main()