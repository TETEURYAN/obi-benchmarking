
def main():
    n = int(input())
    pontos_dario = 0
    pontos_xerxes = 0

    for _ in range(n):
        d, x = map(int, input().split())
        if (d == 0 and (x == 1 or x == 2)) or (d == 1 and (x == 2 or x == 3)) or (d == 2 and (x == 3 or x == 4)) or (d == 3 and (x == 4 or x == 0)) or (d == 4 and (x == 0 or x == 1)):
            pontos_dario += 1
        else:
            pontos_xerxes += 1

    if pontos_dario > pontos_xerxes:
        print("dario")
    else:
        print("xerxes")

if __name__ == "__main__":
    main()
