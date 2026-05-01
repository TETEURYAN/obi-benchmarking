import sys

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    N = int(next(it))
    M = int(next(it))
    A = set(int(next(it)) for _ in range(N))
    B_seq = [int(next(it)) for _ in range(M)]

    # Conjunto de números que já estão em B (jogadas válidas até o momento)
    valid = set()
    # Conjunto de todas as somas de dois números já em B
    sums = set()

    for i, num in enumerate(B_seq):
        # Verifica se a jogada é válida
        if num in A or num in sums:
            # Jogada válida: adiciona ao conjunto valid e atualiza sums
            # Atualiza sums com todas as somas entre num e cada elemento já em valid
            new_sums = set()
            for v in valid:
                new_sums.add(v + num)
            sums.update(new_sums)
            # Também adiciona a soma de num com ele mesmo
            sums.add(num + num)
            # Adiciona num ao conjunto de números válidos
            valid.add(num)
        else:
            # Primeira jogada inválida
            print(num)
            return

    # Se todas as jogadas foram válidas
    print("sim")

if __name__ == "__main__":
    main()