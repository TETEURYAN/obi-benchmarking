import sys

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    L = int(next(it))
    C = int(next(it))
    A = [[int(next(it)) for _ in range(C)] for _ in range(L)]

    # Transformação para B[i][j] = A[i][j] - A[i][0] - A[0][j] + A[0][0]
    B = [[0] * C for _ in range(L)]
    for i in range(L):
        for j in range(C):
            B[i][j] = A[i][j] - A[i][0] - A[0][j] + A[0][0]

    # Para uma submatriz ser super‑legal, todos os B[i][j] nela devem ser >= 0.
    # Queremos a maior submatriz (em área) onde todos os B[i][j] >= 0.
    # Isso se reduz a: para cada linha i, calcular o histograma de alturas
    # onde altura[i][j] = comprimento do segmento contínuo de B[k][j] >= 0
    # terminando na linha i.
    altura = [[0] * C for _ in range(L)]
    for j in range(C):
        seq = 0
        for i in range(L):
            if B[i][j] >= 0:
                seq += 1
            else:
                seq = 0
            altura[i][j] = seq

    ans = 0
    for i in range(L):
        stack = []
        left = [0] * C
        for j in range(C):
            while stack and altura[i][stack[-1]] >= altura[i][j]:
                stack.pop()
            left[j] = stack[-1] + 1 if stack else 0
            stack.append(j)
        stack.clear()
        right = [C - 1] * C
        for j in range(C - 1, -1, -1):
            while stack and altura[i][stack[-1]] >= altura[i][j]:
                stack.pop()
            right[j] = stack[-1] - 1 if stack else C - 1
            stack.append(j)
        for j in range(C):
            h = altura[i][j]
            if h >= 2:  # precisa ter pelo menos 2 linhas para ser super‑legal
                width = right[j] - left[j] + 1
                if width >= 2:  # precisa ter pelo menos 2 colunas
                    area = h * width
                    if area > ans:
                        ans = area
    print(ans)

if __name__ == "__main__":
    main()