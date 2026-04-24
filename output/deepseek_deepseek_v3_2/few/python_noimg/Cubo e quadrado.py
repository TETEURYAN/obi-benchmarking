import sys

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    A = int(data[0])
    B = int(data[1])

    # Números que são quadrados e cubos são sextas potências
    # x = k^6 para algum inteiro k
    # Encontrar k tal que k^6 está em [A, B]
    # k mínimo: ceil(A^(1/6)), k máximo: floor(B^(1/6))
    # Usar arredondamento seguro com inteiros

    # Calcular k_min: menor k com k^6 >= A
    k_min = int(round(A ** (1/6)))
    # Ajuste para garantir k_min^6 >= A
    while k_min ** 6 < A:
        k_min += 1
    while k_min > 1 and (k_min - 1) ** 6 >= A:
        k_min -= 1

    # Calcular k_max: maior k com k^6 <= B
    k_max = int(round(B ** (1/6)))
    # Ajuste para garantir k_max^6 <= B
    while k_max ** 6 > B:
        k_max -= 1
    while (k_max + 1) ** 6 <= B:
        k_max += 1

    count = max(0, k_max - k_min + 1)
    print(count)

if __name__ == "__main__":
    main()