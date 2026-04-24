import sys

def main():
    # Leitura rápida da entrada
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return

    A = int(input_data[0])
    B = int(input_data[1])

    # A sequência de cadeiras no sentido anti-horário é 1, 2, 0, 1, 2, 0...
    # O k-ésimo elemento dessa sequência (1-indexado) é dado por k % 3.
    # Ana conta A cadeiras começando da cadeira 1.
    cadeira_ana = A % 3

    # Beatriz conta B cadeiras começando da cadeira 1.
    # O destino inicial de Beatriz é B % 3.
    destino_beatriz = B % 3

    # Se o destino de Beatriz for a cadeira onde Ana está, ela move para a próxima.
    # A próxima cadeira no sentido anti-horário (0 -> 1 -> 2 -> 0) é (x + 1) % 3.
    if destino_beatriz == cadeira_ana:
        cadeira_beatriz = (destino_beatriz + 1) % 3
    else:
        cadeira_beatriz = destino_beatriz

    # Carolina senta na cadeira restante.
    # A soma das cadeiras 0 + 1 + 2 é 3. Logo, a cadeira restante é 3 - (ocupadas).
    cadeira_carolina = (3 - cadeira_ana - cadeira_beatriz) % 3

    print(cadeira_carolina)

if __name__ == "__main__":
    main()