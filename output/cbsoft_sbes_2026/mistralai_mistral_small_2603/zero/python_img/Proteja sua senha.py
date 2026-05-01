
def main():
    import sys
    data = sys.stdin.read().split()
    idx = 0
    test_num = 1
    while True:
        if idx >= len(data):
            break
        N = int(data[idx])
        idx += 1
        if N == 0:
            break
        associations = []
        for _ in range(N):
            digits = list(map(int, data[idx:idx+10]))
            idx += 10
            letters = data[idx:idx+6]
            idx += 6
            associations.append((digits, letters))
        password_digits = [None] * 6
        for pos in range(6):
            possible_digits = []
            for digits, letters in associations:
                letter = letters[pos]
                letter_index = ord(letter) - ord('A')
                start = letter_index * 2
                d1 = digits[start]
                d2 = digits[start + 1]
                possible_digits.append((d1, d2))
            for d in possible_digits[0]:
                all_match = True
                for pair in possible_digits[1:]:
                    if d not in pair:
                        all_match = False
                        break
                if all_match:
                    password_digits[pos] = d
                    break
        print(f"Teste {test_num}")
        print(' '.join(map(str, password_digits)))
        print()
        test_num += 1

if __name__ == "__main__":
    main()
