import sys

def main():
    # Leitura rápida de toda a entrada
    input_data = sys.stdin.read().split()
    
    # Verificação de segurança para entrada vazia
    if not input_data:
        return

    horizontal = input_data[0]
    vertical = input_data[1]

    # Dicionário para armazenar o maior índice (posição mais baixa) de cada letra na vertical.
    # Como iteramos da esquerda para a direita, o último valor atribuído será o maior índice.
    last_occurrence_vertical = {}
    for idx, char in enumerate(vertical):
        last_occurrence_vertical[char] = idx + 1

    # Iteramos pela palavra horizontal da direita para a esquerda.
    # Isso garante que o primeiro match encontrado satisfaça a condição primária:
    # "o cruzamento mais à direita possível".
    for i in range(len(horizontal) - 1, -1, -1):
        char = horizontal[i]
        if char in last_occurrence_vertical:
            # Encontramos a letra comum.
            # O índice vertical armazenado já é o maior possível para esta letra,
            # satisfazendo a condição secundária: "o cruzamento mais abaixo possível".
            print(f"{i + 1} {last_occurrence_vertical[char]}")
            return

    # Se o loop terminar sem encontrar letra comum
    print("-1 -1")

if __name__ == "__main__":
    main()