import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    n = int(data[0])
    digits = list(map(int, data[1:1+n]))

    # Tentar encontrar o menor A possível
    # O número de dígitos em A pode variar de 1 até len(digits)
    # Precisamos encontrar a partição que forma números válidos (1 <= A <= B <= 10^1000)

    # Vamos tentar todas as possíveis quantidades de dígitos para A (de 1 até n-1)
    # Começando do menor número de dígitos para A (para garantir que A seja o menor possível)
    for num_digits_A in range(1, n):
        # Tentar formar A com os primeiros num_digits_A dígitos
        A_str = ''.join(map(str, digits[:num_digits_A]))
        A = int(A_str)

        # O restante dos dígitos formam a sequência de B
        remaining_digits = digits[num_digits_A:]
        B_str = ''.join(map(str, remaining_digits))
        B = int(B_str)

        # Verificar se A <= B e se a concatenação dos dígitos de A e B (com espaços) forma a sequência original
        # A concatenação deve ser exatamente a sequência original
        # Como já estamos usando a sequência original, a única verificação necessária é A <= B
        if A <= B:
            print(A)
            return

    # Se não encontrou nenhuma partição válida com A tendo menos dígitos que B,
    # então A deve ser o número inteiro formado por todos os dígitos (e B = A)
    A_str = ''.join(map(str, digits))
    A = int(A_str)
    print(A)

if __name__ == "__main__":
    main()