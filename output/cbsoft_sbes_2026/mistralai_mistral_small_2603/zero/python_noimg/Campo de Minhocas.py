
def main():
    import sys
    input = sys.stdin.read().split()
    ptr = 0
    N = int(input[ptr])
    ptr += 1
    M = int(input[ptr])
    ptr += 1

    max_sum = 0

    for i in range(N):
        row_sum = 0
        for j in range(M):
            val = int(input[ptr])
            ptr += 1
            row_sum += val
        if row_sum > max_sum:
            max_sum = row_sum

    for j in range(M):
        col_sum = 0
        for i in range(N):
            val = int(input[ptr - N * M + i * M + j])
            col_sum += val
        if col_sum > max_sum:
            max_sum = col_sum

    print(max_sum)

if __name__ == "__main__":
    main()
