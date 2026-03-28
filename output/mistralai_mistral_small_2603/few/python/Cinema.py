import sys

def main():
    idades = list(map(int, sys.stdin.read().split()))
    total = 0
    for idade in idades:
        if idade <= 17:
            total += 15
        elif idade <= 59:
            total += 30
        else:
            total += 20
    print(total)

if __name__ == "__main__":
    main()