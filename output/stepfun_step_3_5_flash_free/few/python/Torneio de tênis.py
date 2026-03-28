import sys

def main():
    data = sys.stdin.read().split()
    vitorias = sum(1 for x in data if x == 'V')
    if vitorias >= 5:
        print(1)
    elif vitorias >= 3:
        print(2)
    elif vitorias >= 1:
        print(3)
    else:
        print(-1)

if __name__ == "__main__":
    main()