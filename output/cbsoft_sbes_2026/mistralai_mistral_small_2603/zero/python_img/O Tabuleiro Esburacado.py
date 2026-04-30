
def main():
    n = int(input().strip())
    movimentos = list(map(int, input().split()))

    # Coordenadas dos buracos
    buracos = [(1, 3), (2, 3), (2, 5), (5, 4)]
    # Movimentos do cavalo (dx, dy) para cada número de 1 a 8
    deslocamentos = [
        (2, 1),   # 1
        (1, 2),   # 2
        (-1, 2),  # 3
        (-2, 1),  # 4
        (-2, -1), # 5
        (-1, -2), # 6
        (1, -2),  # 7
        (2, -1)   # 8
    ]

    x, y = 4, 3
    movimentosfeitos = 0

    for m in movimentos:
        dx, dy = deslocamentos[m-1]
        novox = x + dx
        novoy = y + dy

        if (novox, novoy) in buracos:
            break

        x, y = novox, novoy
        movimentosfeitos += 1

    print(movimentosfeitos)

if __name__ == "__main__":
    main()
