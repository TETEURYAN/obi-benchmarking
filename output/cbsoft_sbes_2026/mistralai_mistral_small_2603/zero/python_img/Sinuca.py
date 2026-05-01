
def main():
    n = int(input().strip())
    row = list(map(int, input().split()))

    while len(row) > 1:
        new_row = []
        for i in range(len(row) - 1):
            if row[i] == row[i + 1]:
                new_row.append(1)
            else:
                new_row.append(-1)
        row = new_row

    if row[0] == 1:
        print("preta")
    else:
        print("branca")

if __name__ == "__main__":
    main()
