import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    n = int(data[0])
    soma = 0
    pilha = []
    idx = 1
    for _ in range(n):
        x = int(data[idx])
        idx += 1
        if x == 0:
            if pilha:
                removido = pilha.pop()
                soma -= removido
        else:
            pilha.append(x)
            soma += x
    print(soma)

if __name__ == "__main__":
    main()