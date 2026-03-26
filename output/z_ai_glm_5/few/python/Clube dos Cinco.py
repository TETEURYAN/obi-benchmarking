import sys

def main():
    # Leitura rápida de todos os dados de entrada
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return

    iterator = iter(input_data)
    
    try:
        N = int(next(iterator))
        A = int(next(iterator))
        B = int(next(iterator))
        C = int(next(iterator))
        D = int(next(iterator))
        E = int(next(iterator))
        F = int(next(iterator))
        G = int(next(iterator))
    except StopIteration:
        return

    # Lógica baseada no Princípio da Inclusão-Exclusão e na análise dos dados:
    # Seja x o número de pessoas que praticam 3 esportes.
    # Pessoas que praticam 3 esportes mentem, então não são contadas em D, E, F (interseções duplas relatadas),
    # mas são contadas em A, B, C (dados dos treinadores) e em G (relataram não praticar nenhum).
    # 
    # A igualdade esperada para o total de associados N é:
    # N = (A + B + C) - (D + E + F) + G - 2x
    # Derivação:
    # N = Total
    # Total = (Pessoas em pelo menos um esporte) + (Pessoas em nenhum esporte relatado)
    # Pessoas em nenhum esporte relatado = G_real + mentirosos = (G - x) + x = G
    # Pessoas em pelo menos um esporte = Soma(sets) - Soma(interseções duplas) + Interseção tripla
    # Sets: A, B, C (contam todos, incluindo os x mentirosos)
    # Interseções duplas relatadas: D, E, F (não contam os x mentirosos)
    # Interseção tripla real: x
    # Logo, |A U B U C| = A + B + C - (D + x) - (E + x) - (F + x) + x
    #                   = A + B + C - D - E - F - 2x
    # 
    # N = (A + B + C - D - E - F - 2x) + G
    # 2x = A + B + C - D - E - F + G - N
    #
    # Se o valor calculado for 0, então x=0 (ninguém faz 3 esportes).
    # Se o valor for diferente de 0 (positivo, dadas as restrições do problema), então x > 0 (alguém faz 3 esportes).

    valor = A + B + C - D - E - F + G - N
    
    if valor == 0:
        print("N")
    else:
        print("S")

if __name__ == "__main__":
    main()