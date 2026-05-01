import sys

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    n = int(data[0])
    digits = list(map(int, data[1:1+n]))
    
    # Encontrar posições de dígitos que podem ir para o final para tornar divisível por 5
    # Um número é divisível por 5 se terminar em 0 ou 5
    candidates = []
    for i in range(n):
        if digits[i] == 0 or digits[i] == 5:
            candidates.append(i)
    
    if not candidates:
        print(-1)
        return
    
    best = None
    
    # Para cada candidato, tentar trocar com cada posição anterior (para maximizar)
    for cand in candidates:
        for i in range(n):
            if i == cand:
                continue
            # Não podemos trocar se o dígito na posição i for igual ao na posição cand
            # (troca não muda nada) ou se trocar mantém o mesmo dígito no final
            if i == n-1 and digits[cand] == digits[i]:
                continue
            
            # Criar nova lista com a troca
            new_digits = digits[:]
            new_digits[i], new_digits[cand] = new_digits[cand], new_digits[i]
            
            # Verificar se é divisível por 5 (último dígito 0 ou 5)
            if new_digits[-1] % 5 != 0:
                continue
            
            # Comparar com o melhor encontrado
            if best is None or new_digits > best:
                best = new_digits
    
    if best is None:
        print(-1)
    else:
        print(' '.join(map(str, best)))

if __name__ == "__main__":
    main()