import sys

def main():
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return

    # O primeiro elemento é N, o restante são os interruptores pressionados
    # input_data[0] é N
    # input_data[1:] são os números dos interruptores (1 ou 2)
    
    ops = input_data[1:]
    
    # Contagem de quantas vezes cada interruptor foi pressionado
    # Como os dados lidos são strings, contamos '1' e '2'
    count_1 = ops.count('1')
    count_2 = ops.count('2')
    
    # Lógica das lâmpadas:
    # Lâmpada A: Liga/Desliga com I1 e I2. Total de trocas = count_1 + count_2.
    # Se o número de trocas for ímpar, termina acesa (1). Se par, apagada (0).
    state_a = (count_1 + count_2) % 2
    
    # Lâmpada B: Liga/Desliga apenas com I2. Total de trocas = count_2.
    # Se o número de trocas for ímpar, termina acesa (1). Se par, apagada (0).
    state_b = count_2 % 2
    
    # Imprimir resultado conforme formato solicitado
    print(state_a)
    print(state_b)

if __name__ == "__main__":
    main()