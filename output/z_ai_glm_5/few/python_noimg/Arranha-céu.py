import sys

# O problema consiste em atualizar valores pontuais e consultar somas de prefixo.
# Com N e Q até 10^5, uma complexidade O(log N) por operação é necessária.
# A estrutura de dados ideal para isso é a Fenwick Tree (Binary Indexed Tree).

def solve():
    # Leitura rápida de toda a entrada
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return

    iterator = iter(input_data)
    
    try:
        N = int(next(iterator))
        Q = int(next(iterator))
    except StopIteration:
        return

    # Inicialização da Fenwick Tree e array de valores atuais
    bit = [0] * (N + 1)
    arr = [0] * (N + 1)

    def update(idx, delta):
        while idx <= N:
            bit[idx] += delta
            idx += idx & -idx

    def query(idx):
        s = 0
        while idx > 0:
            s += bit[idx]
            idx -= idx & -idx
        return s

    # Leitura dos valores iniciais e construção da árvore
    for i in range(1, N + 1):
        val = int(next(iterator))
        arr[i] = val
        update(i, val)

    output_lines = []
    
    # Processamento dos eventos
    for _ in range(Q):
        op = int(next(iterator))
        if op == 0:
            # Evento de Mudança: atualizar andar K para P
            k = int(next(iterator))
            p = int(next(iterator))
            delta = p - arr[k]
            if delta != 0:
                update(k, delta)
                arr[k] = p
        else:
            # Evento Bombeiro: soma do andar 1 ao K
            k = int(next(iterator))
            output_lines.append(str(query(k)))

    sys.stdout.write('\n'.join(output_lines) + '\n')

if __name__ == '__main__':
    solve()