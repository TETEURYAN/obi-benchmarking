
import sys

def main():
    data = sys.stdin.read().split()
    D = int(data[0])
    A = int(data[1])
    N = int(data[2])

    total = 0
    days_stayed = 32 - N

    for day in range(1, days_stayed + 1):
        if N + day - 1 <= 15:
            diaria = D + A * (day - 1)
        else:
            diaria = D + A * 14
        total += diaria

    print(total)

if __name__ == "__main__":
    main()
