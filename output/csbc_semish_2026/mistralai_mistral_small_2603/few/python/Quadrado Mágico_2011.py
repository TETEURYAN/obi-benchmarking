
import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        print(0)
        return

    n = int(data[0])
    if n < 3 or n > 1000:
        print(0)
        return

    square = []
    index = 1
    for i in range(n):
        row = list(map(int, data[index:index + n]))
        square.append(row)
        index += n

    magic_sum = None
    valid = True

    for i in range(n):
        row_sum = sum(square[i])
        if magic_sum is None:
            magic_sum = row_sum
        elif row_sum != magic_sum:
            valid = False
            break

    if not valid:
        print(0)
        return

    for j in range(n):
        col_sum = 0
        for i in range(n):
            col_sum += square[i][j]
        if col_sum != magic_sum:
            valid = False
            break

    if not valid:
        print(0)
        return

    diag1 = 0
    diag2 = 0
    for i in range(n):
        diag1 += square[i][i]
        diag2 += square[i][n - 1 - i]

    if diag1 != magic_sum or diag2 != magic_sum:
        print(0)
        return

    print(magic_sum)

if __name__ == "__main__":
    main()
