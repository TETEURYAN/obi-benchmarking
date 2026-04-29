import sys

def main():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    pilha = []

    for i in range(1, n + 1):
        x = int(data[i])
        if x == 0:
            pilha.pop()
        else:
            pilha.append(x)

    print(sum(pilha))

if __name__ == "__main__":
    main()
