
import sys

def main():
    # Lê toda a entrada de uma vez para maior eficiência
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return

    iterator = iter(input_data)
    
    try:
        n_str = next(iterator)
        N = int(n_str)
    except StopIteration:
        return

    # Inicializa a matriz e os arrays de soma
    matrix = []
    row_sums = [0] * N
    col_sums = [0] * N
    
    # Lê a matriz e calcula as somas das linhas e colunas
    for i in range(N):
        row = []
        for j in range(N):
            val = int(next(iterator))
            row.append(val)
            row_sums[i] += val
            col_sums[j] += val
        matrix.append(row)

    max_weight = -1
    
    # Calcula o peso máximo
    # Peso = (Soma da Linha) + (Soma da Coluna) - 2 * Valor da Célula
    # Pois a célula (i, j) está incluída na soma da linha e na da coluna,
    # e a torre não ataca a própria posição onde está.
    for i in range(N):
        for j in range(N):
            weight = row_sums[i] + col_sums[j] - 2 * matrix[i][j]
            if weight > max_weight:
                max_weight = weight
                
    print(max_weight)

if __name__ == "__main__":
    main()
