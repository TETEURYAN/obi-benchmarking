
import sys

def main():
    F, R = map(int, sys.stdin.readline().split())
    gotas = list(map(int, sys.stdin.readline().split()))

    if R == 0:
        print(0)
        return

    max_dias = 0

    # Verifica o intervalo antes da primeira gota
    if gotas[0] > 1:
        dias = gotas[0] - 1
        max_dias = max(max_dias, dias)

    # Verifica os intervalos entre as gotas
    for i in range(1, R):
        intervalo = gotas[i] - gotas[i-1] - 1
        if intervalo > 0:
            dias = intervalo // 2
            max_dias = max(max_dias, dias)

    # Verifica o intervalo depois da última gota
    if gotas[-1] < F:
        dias = F - gotas[-1]
        max_dias = max(max_dias, dias)

    print(max_dias)

if __name__ == "__main__":
    main()
