import sys

def main():
    # Leitura rápida de toda a entrada
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return

    # Iterador para processar os dados sequencialmente
    iterator = iter(input_data)
    
    try:
        # Leitura de N e M
        n = int(next(iterator))
        m = int(next(iterator))
    except StopIteration:
        return

    # Vetor para armazenar a soma dos valores de cada coluna
    col_sums = [0] * m

    # Processamento das N linhas, cada uma com M inteiros
    # Complexidade: O(N*M)
    for _ in range(n):
        for j in range(m):
            val = int(next(iterator))
            col_sums[j] += val
            
    # O problema se resume a encontrar a coluna com menor soma total.
    # Podemos escolher a rua adjacente a essa coluna e expandir para ela.
    # Como M >= 2, toda coluna possui pelo menos uma rua adjacente.
    print(min(col_sums))

if __name__ == '__main__':
    main()