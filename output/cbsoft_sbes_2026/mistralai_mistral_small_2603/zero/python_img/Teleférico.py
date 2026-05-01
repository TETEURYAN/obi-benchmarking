
def main():
    C = int(input())
    A = int(input())
    if A == 0:
        print(0)
        return
    if C == 1:
        print(A)
        return
    viagens = (A + C - 2) // (C - 1)
    print(viagens)

if __name__ == "__main__":
    main()
