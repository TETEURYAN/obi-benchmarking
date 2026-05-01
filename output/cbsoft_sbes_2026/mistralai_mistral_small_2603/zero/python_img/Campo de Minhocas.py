
def main():
    import sys
    data = sys.stdin.read().split()
    n = int(data[0])
    m = int(data[1])
    index = 2
    max_sum = 0

    for i in range(n):
        row_sum = 0
        for j in range(m):
            row_sum += int(data[index])
            index += 1
        if row_sum > max_sum:
            max_sum = row_sum

    for j in range(m):
        col_sum = 0
        for i in range(n):
            col_sum += int(data[2 + i * m + j])
        if col_sum > max_sum:
            max_sum = col_sum

    print(max_sum)

if __name__ == "__main__":
    main()
