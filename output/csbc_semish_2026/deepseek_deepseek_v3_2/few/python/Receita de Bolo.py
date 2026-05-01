import sys

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    A, B, C = map(int, data)
    farinha_por_bolo = 2
    ovos_por_bolo = 3
    leite_por_bolo = 5
    max_bolos_farinha = A // farinha_por_bolo
    max_bolos_ovos = B // ovos_por_bolo
    max_bolos_leite = C // leite_por_bolo
    max_bolos = min(max_bolos_farinha, max_bolos_ovos, max_bolos_leite)
    print(max_bolos)

if __name__ == "__main__":
    main()