import sys

def main():
    # Leitura rápida de todos os dados de entrada
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return

    # Parse dos valores de entrada
    # A: altura do muro
    # S: distância que sobe por dia
    # D: distância que desce por noite
    A = int(input_data[0])
    S = int(input_data[1])
    D = int(input_data[2])

    # Se a distância que ela sobe é maior ou igual à altura do muro,
    # ela chega ao topo no primeiro dia.
    if S >= A:
        print(1)
    else:
        # Caso contrário, precisamos calcular os dias.
        # O progresso líquido por dia (ciclo de 24h) é (S - D).
        # No último dia, ela chega ao topo e não escorrega.
        # Portanto, ela precisa alcançar uma altura de (A - S) antes do último dia.
        
        # Distância a ser percorrida com progresso líquido
        remaining_distance = A - S
        
        # Progresso líquido diário
        net_progress = S - D
        
        # Cálculo do número de dias para atingir 'remaining_distance'.
        # Usamos divisão inteira com teto: ceil(x / y) = (x + y - 1) // y
        # Isso nos dá o número de dias "completos" de subida/escorregamento.
        days_before_last = (remaining_distance + net_progress - 1) // net_progress
        
        # O total de dias é os dias de progresso + o dia final que atinge o topo
        total_days = days_before_last + 1
        
        print(total_days)

if __name__ == "__main__":
    main()