import sys

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return

    N = int(data[0])
    F = int(data[1])
    caps = list(map(int, data[2:2 + N]))

    def total_moedas(dias):
        soma = 0
        for c in caps:
            soma += dias // c
        return soma

    low = 1
    high = 1
    # Estimar upper bound
    while total_moedas(high) < F:
        high *= 2

    while low < high:
        mid = (low + high) // 2
        if total_moedas(mid) >= F:
            high = mid
        else:
            low = mid + 1

    print(low)

if __name__ == "__main__":
    main()