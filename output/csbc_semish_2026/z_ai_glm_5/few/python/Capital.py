import sys

def solve():
    # Lê toda a entrada de uma vez para eficiência
    input_data = sys.stdin.read().split()
    
    # Verifica se a entrada não está vazia
    if not input_data:
        return

    # Extrai os quatro valores de área
    # As restrições garantem que temos 4 inteiros
    a1 = int(input_data[0])
    a2 = int(input_data[1])
    a3 = int(input_data[2])
    a4 = int(input_data[3])

    # Para formar o retângulo com duas divisões perpendiculares, 
    # é necessário que o produto das áreas de quinas opostas seja igual.
    # Existem 3 maneiras de parear os 4 valores em dois pares de quinas opostas.
    # Verificamos se alguma dessas configurações satisfaz a condição.
    
    # Caso 1: (a1, a2) são opostos e (a3, a4) são opostos
    if a1 * a2 == a3 * a4:
        print('S')
        return

    # Caso 2: (a1, a3) são opostos e (a2, a4) são opostos
    if a1 * a3 == a2 * a4:
        print('S')
        return

    # Caso 3: (a1, a4) são opostos e (a2, a3) são opostos
    if a1 * a4 == a2 * a3:
        print('S')
        return

    # Se nenhum caso funcionar, é impossível
    print('N')

if __name__ == '__main__':
    solve()