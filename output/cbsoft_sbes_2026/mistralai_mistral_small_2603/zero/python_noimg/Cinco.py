
def main():
    import sys
    data = sys.stdin.read().split()
    if not data:
        return
    n = int(data[0])
    digits = list(map(int, data[1:n+1]))

    def is_divisible_by_5(d):
        return d[-1] == 0 or d[-1] == 5

    if is_divisible_by_5(digits):
        print(-1)
        return

    max_num = -1
    best_swap = None

    for i in range(n):
        for j in range(i+1, n):
            digits[i], digits[j] = digits[j], digits[i]
            if is_divisible_by_5(digits):
                current_num = int(''.join(map(str, digits)))
                if current_num > max_num:
                    max_num = current_num
                    best_swap = digits.copy()
            digits[i], digits[j] = digits[j], digits[i]

    if max_num != -1:
        print(' '.join(map(str, best_swap)))
    else:
        print(-1)

if __name__ == "__main__":
    main()
