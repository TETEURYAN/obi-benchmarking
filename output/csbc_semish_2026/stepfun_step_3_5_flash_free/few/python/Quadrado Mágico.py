import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    
    n = int(data[0])
    matrix = []
    idx = 1
    for i in range(n):
        row = list(map(int, data[idx:idx+n]))
        matrix.append(row)
        idx += n
    
    row_sums = [sum(row) for row in matrix]
    col_sums = [0] * n
    for j in range(n):
        for i in range(n):
            col_sums[j] += matrix[i][j]
    
    magic_sum = max(row_sums)
    
    linha = None
    for i in range(n):
        if row_sums[i] != magic_sum:
            linha = i
            break
    
    coluna = None
    for j in range(n):
        if col_sums[j] != magic_sum:
            coluna = j
            break
    
    valor = magic_sum - row_sums[linha]
    
    print(valor)
    print(linha + 1)
    print(coluna + 1)

if __name__ == "__main__":
    main()