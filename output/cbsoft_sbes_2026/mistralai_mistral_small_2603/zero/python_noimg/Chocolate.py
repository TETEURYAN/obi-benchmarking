
def main():
    n = int(input())
    divisores = list(map(int, input().split()))
    estoque = 0
    for d in divisores:
        estoque += d - 1
    print(estoque)

if __name__ == "__main__":
    main()
