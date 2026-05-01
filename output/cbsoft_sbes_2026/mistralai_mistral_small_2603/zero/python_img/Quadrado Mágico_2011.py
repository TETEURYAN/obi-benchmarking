
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

    magic_value = sum(square[0])

    is_magic = True

    for row in square:
        if sum(row) != magic_value:
            is_magic = False
            break

    if is_magic:
        for j in range(n):
            col_sum = 0
            for i in range(n):
                col_sum += square[i][j]
            if col_sum != magic_value:
                is_magic = False
                break

    if is_magic:
        diag1 = 0
        diag2 = 0
        for i in range(n):
            diag1 += square[i][i]
            diag2 += square[i][n-1-i]
        if diag1 != magic_value or diag2 != magic_value:
            is_magic = False

    if is_magic:
        print(magic_value)
    else:
        print(0)

if __name__ == "__main__":
    main()
