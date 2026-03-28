import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    nums = list(map(int, data))
    test_cases = []
    for n in nums:
        if n == -1:
            break
        test_cases.append(n)
    for i, n in enumerate(test_cases, start=1):
        pieces = (2 ** n + 1) ** 2
        print(f"Teste {i}")
        print(pieces)
        print()

if __name__ == "__main__":
    main()