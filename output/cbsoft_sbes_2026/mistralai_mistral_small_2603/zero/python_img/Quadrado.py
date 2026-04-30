
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

    sums_row = [0] * n
    sums_col = [0] * n

    for i in range(n):
        for j in range(n):
            sums_row[i] += square[i][j]
            sums_col[j] += square[i][j]

    M = max(sums_row)
    if M in sums_col:
        M = M
    else:
        M = max(sums_col)

    original = None
    new_val = None

    for i in range(n):
        for j in range(n):
            if square[i][j] > M:
                new_val = square[i][j]
                original = new_val - (new_val - M)
                break
        if new_val is not None:
            break

    for i in range(n):
        for j in range(n):
            if square[i][j] == original:
                square[i][j] = new_val
                break
        else:
            continue
        break

    sums_row = [0] * n
    sums_col = [0] * n

    for i in range(n):
        for j in range(n):
            sums_row[i] += square[i][j]
            sums_col[j] += square[i][j]

    M_correct = max(sums_row)
    if M_correct in sums_col:
        pass
    else:
        M_correct = max(sums_col)

    for i in range(n):
        for j in range(n):
            if square[i][j] != original and square[i][j] != new_val:
                if sums_row[i] == M_correct and sums_col[j] == M_correct:
                    pass
                else:
                    if sums_row[i] != M_correct:
                        original_val = square[i][j]
                        new_val_candidate = M_correct - (sums_row[i] - square[i][j])
                        if new_val_candidate != square[i][j]:
                            original = original_val
                            new_val = new_val_candidate
                            break
                    if sums_col[j] != M_correct:
                        original_val = square[i][j]
                        new_val_candidate = M_correct - (sums_col[j] - square[i][j])
                        if new_val_candidate != square[i][j]:
                            original = original_val
                            new_val = new_val_candidate
                            break
        if original is not None:
            break

    print(f"{original} {new_val}")

if __name__ == "__main__":
    main()
