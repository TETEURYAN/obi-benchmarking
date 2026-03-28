import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    F = int(data[0])
    R = int(data[1])
    positions = list(map(int, data[2:2+R]))

    if R == 0:
        print(0)
        return

    max_day = 0

    # Verifica o intervalo entre as gotas e as extremidades
    # Antes da primeira gota
    max_day = max(max_day, positions[0] - 1)

    # Entre as gotas
    for i in range(1, R):
        gap = positions[i] - positions[i-1] - 1
        days = gap // 2
        max_day = max(max_day, days)

    # Depois da última gota
    max_day = max(max_day, F - positions[-1])

    print(max_day)

if __name__ == "__main__":
    main()