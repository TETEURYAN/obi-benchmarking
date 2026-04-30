
def main():
    import sys
    data = sys.stdin.read().split()
    n = int(data[0])
    square = []
    index = 1
    for i in range(n):
        row = list(map(int, data[index:index+n]))
        square.append(row)
        index += n

    target = None
    is_magic = True

    for i in range(n):
        row_sum = sum(square[i])
        if target is None:
            target = row_sum
        elif row_sum != target:
            is_magic = False
            break

    if not is_magic:
        print(0)
        return

    for j in range(n):
        col_sum = 0
        for i in range(n):
            col_sum += square[i][j]
        if col_sum != target:
            is_magic = False
            break

    if not is_magic:
        print(0)
        return

    diag1 = 0
    diag2 = 0
    for i in range(n):
        diag1 += square[i][i]
        diag2 += square[i][n-1-i]

    if diag1 != target or diag2 != target:
        print(0)
    else:
        print(target)

if __name__ == "__main__":
    main()
