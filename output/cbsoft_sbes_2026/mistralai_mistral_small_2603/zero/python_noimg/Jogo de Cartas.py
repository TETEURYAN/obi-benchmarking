
import sys

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    cards = list(map(int, data[1:n+1]))

    rounds = 0
    current = 1
    pos = 0

    while current <= n:
        rounds += 1
        while pos < n:
            if cards[pos] == current:
                current += 1
                pos += 1
                break
            pos += 1
        else:
            pos = 0

    print(rounds)

if __name__ == "__main__":
    main()
