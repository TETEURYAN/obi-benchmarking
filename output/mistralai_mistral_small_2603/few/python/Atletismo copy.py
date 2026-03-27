
import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return

    n = int(data[0])
    arrival_order = list(map(int, data[1:n+1]))

    positions = [0] * (n + 1)
    for position, athlete in enumerate(arrival_order, start=1):
        positions[athlete] = position

    for i in range(1, n + 1):
        print(positions[i])

if __name__ == "__main__":
    main()
