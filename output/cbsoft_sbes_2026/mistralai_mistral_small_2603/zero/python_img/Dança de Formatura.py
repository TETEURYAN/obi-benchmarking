
import sys

def main():
    data = sys.stdin.read().split()
    idx = 0
    N = int(data[idx])
    M = int(data[idx+1])
    P = int(data[idx+2])
    idx += 3

    # Inicializa as posições iniciais dos alunos
    # Cada aluno i está inicialmente na posição (i-1)//M + 1, (i-1)%M + 1
    # Mas vamos trabalhar com mapeamentos de linhas e colunas

    # Mapeamento de linhas: linha original -> linha atual
    line_map = list(range(1, N+1))
    # Mapeamento de colunas: coluna original -> coluna atual
    col_map = list(range(1, M+1))

    for _ in range(P):
        op = data[idx]
        a = int(data[idx+1])
        b = int(data[idx+2])
        idx += 3
        if op == 'L':
            line_map[a-1], line_map[b-1] = line_map[b-1], line_map[a-1]
        else:  # op == 'C'
            col_map[a-1], col_map[b-1] = col_map[b-1], col_map[a-1]

    # Agora, para cada posição (i,j) na matriz final, precisamos encontrar qual aluno está lá
    # O aluno na posição (i,j) final veio da posição original (line_map_inv[i], col_map_inv[j])
    # Onde line_map_inv é o inverso de line_map: dado uma linha atual, qual era a linha original

    # Construir os mapeamentos inversos
    line_map_inv = [0] * (N + 1)
    for original_line in range(1, N+1):
        current_line = line_map[original_line - 1]
        line_map_inv[current_line] = original_line

    col_map_inv = [0] * (M + 1)
    for original_col in range(1, M+1):
        current_col = col_map[original_col - 1]
        col_map_inv[current_col] = original_col

    # Agora, para cada célula (i,j) na matriz final, o aluno é:
    # aluno = (line_map_inv[i] - 1) * M + col_map_inv[j]
    # Porque a posição original era (line_map_inv[i], col_map_inv[j])

    out_lines = []
    for i in range(1, N+1):
        line = []
        for j in range(1, M+1):
            original_line = line_map_inv[i]
            original_col = col_map_inv[j]
            aluno = (original_line - 1) * M + original_col
            line.append(str(aluno))
        out_lines.append(' '.join(line))

    print('\n'.join(out_lines))

if __name__ == '__main__':
    main()
