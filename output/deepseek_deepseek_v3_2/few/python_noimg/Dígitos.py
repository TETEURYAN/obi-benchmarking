import sys

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    n = int(data[0])
    digits = list(map(int, data[1:1 + n]))

    # Função para tentar construir a sequência a partir de um índice inicial
    def try_start(start: int):
        # Primeiro número: dígitos[start .. end-1]
        # Precisamos determinar o comprimento do primeiro número.
        # Ele pode ter 1 dígito, 2 dígitos, etc.
        # Mas sabemos que a sequência deve conter todos os números consecutivos
        # até o último dígito.
        # Vamos tentar todos os comprimentos possíveis para o primeiro número.
        for length in range(1, n - start + 1):
            if digits[start] == 0 and length > 1:
                continue  # número não pode começar com zero se tiver mais de um dígito
            first_num = 0
            for i in range(start, start + length):
                first_num = first_num * 10 + digits[i]
            # Agora tentamos consumir a sequência a partir deste primeiro número
            cur = first_num
            pos = start + length
            while pos < n:
                cur += 1
                cur_str = str(cur)
                cur_len = len(cur_str)
                if pos + cur_len > n:
                    break
                for i in range(cur_len):
                    if digits[pos + i] != int(cur_str[i]):
                        break
                else:
                    pos += cur_len
                    continue
                break
            else:
                # Consumimos toda a sequência com sucesso
                return first_num
        return None

    # Tenta começar em cada posição possível (o primeiro número pode começar em qualquer dígito)
    # Mas queremos o menor A possível, então tentamos começar com o menor número possível.
    # No entanto, o primeiro número deve começar no índice 0.
    # Mas o problema não diz que o primeiro dígito é o primeiro dígito de A?
    # Sim, a sequência começa com os dígitos de A.
    # Portanto, A começa no índice 0.
    # Mas A pode ter comprimento variável.
    # Vamos tentar todos os comprimentos possíveis para A começando em 0.
    # E escolher o menor A que faz a sequência inteira ser válida.
    best = None
    for length in range(1, n + 1):
        if digits[0] == 0 and length > 1:
            continue
        first_num = 0
        for i in range(length):
            first_num = first_num * 10 + digits[i]
        # Verifica se a sequência inteira pode ser gerada a partir de first_num
        cur = first_num
        pos = length
        ok = True
        while pos < n:
            cur += 1
            cur_str = str(cur)
            cur_len = len(cur_str)
            if pos + cur_len > n:
                ok = False
                break
            for i in range(cur_len):
                if digits[pos + i] != int(cur_str[i]):
                    ok = False
                    break
            if not ok:
                break
            pos += cur_len
        if ok:
            if best is None or first_num < best:
                best = first_num
    print(best)

if __name__ == "__main__":
    solve()