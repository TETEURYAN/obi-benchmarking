import sys

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    n = data[0]
    idx = 1

    col_sums = [0] * n
    diag1 = 0
    diag2 = 0
    target = None

    for i in range(n):
        row_sum = 0
        for j in range(n):
            x = data[idx]
            idx += 1
            row_sum += x
            col_sums[j] += x
            if i == j:
                diag1 += x
            if i + j == n - 1:
                diag2 += x
        if target is None:
            target = row_sum
        elif row_sum != target:
            print(0)
            return

    if diag1 != target or diag2 != target:
        print(0)
        return

    for s in col_sums:
        if s != target:
            print(0)
            return

    print(target)

if __name__ == "__main__":
    main()