import sys

def main():
    # Leitura rápida de todos os dados de entrada
    input_data = sys.stdin.read().split()
    
    # Verificação de segurança caso a entrada esteja vazia
    if not input_data:
        return

    # Parse dos inteiros: IA, IB, FA, FB
    # A entrada contém quatro inteiros conforme descrito
    IA = int(input_data[0])
    IB = int(input_data[1])
    FA = int(input_data[2])
    FB = int(input_data[3])

    # Calcula a diferença (XOR) entre o estado inicial e final para cada lâmpada
    # delta_a = 1 se A precisa mudar, 0 caso contrário
    # delta_b = 1 se B precisa mudar, 0 caso contrário
    delta_a = IA ^ FA
    delta_b = IB ^ FB

    # Lógica para minimizar o número de apertos:
    # Seja n1 o número de apertos em C1 (alterna A) e n2 o número de apertos em C2 (alterna A e B).
    # O estado final de A é determinado por: (n1 + n2) % 2 == delta_a
    # O estado final de B é determinado por: n2 % 2 == delta_b
    # Como queremos minimizar n1 + n2, restringimos n1 e n2 a {0, 1}.
    # Da segunda equação: n2 = delta_b.
    # Substituindo na primeira: (n1 + delta_b) % 2 = delta_a  =>  n1 = delta_a ^ delta_b.
    # O custo total é n1 + n2.
    
    res = (delta_a ^ delta_b) + delta_b
    
    print(res)

if __name__ == "__main__":
    main()