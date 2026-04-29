import sys

def main():
    nums = list(map(int, sys.stdin.read().strip().split()))
    out = []
    teste = 1

    for n in nums:
        if n == -1:
            break
        pieces = (2 ** n + 1) ** 2
        out.append(f"Teste {teste}")
        out.append(str(pieces))
        out.append("")
        teste += 1

    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    main()
