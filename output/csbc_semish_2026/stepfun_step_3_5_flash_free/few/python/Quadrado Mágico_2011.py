import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    n = int(data[0])
    total_cells = n * n
    if len(data) != 1 + total_cells:
        print(0)
        return

    mat = []
    idx = 1
    for i in range(n):
        row = list(map(int, data[idx:idx+n]))
        idx += n
        mat.append(row)

    seen = set()
    for i in range(n):
        for j in range(n):
            x = mat[i][j]
            if x < 1 or x > total_cells:
                print(0)
                return
            if x in seen:
                print(0)
                return
            seen.add(x)

    if len(seen) != total_cells:
        print(0)
        return

    magic_sum = n * (total_cells + 1) // 2

    for i in range(n):
        if sum(mat[i]) != magic_sum:
            print(0)
            return

    for j in range(n):
        s = 0
        for i in range(n):
            s += mat[i][j]
        if s != magic_sum:
            print(0)
            return

    s = 0
    for i in range(n):
        s += mat[i][i]
    if s != magic_sum:
        print(0)
        return

    s = 0
    for i in range(n):
        s += mat[i][n-1-i]
    if s != magic_sum:
        print(0)
        return

    print(magic_sum)

if __name__ == "__main__":
    main()