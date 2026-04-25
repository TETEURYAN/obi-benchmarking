import sys

def main():
    # Leitura rápida de todos os dados de entrada
    input_data = sys.stdin.read().split()
    
    # Verificação de entrada vazia
    if not input_data:
        return

    # O primeiro elemento é N, o segundo é a string.
    # De acordo com o problema, a string está na segunda linha.
    # Como usamos split(), espaços em branco e quebras de linha são removidos.
    # O problema garante que Ci é uma letra, então a string não contém espaços.
    if len(input_data) < 2:
        return

    s = input_data[1]
    
    # Caso de string vazia (embora N >= 1 garanta o contrário, é uma boa prática verificar)
    if not s:
        print("")
        return

    # Algoritmo de Run-Length Encoding (RLE)
    # Complexidade O(N), onde N é o tamanho da string.
    
    output_parts = []
    current_char = s[0]
    count = 1
    
    # Itera sobre a string a partir do segundo caractere
    for i in range(1, len(s)):
        if s[i] == current_char:
            count += 1
        else:
            output_parts.append(str(count))
            output_parts.append(current_char)
            current_char = s[i]
            count = 1
            
    # Adiciona o último grupo de caracteres
    output_parts.append(str(count))
    output_parts.append(current_char)
    
    # Imprime o resultado no formato solicitado
    print(" ".join(output_parts))

if __name__ == "__main__":
    main()