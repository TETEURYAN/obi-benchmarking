
import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return

    test_cases = []
    idx = 0
    while idx < len(data):
        n = int(data[idx])
        idx += 1
        if n == -1:
            break
        test_cases.append(n)

    for i, n in enumerate(test_cases, 1):
        if n == 0:
            pieces = 1
        else:
            pieces = (2 ** n + 1) ** 2
        print(f"Teste {i}")
        print(pieces)
        print()

if __name__ == "__main__":
    main()
