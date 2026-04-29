import sys

def main():
    data = list(map(int, sys.stdin.read().split()))
    if not data:
        return

    n = data[0]
    a = data[1:1+n]

    last = a[-1]
    best = None

    # Para o resultado ser divisível por 5, o último dígito após a troca
    # deve ser 0 ou 5. Logo, precisamos trocar a última posição com alguma
    # posição i que contenha 0 ou 5.
    # Entre todas as possibilidades, queremos o maior número lexicograficamente.
    # Como só mudam as posições i e n-1, devemos maximizar primeiro o dígito
    # mais à esquerda alterado, isto é, escolher o menor i possível com a[i] > last
    # e a[i] em {0,5}. Se houver empate no i, o valor em i é fixo.
    for i in range(n - 1):
        if (a[i] == 0 or a[i] == 5) and a[i] > last:
            best = i
            break

    # Se não existe troca que melhore alguma posição anterior, ainda pode ser
    # possível obter divisibilidade por 5 sem melhorar o prefixo. Nesse caso,
    # para maximizar o número, devemos escolher a posição mais à direita possível
    # com dígito 0 ou 5.
    if best is None:
        for i in range(n - 2, -1, -1):
            if a[i] == 0 or a[i] == 5:
                best = i
                break

    if best is None:
        print(-1)
        return

    a[best], a[-1] = a[-1], a[best]
    print(*a)

if __name__ == "__main__":
    main()
