
def main():
    n = int(input().strip())
    divisores = list(map(int, input().split()))
    estoque = 0
    pedacos = 1
    for d in divisores:
        estoque += pedacos - 1
        pedacos = pedacos * (d - 1)
    estoque += pedacos - 1
    print(estoque)

if __name__ == "__main__":
    main()
