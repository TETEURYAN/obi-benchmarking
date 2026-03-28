import sys

def solve():
    # Leitura rápida da entrada
    input_data = sys.stdin.read().split()
    
    # Verificação de entrada vazia
    if not input_data:
        return

    # Leitura dos números como strings
    sA = input_data[0]
    sB = input_data[1]

    # Igualando o número de dígitos com zeros à esquerda
    lenA = len(sA)
    lenB = len(sB)
    max_len = max(lenA, lenB)
    
    sA = sA.zfill(max_len)
    sB = sB.zfill(max_len)

    # Listas para armazenar os dígitos remanescentes
    resA_digits = []
    resB_digits = []

    # Processamento do menos significativo para o mais significativo
    for i in range(max_len - 1, -1, -1):
        da = sA[i]
        db = sB[i]

        if da < db:
            # Dígito de A é menor: eliminado de A. B mantém db.
            resB_digits.append(db)
        elif db < da:
            # Dígito de B é menor: eliminado de B. A mantém da.
            resA_digits.append(da)
        else:
            # Dígitos iguais: ambos mantêm
            resA_digits.append(da)
            resB_digits.append(db)

    # Reconstrução dos números (revertendo a ordem)
    strA = "".join(resA_digits[::-1])
    strB = "".join(resB_digits[::-1])

    # Conversão para inteiro ou -1 se vazio
    valA = int(strA) if strA else -1
    valB = int(strB) if strB else -1

    # Saída em ordem não decrescente
    if valA <= valB:
        print(valA, valB)
    else:
        print(valB, valA)

if __name__ == '__main__':
    solve()