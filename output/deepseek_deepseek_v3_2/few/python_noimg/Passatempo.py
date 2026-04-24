import sys

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    idx = 0
    L = int(data[idx]); idx += 1
    C = int(data[idx]); idx += 1
    
    # Mapeia variável para índice
    var_to_idx = {}
    idx_to_var = []
    var_count = 0
    
    # Matriz de coeficientes: cada linha é uma equação
    # Equações 0..L-1: linhas do grid
    # Equações L..L+C-1: colunas
    # Total de equações: L + C
    # Total de variáveis: no máximo L*C, mas vamos descobrir dinamicamente
    equations = []
    sums = []
    
    # Processa linhas
    for i in range(L):
        coeffs = {}
        for j in range(C):
            var = data[idx]; idx += 1
            if var not in var_to_idx:
                var_to_idx[var] = var_count
                idx_to_var.append(var)
                var_count += 1
            vid = var_to_idx[var]
            coeffs[vid] = coeffs.get(vid, 0) + 1
        s = int(data[idx]); idx += 1
        equations.append(coeffs)
        sums.append(s)
    
    # Processa colunas
    col_sums = []
    for j in range(C):
        col_sums.append(int(data[idx])); idx += 1
    
    # Agora precisamos construir as equações das colunas
    # Para isso, precisamos da matriz original de variáveis
    # Reconstruímos lendo novamente? Melhor guardar durante a primeira leitura.
    # Vamos refazer: primeiro armazenamos a matriz de variáveis.
    
    # Reset
    idx = 2  # depois de L e C
    grid_vars = []
    for i in range(L):
        row_vars = []
        for j in range(C):
            row_vars.append(data[idx]); idx += 1
        idx += 1  # pular a soma da linha
        grid_vars.append(row_vars)
    
    # Agora equações das colunas
    for j in range(C):
        coeffs = {}
        for i in range(L):
            var = grid_vars[i][j]
            vid = var_to_idx[var]
            coeffs[vid] = coeffs.get(vid, 0) + 1
        equations.append(coeffs)
        sums.append(col_sums[j])
    
    # Temos L+C equações e V variáveis
    V = var_count
    # Ordenar variáveis para output final
    sorted_vars = sorted(idx_to_var)
    # Mapear novo índice ordenado para índice original
    order_map = {var: i for i, var in enumerate(sorted_vars)}
    # Reindexar equações para a ordem alfabética
    # Mas é mais fácil resolver e depois ordenar a saída.
    
    # Inicializar valores das variáveis como None
    values = [None] * V
    # Mapear variável para seu índice original (não ordenado)
    orig_idx_of_var = {v: i for i, v in enumerate(idx_to_var)}
    
    # Fila de variáveis resolvidas
    solved = 0
    while solved < V:
        for eq_idx, coeffs in enumerate(equations):
            unknown_vars = []
            total_known = 0
            for vid, cnt in coeffs.items():
                if values[vid] is None:
                    unknown_vars.append((vid, cnt))
                else:
                    total_known += cnt * values[vid]
            if len(unknown_vars) == 1:
                vid, cnt = unknown_vars[0]
                # Resolve: cnt * x + total_known = sums[eq_idx]
                x = (sums[eq_idx] - total_known) // cnt
                values[vid] = x
                solved += 1
                # Remove esta equação para eficiência? Não necessário.
                break
        # O problema garante que sempre há uma equação com uma incógnita.
    
    # Output em ordem alfabética
    out_lines = []
    for var in sorted_vars:
        vid = orig_idx_of_var[var]
        out_lines.append(f"{var} {values[vid]}")
    sys.stdout.write("\n".join(out_lines))

if __name__ == "__main__":
    solve()