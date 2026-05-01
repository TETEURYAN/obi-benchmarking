import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    n = int(data[0])
    arr = list(map(int, data[1:1+n]))
    soma_atual = 0
    soma_max = -10**18
    for x in arr:
        soma_atual = max(x, soma_atual + x)
        soma_max = max(soma_max, soma_atual)
    print(soma_max)

if __name__ == "__main__":
    main()