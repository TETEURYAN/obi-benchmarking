import sys

def preco_idade(idade: int) -> int:
    if idade <= 17:
        return 15
    elif idade <= 59:
        return 30
    else:
        return 20

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    idade1 = int(data[0])
    idade2 = int(data[1])
    total = preco_idade(idade1) + preco_idade(idade2)
    print(total)

if __name__ == "__main__":
    main()