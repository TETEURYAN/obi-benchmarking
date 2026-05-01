import sys

def main():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    N = int(data[0])
    M = int(data[1])
    P = int(data[2])

    # At the beginning, student number = (row-1)*M + col
    # We track permutations of rows and columns
    row_map = list(range(1, N+1))
    col_map = list(range(1, M+1))

    idx = 3
    for _ in range(P):
        cmd = data[idx].decode()
        a = int(data[idx+1])
        b = int(data[idx+2])
        idx += 3
        if cmd == 'L':
            row_map[a-1], row_map[b-1] = row_map[b-1], row_map[a-1]
        elif cmd == 'C':
            col_map[a-1], col_map[b-1] = col_map[b-1], col_map[a-1]

    output_lines = []
    for i in range(N):
        row = row_map[i]
        line = []
        for j in range(M):
            col = col_map[j]
            student = (row-1)*M + col
            line.append(str(student))
        output_lines.append(' '.join(line))

    sys.stdout.write('\n'.join(output_lines))

if __name__ == "__main__":
    main()