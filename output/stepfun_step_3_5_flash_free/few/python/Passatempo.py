import sys
from collections import defaultdict, deque

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    L = int(next(it))
    C = int(next(it))
    
    row_vars = []
    row_sum = []
    for _ in range(L):
        vars_line = [next(it) for _ in range(C)]
        s = int(next(it))
        row_vars.append(vars_line)
        row_sum.append(s)
    
    col_sum = [int(next(it)) for _ in range(C)]
    
    row_occurrences = [dict() for _ in range(L)]
    var_rows = defaultdict(list)
    for i in range(L):
        for v in row_vars[i]:
            row_occurrences[i][v] = row_occurrences[i].get(v, 0) + 1
        for v in row_occurrences[i]:
            var_rows[v].append(i)
    
    col_occurrences = [dict() for _ in range(C)]
    var_cols = defaultdict(list)
    for j in range(C):
        for i in range(L):
            v = row_vars[i][j]
            col_occurrences[j][v] = col_occurrences[j].get(v, 0) + 1
        for v in col_occurrences[j]:
            var_cols[v].append(j)
    
    all_vars = set(var_rows.keys())
    valor = {v: None for v in all_vars}
    
    remaining_row_sum = row_sum[:]
    remaining_col_sum = col_sum[:]
    
    unknown_row_count = [len(row_occurrences[i]) for i in range(L)]
    unknown_col_count = [len(col_occurrences[j]) for j in range(C)]
    
    fila = deque()
    for i in range(L):
        if unknown_row_count[i] == 1:
            fila.append(('row', i))
    for j in range(C):
        if unknown_col_count[j] == 1:
            fila.append(('col', j))
    
    while fila:
        tipo, idx = fila.popleft()
        if tipo == 'row':
            i = idx
            if unknown_row_count[i] != 1:
                continue
            for v in row_occurrences[i]:
                if valor[v] is None:
                    var_desconhecida = v
                    break
            k = row_occurrences[i][var_desconhecida]
            valor_v = remaining_row_sum[i] // k
            valor[var_desconhecida] = valor_v
            for i2 in var_rows[var_desconhecida]:
                freq = row_occurrences[i2][var_desconhecida]
                remaining_row_sum[i2] -= freq * valor_v
                unknown_row_count[i2] -= 1
                if unknown_row_count[i2] == 1:
                    fila.append(('row', i2))
            for j in var_cols[var_desconhecida]:
                freq = col_occurrences[j][var_desconhecida]
                remaining_col_sum[j] -= freq * valor_v
                unknown_col_count[j] -= 1
                if unknown_col_count[j] == 1:
                    fila.append(('col', j))
        else:
            j = idx
            if unknown_col_count[j] != 1:
                continue
            for v in col_occurrences[j]:
                if valor[v] is None:
                    var_desconhecida = v
                    break
            k = col_occurrences[j][var_desconhecida]
            valor_v = remaining_col_sum[j] // k
            valor[var_desconhecida] = valor_v
            for i2 in var_rows[var_desconhecida]:
                freq = row_occurrences[i2][var_desconhecida]
                remaining_row_sum[i2] -= freq * valor_v
                unknown_row_count[i2] -= 1
                if unknown_row_count[i2] == 1:
                    fila.append(('row', i2))
            for j2 in var_cols[var_desconhecida]:
                freq = col_occurrences[j2][var_desconhecida]
                remaining_col_sum[j2] -= freq * valor_v
                unknown_col_count[j2] -= 1
                if unknown_col_count[j2] == 1:
                    fila.append(('col', j2))
    
    for v in sorted(valor.keys()):
        print(v, valor[v])

if __name__ == "__main__":
    main()