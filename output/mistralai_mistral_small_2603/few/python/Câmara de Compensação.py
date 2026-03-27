
import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    idx = 0
    M = int(data[idx])
    N = int(data[idx + 1])
    idx += 2

    saldo = [0] * (N + 1)
    total = 0

    for _ in range(M):
        X = int(data[idx])
        V = int(data[idx + 1])
        Y = int(data[idx + 2])
        idx += 3
        saldo[X] -= V
        saldo[Y] += V
        total += V

    negativos = []
    positivos = []
    for i in range(1, N + 1):
        if saldo[i] < 0:
            negativos.append((i, -saldo[i]))
        elif saldo[i] > 0:
            positivos.append((i, saldo[i]))

    possible = False
    min_total = total

    if negativos and positivos:
        possible = True
        min_total = 0
        i = j = 0
        while i < len(negativos) and j < len(positivos):
            devedor, valor_dev = negativos[i]
            credor, valor_cred = positivos[j]
            transferencia = min(valor_dev, valor_cred)
            min_total += transferencia
            valor_dev -= transferencia
            valor_cred -= transferencia
            if valor_dev == 0:
                i += 1
            else:
                negativos[i] = (devedor, valor_dev)
            if valor_cred == 0:
                j += 1
            else:
                positivos[j] = (credor, valor_cred)

    print('S' if possible else 'N')
    print(min_total)

if __name__ == "__main__":
    main()
