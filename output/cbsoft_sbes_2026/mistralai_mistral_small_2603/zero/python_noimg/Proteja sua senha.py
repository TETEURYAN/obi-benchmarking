
import sys

def solve():
    test_num = 1
    while True:
        line = sys.stdin.readline()
        if not line:
            break
        N = int(line.strip())
        if N == 0:
            break

        associations = []
        for _ in range(N):
            parts = sys.stdin.readline().strip().split()
            digits = parts[:10]
            letters = parts[10:16]
            associations.append((digits, letters))

        password = [''] * 6
        for pos in range(6):
            possible_digits = []
            for digits, letters in associations:
                letter = letters[pos]
                start = ord(letter) - ord('A')
                d1 = digits[start*2]
                d2 = digits[start*2 + 1]
                possible_digits.append((d1, d2))

            for d1, d2 in possible_digits:
                if d1 == d2:
                    password[pos] = d1
                    break
            else:
                for d1, d2 in possible_digits:
                    if d1 != d2:
                        if all((d1 in (p1, p2)) for p1, p2 in possible_digits):
                            password[pos] = d1
                            break
                        elif all((d2 in (p1, p2)) for p1, p2 in possible_digits):
                            password[pos] = d2
                            break

        print(f"Teste {test_num}")
        print(' '.join(password))
        print()
        test_num += 1

solve()
