
def main():
    N = input().strip()
    M = int(input().strip())
    count = 0
    for _ in range(M):
        C = input().strip()
        if len(C) != len(N):
            continue
        valid = True
        for i in range(len(N)):
            digit = N[i]
            char = C[i]
            if digit == '2':
                if char not in {'a', 'b', 'c'}:
                    valid = False
                    break
            elif digit == '3':
                if char not in {'d', 'e', 'f'}:
                    valid = False
                    break
            elif digit == '4':
                if char not in {'g', 'h', 'i'}:
                    valid = False
                    break
            elif digit == '5':
                if char not in {'j', 'k', 'l'}:
                    valid = False
                    break
            elif digit == '6':
                if char not in {'m', 'n', 'o'}:
                    valid = False
                    break
            elif digit == '7':
                if char not in {'p', 'q', 'r', 's'}:
                    valid = False
                    break
            elif digit == '8':
                if char not in {'t', 'u', 'v'}:
                    valid = False
                    break
            elif digit == '9':
                if char not in {'w', 'x', 'y', 'z'}:
                    valid = False
                    break
        if valid:
            count += 1
    print(count)

if __name__ == "__main__":
    main()
