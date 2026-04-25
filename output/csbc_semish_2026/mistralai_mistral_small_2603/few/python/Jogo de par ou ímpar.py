import sys

def main():
    data = sys.stdin.read().split()
    P = int(data[0])
    D1 = int(data[1])
    D2 = int(data[2])
    total = D1 + D2
    if total % 2 == 0:
        winner = P
    else:
        winner = 1 - P
    print(winner)

if __name__ == "__main__":
    main()