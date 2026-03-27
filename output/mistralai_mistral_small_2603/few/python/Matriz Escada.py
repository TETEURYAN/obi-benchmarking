
import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        print('N')
        return

    n = int(data[0])
    m = int(data[1])
    matrix = []
    index = 2
    for i in range(n):
        row = list(map(int, data[index:index+m]))
        matrix.append(row)
        index += m

    if n == 0 or m == 0:
        print('S')
        return

    last_non_zero_col = -1
    for i in range(n):
        row = matrix[i]
        found_non_zero = False
        current_col = -1
        for j in range(m):
            if row[j] != 0:
                found_non_zero = True
                current_col = j
                break

        if not found_non_zero:
            if last_non_zero_col != -1:
                print('N')
                return
            continue

        if current_col < last_non_zero_col:
            print('N')
            return

        last_non_zero_col = current_col

        for k in range(i+1, n):
            for l in range(current_col + 1):
                if matrix[k][l] != 0:
                    print('N')
                    return

    print('S')

if __name__ == "__main__":
    main()
