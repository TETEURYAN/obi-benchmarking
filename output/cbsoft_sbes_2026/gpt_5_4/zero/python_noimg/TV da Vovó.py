import sys

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    i = 0
    teste = 1
    out = []

    while True:
        if i + 1 >= len(data):
            break
        m = data[i]
        n = data[i + 1]
        i += 2

        if m == 0 and n == 0:
            break

        mat = []
        for _ in range(m):
            row = data[i:i + n]
            i += n
            mat.append(row)

        dx = 0
        dy = 0
        while True:
            x = data[i]
            y = data[i + 1]
            i += 2
            if x == 0 and y == 0:
                break
            dx += x
            dy += y

        dx %= n
        dy %= m

        out.append(f"Teste {teste}")
        for r in range(m):
            src_r = (r + dy) % m
            row = mat[src_r]
            if dx == 0:
                out.append(" ".join(map(str, row)) + " ")
            else:
                new_row = row[-dx:] + row[:-dx]
                out.append(" ".join(map(str, new_row)) + " ")
        out.append("")
        teste += 1

    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    main()
