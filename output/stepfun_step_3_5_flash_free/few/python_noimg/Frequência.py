import sys
import array

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    N = int(next(it)); Q = int(next(it))
    timestamp_linha = [0] * (N + 1)
    valor_linha = [0] * (N + 1)
    timestamp_coluna = [0] * (N + 1)
    valor_coluna = [0] * (N + 1)
    total_linhas_valor = [0] * 51
    total_colunas_valor = [0] * 51
    total_linhas_valor[0] = N
    total_colunas_valor[0] = N

    size = Q + 1
    bit_linhas = [array.array('i', [0]) * (size + 1) for _ in range(51)]
    bit_colunas = [array.array('i', [0]) * (size + 1) for _ in range(51)]

    def bit_update(bit, idx, delta):
        while idx <= size:
            bit[idx] += delta
            idx += idx & -idx

    def bit_query(bit, idx):
        s = 0
        while idx:
            s += bit[idx]
            idx -= idx & -idx
        return s

    bit_update(bit_linhas[0], 1, N)
    bit_update(bit_colunas[0], 1, N)

    out = []
    for op in range(1, Q + 1):
        t = int(next(it))
        if t == 1:
            X = int(next(it)); R = int(next(it))
            old_ts = timestamp_linha[X]
            old_val = valor_linha[X]
            bit_update(bit_linhas[old_val], old_ts + 1, -1)
            bit_update(bit_linhas[R], op + 1, 1)
            total_linhas_valor[old_val] -= 1
            total_linhas_valor[R] += 1
            timestamp_linha[X] = op
            valor_linha[X] = R
        elif t == 2:
            X = int(next(it)); R = int(next(it))
            old_ts = timestamp_coluna[X]
            old_val = valor_coluna[X]
            bit_update(bit_colunas[old_val], old_ts + 1, -1)
            bit_update(bit_colunas[R], op + 1, 1)
            total_colunas_valor[old_val] -= 1
            total_colunas_valor[R] += 1
            timestamp_coluna[X] = op
            valor_coluna[X] = R
        elif t == 3:
            X = int(next(it))
            T = timestamp_linha[X]
            val_linha = valor_linha[X]
            soma_count_B = 0
            count_B = [0] * 51
            for v in range(51):
                if total_colunas_valor[v]:
                    q = bit_query(bit_colunas[v], T)
                    cnt = total_colunas_valor[v] - q
                else:
                    cnt = 0
                count_B[v] = cnt
                soma_count_B += cnt
            count_A = N - soma_count_B
            best_val = -1
            best_freq = -1
            for v in range(51):
                freq = count_B[v] + (count_A if v == val_linha else 0)
                if freq > best_freq or (freq == best_freq and v > best_val):
                    best_freq = freq
                    best_val = v
            out.append(str(best_val))
        elif t == 4:
            X = int(next(it))
            T = timestamp_coluna[X]
            val_coluna = valor_coluna[X]
            L1 = [0] * 51
            total_le_T = 0
            for v in range(51):
                if total_linhas_valor[v]:
                    l1 = bit_query(bit_linhas[v], T + 1)
                else:
                    l1 = 0
                L1[v] = l1
                total_le_T += l1
            best_val = -1
            best_freq = -1
            for v in range(51):
                L2 = total_linhas_valor[v] - L1[v]
                freq = L2 + (total_le_T if v == val_coluna else 0)
                if freq > best_freq or (freq == best_freq and v > best_val):
                    best_freq = freq
                    best_val = v
            out.append(str(best_val))
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    main()