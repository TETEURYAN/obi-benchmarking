import sys
from decimal import Decimal, ROUND_HALF_UP

def main():
    # Leitura rápida de todos os dados de entrada
    input_data = sys.stdin.read().split()
    
    # Verificação de entrada vazia
    if not input_data:
        return

    # Parsing dos valores de entrada
    # C: Consumo (km/l), D: Distância (km), T: Combustível atual (l)
    C = int(input_data[0])
    D = int(input_data[1])
    T = int(input_data[2])

    # Utilizamos Decimal para garantir precisão aritmética e controle total sobre o arredondamento
    # Isso evita problemas de ponto flutuante (ex: 1.25 arredondando para 1.2 em vez de 1.3)
    c = Decimal(C)
    d = Decimal(D)
    t = Decimal(T)

    # Cálculo do combustível necessário: Distância / Consumo
    combustivel_necessario = d / c

    # Quantidade a comprar: Necessário - Atual
    comprar = combustivel_necessario - t

    # Se a quantidade for negativa (já tem combustível suficiente), deve comprar 0
    if comprar < 0:
        comprar = Decimal(0)

    # Arredondamento para 1 dígito de precisão.
    # Utilizamos ROUND_HALF_UP, que é o padrão matemático comum (arredonda 0.05 para 0.1).
    resultado = comprar.quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)

    # Impressão do resultado
    print(resultado)

if __name__ == '__main__':
    main()