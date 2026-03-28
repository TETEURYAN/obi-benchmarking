import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    L = int(next(it))
    C = int(next(it))
    A = [[int(next(it)) for _ in range(C)] for _ in range(L)]
    
    if L < 2 or C < 2:
        print(0)
        return
    
    # Construir D: L linhas, C-1 colunas
    D = [[0] * (C-1) for _ in range(L)]
    for i in range(L):
        for j in range(C-1):
            D[i][j] = A[i][j+1] - A[i][j]
    
    # Calcular L_len: para cada coluna j, comprimento da sequência não crescente a partir de i
    L_len = [[0] * (C-1) for _ in range(L)]
    for j in range(C-1):
        # Última linha
        L_len[L-1][j] = 1
        for i in range(L-2, -1, -1):
            if D[i][j] >= D[i+1][j]:
                L_len[i][j] = L_len[i+1][j] + 1
            else:
                L_len[i][j] = 1
    
    max_area = 0
    n = C - 1  # número de colunas em D
    
    for i in range(L):
        H = [L_len[i][j] for j in range(n)]
        # Calcular left
        left = [-1] * n
        stack = []
        for j in range(n):
            while stack and H[stack[-1]] >= H[j]:
                stack.pop()
            left[j] = stack[-1] if stack else -1
            stack.append(j)
        # Calcular right
        right = [n] * n
        stack = []
        for j in range(n-1, -1, -1):
            while stack and H[stack[-1]] >= H[j]:
                stack.pop()
            right[j] = stack[-1] if stack else n
            stack.append(j)
        # Calcular área para cada barra
        for j in range(n):
            if H[j] >= 2:
                area = H[j] * (right[j] - left[j])
                if area > max_area:
                    max_area = area
    
    print(max_area)

if __name__ == "__main__":
    main()