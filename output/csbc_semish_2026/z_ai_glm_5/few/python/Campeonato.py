import sys

def main():
    # Leitura rápida de todos os dados de entrada
    data = sys.stdin.read().split()
    
    if not data:
        return

    # Desempacotamento dos valores: Cv, Ce, Cs, Fv, Fe, Fs
    # Cv, Ce, Fv, Fe são vitórias e empates
    # Cs, Fs são saldos de gols
    Cv, Ce, Cs, Fv, Fe, Fs = map(int, data)

    # Cálculo dos pontos: Vitória = 3 pontos, Empate = 1 ponto
    pontos_cormengo = 3 * Cv + Ce
    pontos_flaminthians = 3 * Fv + Fe

    # Comparação via tuplas (pontos, saldo de gols)
    # Python compara o primeiro elemento, e se for igual, compara o segundo.
    stats_cormengo = (pontos_cormengo, Cs)
    stats_flaminthians = (pontos_flaminthians, Fs)

    if stats_cormengo > stats_flaminthians:
        print('C')
    elif stats_flaminthians > stats_cormengo:
        print('F')
    else:
        print('=')

if __name__ == "__main__":
    main()