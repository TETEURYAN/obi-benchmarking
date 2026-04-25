import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    C = int(data[0])
    A = int(data[1])

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