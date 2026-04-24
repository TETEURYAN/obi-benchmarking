import sys

def main():
    # Leitura rápida de toda a entrada
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return

    iterator = iter(input_data)
    
    try:
        n = int(next(iterator))
    except StopIteration:
        return

    grid = []
    zero_r, zero_c = -1, -1

    # Preenchimento da matriz e localização do zero
    for r in range(n):
        row_data = []
        for c in range(n):
            val = int(next(iterator))
            row_data.append(val)
            if val == 0:
                zero_r = r
                zero_c = c
        grid.append(row_data)

    # Determinação da soma mágica (constante)
    # Como N >= 3 e há apenas um zero, existe pelo menos uma linha completa.
    # Buscamos a primeira linha que não contém o zero para obter a soma esperada.
    target_sum = 0
    for r in range(n):
        if 0 not in grid[r]:
            target_sum = sum(grid[r])
            break
    
    # Cálculo do valor faltante
    # A soma da linha incompleta é igual a (soma_mágica - valor_faltante)
    # Logo, valor_faltante = soma_mágica - soma_linha_incompleta
    current_row_sum = sum(grid[zero_r])
    missing_value = target_sum - current_row_sum

    # Impressão formatada conforme solicitado (1-based indexing)
    print(missing_value)
    print(zero_r + 1)
    print(zero_c + 1)

if __name__ == "__main__":
    main()