import sys

def main():
    # Leitura rápida de todos os dados de entrada
    data = sys.stdin.read().split()
    
    if not data:
        return

    # Parse dos valores de entrada
    v = int(data[0])
    a = int(data[1])
    f = int(data[2])
    p = int(data[3])

    # Armazena as contas em uma lista
    contas = [a, f, p]
    
    # Ordena as contas em ordem crescente para pagar as mais baratas primeiro
    contas.sort()

    count = 0
    # Itera sobre as contas ordenadas
    for conta in contas:
        if v >= conta:
            v -= conta
            count += 1
        else:
            # Como está ordenado, se não pode pagar a atual, não pode pagar as próximas
            break

    # Imprime o resultado
    print(count)

if __name__ == "__main__":
    main()