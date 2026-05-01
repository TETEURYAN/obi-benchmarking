import sys

def solve():
    # Leitura rápida de toda a entrada
    input_data = sys.stdin.read().split()
    
    # Verificação de entrada vazia (caso de borda, embora o problema garanta N >= 3)
    if not input_data:
        return

    # O primeiro valor é N, mas não precisamos dele explicitamente para a lógica
    # pois podemos simplesmente processar todos os números restantes.
    # n = int(input_data[0])
    
    # Converte as strings de energia para inteiros
    energies = list(map(int, input_data[1:]))
    
    # Encontra a energia mínima e máxima
    min_e = min(energies)
    max_e = max(energies)
    
    # A menor dissonância é dada por 2 * (max - min).
    # Isso ocorre porque, em uma ordenação ideal (ex: crescente),
    # a soma das diferenças adjacentes é (max - min) e a aresta que fecha o ciclo
    # tem peso (max - min). Qualquer outra configuração resulta em custo maior
    # ou igual a este limite inferior.
    result = 2 * (max_e - min_e)
    
    # Imprime o resultado
    print(result)

if __name__ == '__main__':
    solve()