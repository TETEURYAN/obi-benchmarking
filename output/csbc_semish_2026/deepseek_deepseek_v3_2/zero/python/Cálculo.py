
import sys

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    M = int(next(it))
    N = int(next(it))
    X = [int(next(it)) for _ in range(M)]
    Y = [int(next(it)) for _ in range(N)]

    # Garantir que X e Y tenham o mesmo comprimento, preenchendo com zeros à direita
    max_len = max(M, N)
    X = X + [0] * (max_len - M)
    Y = Y + [0] * (max_len - N)

    # Soma com carry, começando do dígito menos significativo (direita)
    result = []
    carry = 0
    for i in range(max_len - 1, -1, -1):
        total = X[i] + Y[i] + carry
        result.append(total % 2)
        carry = total // 2

    # Se ainda houver carry, adiciona mais um dígito
    if carry:
        result.append(carry)

    # Inverter para obter a ordem correta (mais significativo à esquerda)
    result.reverse()

    # Remover zeros à esquerda, mas garantir que o último dígito seja 1
    # (representação usa o menor número de dígitos possível, com último dígito 1)
    while len(result) > 1 and result[-1] == 0:
        result.pop()

    # Imprimir resultado
    print(' '.join(map(str, result)))

if __name__ == "__main__":
    main()
