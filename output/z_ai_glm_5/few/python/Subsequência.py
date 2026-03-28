import sys

def main():
    # Leitura rápida de toda a entrada
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return

    # Conversão de todos os valores para inteiros
    nums = list(map(int, input_data))
    
    # Extração dos tamanhos A e B
    A = nums[0]
    B = nums[1]
    
    # Extração das sequências SA e SB
    # SA inicia no índice 2 e possui tamanho A
    SA = nums[2 : 2 + A]
    # SB inicia após SA e possui tamanho B
    SB = nums[2 + A : 2 + A + B]
    
    # Algoritmo guloso para verificar subsequência
    # 'idx' mantém a posição atual em SB que estamos buscando
    idx = 0
    
    # Se B for 0, é trivialmente subsequência (restrição diz B >= 1, mas é boa prática)
    if B == 0:
        print("S")
        return

    # Itera sobre SA para encontrar os elementos de SB em ordem
    for x in SA:
        if x == SB[idx]:
            idx += 1
            # Se encontramos todos os elementos de SB, podemos parar
            if idx == B:
                break
    
    # Se idx == B, todos os elementos de SB foram encontrados em ordem
    if idx == B:
        print("S")
    else:
        print("N")

if __name__ == "__main__":
    main()