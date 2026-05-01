
def main():
    resultados = []
    for _ in range(15):
        m, n = map(int, input().split())
        resultados.append((m, n))

    vencedores = [''] * 15
    vencedores[0] = 'A' if resultados[0][0] > resultados[0][1] else 'B'
    vencedores[1] = 'C' if resultados[1][0] > resultados[1][1] else 'D'
    vencedores[2] = 'E' if resultados[2][0] > resultados[2][1] else 'F'
    vencedores[3] = 'G' if resultados[3][0] > resultados[3][1] else 'H'
    vencedores[4] = 'I' if resultados[4][0] > resultados[4][1] else 'J'
    vencedores[5] = 'K' if resultados[5][0] > resultados[5][1] else 'L'
    vencedores[6] = 'M' if resultados[6][0] > resultados[6][1] else 'N'
    vencedores[7] = 'O' if resultados[7][0] > resultados[7][1] else 'P'

    vencedores[8] = vencedores[0] if resultados[8][0] > resultados[8][1] else vencedores[1]
    vencedores[9] = vencedores[2] if resultados[9][0] > resultados[9][1] else vencedores[3]
    vencedores[10] = vencedores[4] if resultados[10][0] > resultados[10][1] else vencedores[5]
    vencedores[11] = vencedores[6] if resultados[11][0] > resultados[11][1] else vencedores[7]

    vencedores[12] = vencedores[8] if resultados[12][0] > resultados[12][1] else vencedores[9]
    vencedores[13] = vencedores[10] if resultados[13][0] > resultados[13][1] else vencedores[11]

    campeao = vencedores[14] if resultados[14][0] > resultados[14][1] else vencedores[13]
    print(campeao)

if __name__ == '__main__':
    main()
