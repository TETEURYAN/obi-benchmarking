
def main():
    import sys
    data = sys.stdin.read().split()
    if not data:
        return
    n = int(data[0])
    digits = list(map(int, data[1:n+1]))

    def is_divisible_by_5(num):
        return num % 5 == 0

    original_num = int(''.join(map(str, digits)))
    if is_divisible_by_5(original_num):
        print(-1)
        return

    best_num = -1
    best_digits = [-1]

    for i in range(n):
        for j in range(i+1, n):
            new_digits = digits[:]
            new_digits[i], new_digits[j] = new_digits[j], new_digits[i]
            new_num = int(''.join(map(str, new_digits)))
            if is_divisible_by_5(new_num):
                if new_num > best_num:
                    best_num = new_num
                    best_digits = new_digits.copy()

    if best_num == -1:
        print(-1)
    else:
        print(' '.join(map(str, best_digits)))

if __name__ == "__main__":
    main()
