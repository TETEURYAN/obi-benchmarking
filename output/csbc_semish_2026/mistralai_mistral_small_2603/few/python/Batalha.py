import sys

def main():
    data = sys.stdin.read().split()
    A1 = int(data[0])
    D1 = int(data[1])
    A2 = int(data[2])
    D2 = int(data[3])

    player1_doesnt_faint = (D1 != A2)
    player2_doesnt_faint = (D2 != A1)

    if player1_doesnt_faint and not player2_doesnt_faint:
        print(1)
    elif player2_doesnt_faint and not player1_doesnt_faint:
        print(2)
    else:
        print(-1)

if __name__ == "__main__":
    main()