import sys

def main():
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return

    x = int(input_data[0])
    y = int(input_data[1])
    
    # O campo é um retângulo de 16m x 8m.
    # Pela análise das coordenadas de exemplo e posição do juiz em (0,0):
    # A largura é 16, centrada no juiz: X varia de -8 a 8.
    # O comprimento é 8, partindo do juiz para frente: Y varia de 0 a 8.
    # Bolas na linha são consideradas dentro (inclusive).
    
    if -8 <= x <= 8 and 0 <= y <= 8:
        print('S')
    else:
        print('N')

if __name__ == '__main__':
    main()