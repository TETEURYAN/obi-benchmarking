
import sys

def main():
    test_num = 1
    for line in sys.stdin:
        n = int(line.strip())
        if n == -1:
            break
        if n == 0:
            pieces = 4
        else:
            pieces = 4 + 5 * (2 ** (2 * (n - 1)))
        print(f"Teste {test_num}")
        print(pieces)
        print()
        test_num += 1

if __name__ == "__main__":
    main()
