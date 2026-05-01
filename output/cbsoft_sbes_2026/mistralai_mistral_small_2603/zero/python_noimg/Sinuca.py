
def main():
    N = int(input())
    bolas = list(map(int, input().split()))

    while len(bolas) > 1:
        nova_linha = []
        for i in range(len(bolas) - 1):
            if bolas[i] == bolas[i+1]:
                nova_linha.append(1)
            else:
                nova_linha.append(-1)
        bolas = nova_linha

    if bolas[0] == 1:
        print("preta")
    else:
        print("branca")

if __name__ == "__main__":
    main()
