import sys

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return

    A = int(data[0])
    N = int(data[1])
    M = int(data[2])

    rows = []
    idx = 3
    for i in range(N):
        row = list(map(int, data[idx: idx + M]))
        rows.append(row)
        idx += M

    # rows são lidas da fila mais distante (N) para a mais próxima (1)
    # então rows[0] é fila N, rows[N-1] é fila 1.
    # Para verificar da fila mais próxima primeiro, vamos iterar de rows[N-1] até rows[0].
    for fila_num in range(N - 1, -1, -1):  # fila_num 0-based: fila N-1 é fila 1
        row = rows[fila_num]
        consecutive = 0
        for seat in row:
            if seat == 0:
                consecutive += 1
                if consecutive == A:
                    # fila real = N - fila_num (pois fila_num 0-based: fila N corresponde a 0)
                    print(N - fila_num)
                    return
            else:
                consecutive = 0

    print(-1)

if __name__ == "__main__":
    main()