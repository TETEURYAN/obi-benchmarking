import sys

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    N = int(next(it))
    M = int(next(it))
    matrix = [[int(next(it)) for _ in range(M)] for _ in range(N)]

    last_non_zero_col = -1
    found_all_zero = False

    for i in range(N):
        row = matrix[i]
        first_non_zero = -1
        for j in range(M):
            if row[j] != 0:
                first_non_zero = j
                break

        if first_non_zero == -1:
            found_all_zero = True
            continue

        if found_all_zero:
            print("N")
            return

        if first_non_zero <= last_non_zero:
            print("N")
            return

        last_non_zero_col = first_non_zero

    print("S")

if __name__ == "__main__":
    main()