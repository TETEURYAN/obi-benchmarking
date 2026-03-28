import sys

def main():
    # Leitura rápida de A e B
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return

    A = int(input_data[0])
    B = int(input_data[1])
    
    count = 0
    k = 1
    
    # Um número é quadrado e cubo perfeito se e somente se é uma sexta potência (k^6).
    # O limite superior é 10^8.
    # 21^6 = 85766121
    # 22^6 = 113379904
    # Logo, o loop precisa ir apenas até k=21 no máximo.
    # Iteramos k até que k^6 exceda B.
    
    while True:
        val = k ** 6
        if val > B:
            break
        if val >= A:
            count += 1
        k += 1
            
    print(count)

if __name__ == "__main__":
    main()