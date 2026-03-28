
import sys

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    matrix = []
    index = 1
    for i in range(n):
        row = list(map(int, data[index:index+n]))
        matrix.append(row)
        index += n

    original_sum = None
    for i in range(n):
        row_sum = sum(matrix[i])
        if original_sum is None:
            original_sum = row_sum
        elif row_sum != original_sum:
            if row_sum < original_sum:
                original = row_sum
                changed = original_sum
            else:
                original = original_sum
                changed = row_sum
            break

    for j in range(n):
        col_sum = sum(matrix[i][j] for i in range(n))
        if col_sum != original_sum:
            if col_sum < original_sum:
                original = col_sum
                changed = original_sum
            else:
                original = original_sum
            break

    for i in range(n):
        for j in range(n):
            temp = matrix[i][j]
            matrix[i][j] = original_sum
            row_ok = all(sum(row) == original_sum for row in matrix)
            col_ok = all(sum(matrix[k][j] for k in range(n)) == original_sum for j in range(n))
            if row_ok and col_ok:
                print(temp, original_sum)
                return
            matrix[i][j] = temp

if __name__ == "__main__":
    main()
