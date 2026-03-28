import sys

def solve():
    # Lê a entrada completa de uma vez usando sys.stdin.read()
    # splitlines() divide a string em linhas e remove o caractere de nova linha final
    input_data = sys.stdin.read().splitlines()
    
    # Verifica se há dados de entrada (caso o arquivo esteja vazio)
    if not input_data:
        return
    
    # Pega a primeira linha (a mensagem codificada)
    encoded = input_data[0]
    
    decoded = []
    i = 0
    n = len(encoded)
    
    # Itera sobre a string codificada
    while i < n:
        # Se o caractere atual for 'p', o próximo caractere é a letra original
        if encoded[i] == 'p':
            # Adiciona o caractere seguinte à decodificação
            # O problema garante que a entrada é válida, então i+1 sempre existe
            decoded.append(encoded[i+1])
            # Pula o 'p' e a letra decodificada
            i += 2
        else:
            # Se não for 'p', é um espaço (pela definição do problema)
            decoded.append(encoded[i])
            i += 1
            
    # Imprime a mensagem decodificada
    print("".join(decoded))

if __name__ == "__main__":
    solve()